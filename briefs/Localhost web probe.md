**Lab brief: Localhost web probe**

**Goal.** Stand up a tiny HTTP server bound only to loopback, probe it with `curl`/`lsof`, then shut it down.

**Setup.**
```bash
mkdir -p /tmp/cyber-lab && echo '<h1>hello local lab</h1>' > /tmp/cyber-lab/index.html
cd /tmp/cyber-lab && python3 -m http.server 8765 --bind 127.0.0.1
```

**Probes (second tab).**
```bash
lsof -nP -iTCP:8765 -sTCP:LISTEN          # expect 127.0.0.1:8765
curl -sI http://127.0.0.1:8765/             # 200
curl -sI http://127.0.0.1:8765/nope.html    # 404
curl -s  http://127.0.0.1:8765/             # HTML body
curl -sI --connect-timeout 2 http://192.168.68.106:8765/ || echo "not reachable on LAN (good)"
```

**Teardown.** `Ctrl+C` in the server tab, then `lsof … || echo "port free"`.

**Takeaway.** Bind address decides who can reach you; status codes map what’s there; inventory before and after keeps the experiment honest.