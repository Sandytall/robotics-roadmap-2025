# Gaussian noise generator (Box-Muller).
# Run: `python gaussian_noise.py`
import math, random

def gaussian(mu=0.0, sigma=1.0):
    u1, u2 = random.random(), random.random()
    z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2*math.pi*u2)
    return mu + sigma * z0

if __name__ == "__main__":
    print([round(gaussian(0,1),3) for _ in range(5)])
