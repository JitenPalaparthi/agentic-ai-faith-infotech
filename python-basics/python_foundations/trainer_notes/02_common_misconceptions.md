# Common Python Misconceptions

- `is` is not a replacement for `==`.
- Default mutable parameters are shared across calls.
- Assignment does not copy an object.
- A tuple can contain mutable objects.
- Threads are useful for many I/O-bound workloads despite the GIL.
- Multiprocessing has serialization and process startup costs.
- Asyncio is cooperative concurrency, not automatic parallelism.
- Type hints are not runtime enforcement by default.
- `finally` is for cleanup and executes even when exceptions propagate.
