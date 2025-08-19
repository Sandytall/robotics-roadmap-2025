# Simple particle motion with process noise.
# Run: `python particles.py`
import random

def step(x, v, noise=0.01):
    return x + v + random.gauss(0, noise)

if __name__ == "__main__":
    x = 0.0
    for t in range(10):
        x = step(x, 1.0)
        print(t, x)
