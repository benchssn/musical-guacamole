"""MacSentinel v0.1: local macOS behavioral monitoring, built in stages."""

import argparse
import csv
import math
import json
import platform
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

VERSION = "0.1.0"
DATA_DIR = Path(__file__).resolve().parent / "data"
FIELDS = ["timestamp_utc", "cpu_percent", "memory_percent", "process_count"]
MIN_BASELINE_SAMPLES = 30


def build_baseline(source):
    """Validate an explicitly selected recording and save its summary separately."""
    source = source.expanduser().resolve(strict=True)
    values = {name: [] for name in FIELDS[1:]}
    timestamps = []
    with source.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, strict=True)
        if reader.fieldnames != FIELDS:
            raise ValueError(f"CSV columns must be: {', '.join(FIELDS)}")
        for line, row in enumerate(reader, start=2):
            try:
                if None in row or any(value is None for value in row.values()):
                    raise ValueError("wrong number of columns")
                stamp = datetime.fromisoformat(row["timestamp_utc"])
                if stamp.utcoffset() is None or stamp.utcoffset().total_seconds() != 0:
                    raise ValueError("timestamp must include UTC offset")
                if timestamps and stamp <= timestamps[-1]:
                    raise ValueError("timestamps must increase")
                parsed = {name: float(row[name]) for name in values}
                for name, value in parsed.items():
                    if not math.isfinite(value):
                        raise ValueError(f"{name} must be finite")
                    if name == "process_count":
                        if value < 1 or not value.is_integer():
                            raise ValueError("process_count must be a positive integer")
                    elif not 0 <= value <= 100:
                        raise ValueError(f"{name} must be between 0 and 100")
            except (ValueError, TypeError) as error:
                raise ValueError(f"Invalid CSV row {line}: {error}") from None
            timestamps.append(stamp)
            for name, value in parsed.items():
                values[name].append(value)
    count = len(timestamps)
    if count < MIN_BASELINE_SAMPLES:
        raise ValueError(f"Baseline needs at least {MIN_BASELINE_SAMPLES} samples; found {count}. Record a longer session.")
    metrics = {
        name: {"mean": statistics.mean(series),
               "stddev": statistics.stdev(series),
               "zero_variance": min(series) == max(series)}
        for name, series in values.items()
    }
    now = datetime.now(timezone.utc)
    baseline = {
        "schema_version": 1,
        "created_at_utc": now.isoformat(),
        "source_csv": str(source),
        "sample_count": count,
        "first_sample_utc": timestamps[0].isoformat(),
        "last_sample_utc": timestamps[-1].isoformat(),
        "duration_seconds": (timestamps[-1] - timestamps[0]).total_seconds(),
        "stddev_method": "sample (n-1)",
        "metrics": metrics,
    }
    destination = DATA_DIR / f"baseline_{now.strftime('%Y%m%dT%H%M%S_%fZ')}.json"
    with destination.open("x", encoding="utf-8") as handle:
        json.dump(baseline, handle, indent=2, allow_nan=False)
        handle.write("\n")
    print(f"Baseline built from {count} samples. Saved to {destination}")
    for name, metric in metrics.items():
        print(f"{name}: mean {metric['mean']:.3f}, standard deviation {metric['stddev']:.3f}")
        if metric["zero_variance"]:
            print(f"  {name} did not vary. A later detector must not divide by its zero standard deviation.")
    print("This describes the selected recording; it does not establish that activity is safe or representative.")
    return 0


def positive_count(value):
    """Reject invalid sample counts before creating a file."""
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("must be a positive whole number") from None
    if number < 1:
        raise argparse.ArgumentTypeError("must be a positive whole number")
    return number


def sample_interval(value):
    """Use a finite, bounded CPU measurement window."""
    try:
        number = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError("must be a number from 1 to 3600 seconds") from None
    if not math.isfinite(number) or not 1 <= number <= 3600:
        raise argparse.ArgumentTypeError("must be a number from 1 to 3600 seconds")
    return number


def collect_samples(psutil, count, interval):
    """Write a separate CSV for each run, preserving earlier recordings."""
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    destination = DATA_DIR / f"samples_{stamp}.csv"
    completed = 0
    print(f"Recording {count} samples with a {interval:g}-second CPU window.")
    print(f"CSV: {destination}")
    print("Press Ctrl+C to stop; completed rows will be kept.")
    with destination.open("x", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        handle.flush()
        try:
            for index in range(count):
                # Blocking measurement: average system CPU usage over this window.
                cpu = psutil.cpu_percent(interval=interval)
                memory = psutil.virtual_memory().percent
                processes = len(psutil.pids())
                row = {
                    "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
                    "cpu_percent": cpu,
                    "memory_percent": memory,
                    "process_count": processes,
                }
                writer.writerow(row)
                handle.flush()
                completed += 1
                print(f"{index + 1}/{count}: CPU {cpu:.1f}% | memory {memory:.1f}% | processes {processes}")
        except KeyboardInterrupt:
            print("\nRecording stopped.")
    print(f"Saved {completed} samples to {destination}")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command")
    commands.add_parser("check", help="check prerequisites without collecting data")
    sample = commands.add_parser("sample", help="save aggregate system measurements locally")
    sample.add_argument("--count", type=positive_count, default=10, help="number of samples (default: 10)")
    sample.add_argument("--interval", type=sample_interval, default=1.0, help="CPU window in seconds, 1–3600 (default: 1)")
    baseline = commands.add_parser("baseline", help="build a statistical baseline from a chosen CSV")
    baseline.add_argument("--input", required=True, type=Path, help="CSV recording to use for the baseline")
    args = parser.parse_args()
    if platform.system() != "Darwin":
        print("This beginner project currently supports macOS only.", file=sys.stderr)
        return 1
    try:
        import psutil
    except ImportError:
        print("psutil is missing from this Python environment.", file=sys.stderr)
        return 1
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if args.command == "baseline":
            return build_baseline(args.input)
        if args.command == "sample":
            return collect_samples(psutil, args.count, args.interval)
        print(f"MacSentinel {VERSION} — startup check")
        print(f"Python: {platform.python_version()}")
        print(f"psutil: {psutil.__version__}")
        print(f"Local data folder: {DATA_DIR}")
        print("Startup check passed. No measurements collected.")
        return 0
    except (OSError, ValueError, csv.Error, psutil.Error) as error:
        print(f"MacSentinel could not complete the operation: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
