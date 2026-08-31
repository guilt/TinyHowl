import time
from tinyhowl.params import baby_base
from tinyhowl.synth import frame_ms, synthesize_frame
p = baby_base(); phase = 0.0
t0 = time.perf_counter(); n = 200
for i in range(n):
    _, phase = synthesize_frame(p, phase, i / n)
elapsed_ms = (time.perf_counter() - t0) * 1000 / n
print(f"frame={frame_ms()}ms wall={elapsed_ms:.3f}ms/frame")
assert elapsed_ms < 8.0
