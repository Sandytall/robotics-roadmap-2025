# Homogeneous transform application.
# Run: `python transform_point.py`
import numpy as np

def transform_point(T, p):
    p_h = np.r_[p, 1.0]
    return (T @ p_h)[:3]

if __name__ == "__main__":
    import numpy as np
    T = np.eye(4)
    T[:3,3] = [1,2,3]
    p = np.array([0.5, 0.0, -1.0])
    print(transform_point(T, p))
