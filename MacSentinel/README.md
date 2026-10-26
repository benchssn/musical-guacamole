# MacSentinel v0.1

A beginner-friendly, local macOS behavioral anomaly detector built in stages.

## Stage 1 — minimal project (complete)

Verified with Python 3.14.0 and psutil 7.1.3, already installed on this Mac.
No download or installation is needed in this environment.
`requirements.txt` records the installed dependency version.

From this project folder, check prerequisites without collecting measurements:

```sh
python3 macsentinel.py
```

`python3 macsentinel.py check` does the same thing.

## Stage 2 — collect local CSV samples (complete)

Start with a short recording:

```sh
python3 macsentinel.py sample --count 10 --interval 1
```

Each row contains:

| Column | Meaning |
| --- | --- |
| timestamp_utc | UTC timestamp at the end of measurement, with timezone offset |
| cpu_percent | System CPU utilization, averaged over the interval, from 0–100% |
| memory_percent | System memory utilization from psutil, from 0–100% |
| process_count | Number of process IDs visible at that moment |

CPU usage is averaged across the Mac's CPUs. Memory utilization follows psutil's
macOS accounting; it may differ from Activity Monitor's memory displays.
Memory and process count are snapshots taken after the CPU window.
Processes can start or exit while a sample is being collected.

The default is 10 samples with one-second CPU windows, taking roughly 10 seconds.
The interval must be between 1 and 3600 seconds; count must be a positive integer.
There is a small amount of extra time between windows for collecting and writing.

Each run creates a new `data/samples_<UTC timestamp>.csv` beside the script,
regardless of the folder you run the command from. Earlier recordings are preserved.
Completed rows are flushed to disk after each sample. Ctrl+C stops recording and
keeps completed rows; stopping before the first sample leaves a header-only CSV.
Use `python3 macsentinel.py sample --help` for options.

These recordings are raw measurements. Sampling does not update an existing baseline.

## Stage 3 — build a baseline (complete)

A baseline summarizes a recording you choose. The mean is the average value;
standard deviation describes how much values vary around that average. We use
sample standard deviation (dividing variance by n−1).

Record a session during your usual activity, for example ten minutes:

```sh
python3 macsentinel.py sample --count 120 --interval 5
```

Then use the exact CSV path printed by that command:

```sh
python3 macsentinel.py baseline --input data/samples_YOUR_TIMESTAMP.csv
```

Replace `samples_YOUR_TIMESTAMP.csv` with your actual filename. Relative input
paths are resolved from your current terminal folder. Each baseline is a new
`data/baseline_<timestamp>.json` file beside the script. It records the source CSV,
sample count, observation times, duration, and each metric's mean and standard
deviation. Earlier baselines and raw recordings are preserved. Later recordings
will not change this baseline automatically.

At least 30 samples are required as a learning guardrail, not a guarantee of a
representative baseline. A short verification run only confirms the feature works.
Use longer recordings covering normal work before drawing conclusions. Successive
samples can be correlated, and the three metrics need not follow a normal distribution.
Use the same sampling interval for later comparisons because CPU averaging depends
on it; this CSV format does not record the configured interval.

Malformed columns, missing values, non-finite or out-of-range measurements, invalid
process counts, and non-increasing or non-UTC timestamps are rejected before saving.
Constant metrics are saved with zero standard deviation and `zero_variance: true`;
a later detector must handle these without dividing by zero. No alerts run yet.

## Next stage — not implemented yet

4. Compare new samples against that baseline, handling zero variance and too few
   samples explicitly. Explain alerts as unusual measurements, not proof of malware.

Each stage will be explained and verified before moving to the next.

## Boundaries

No network scanning, external transmission, administrator privileges, process
termination, or automatic startup. Samples contain aggregate measurements,
not process names, command lines, or file contents. All project data stays in
`data/` unless you explicitly copy or share it. This is a learning tool; statistical
deviations alone cannot establish whether a Mac is compromised.
