# How-To: Pipe into TinyEar

```bash
tinyhowl coo - | tinyear ingest - --out /tmp/ear --stem coo
TINYHOWL_ROOT=../tinyhowl make -C ../TinyEar pipe
```

Howl is a *test* dependency for Ear, not a runtime one.
