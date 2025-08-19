# Simulate x'' = a with constant acceleration, integrate via NumPy-like loops.
# Run: `python trajectory.py`

def simulate(dt=0.01, T=2.0, a=1.0):
    n = int(T/dt)
    x = 0.0; v = 0.0
    xs = []
    for _ in range(n):
        v += a*dt
        x += v*dt
        xs.append(x)
    return xs

if __name__ == "__main__":
    xs = simulate()
    print(f"final x = {xs[-1]:.4f}, steps = {len(xs)}")
