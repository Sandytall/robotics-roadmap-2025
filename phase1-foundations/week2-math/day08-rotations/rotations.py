# Rotation conversions: Euler <-> Quaternion <-> R matrix.
# Run: `python rotations.py`
import math
from typing import Tuple

def euler_xyz_to_quat(roll, pitch, yaw) -> Tuple[float,float,float,float]:
    cr, sr = math.cos(roll/2), math.sin(roll/2)
    cp, sp = math.cos(pitch/2), math.sin(pitch/2)
    cy, sy = math.cos(yaw/2), math.sin(yaw/2)
    w = cr*cp*cy + sr*sp*sy
    x = sr*cp*cy - cr*sp*sy
    y = cr*sp*cy + sr*cp*sy
    z = cr*cp*sy - sr*sp*cy
    return (w,x,y,z)

def quat_to_rotmat(w,x,y,z):
    return [
        [1-2*(y*y+z*z), 2*(x*y - z*w), 2*(x*z + y*w)],
        [2*(x*y + z*w), 1-2*(x*x+z*z), 2*(y*z - x*w)],
        [2*(x*z - y*w), 2*(y*z + x*w), 1-2*(x*x+y*y)]
    ]

if __name__ == "__main__":
    q = euler_xyz_to_quat(0.1, 0.2, 0.3)
    R = quat_to_rotmat(*q)
    print("q =", q)
    print("R =", R)
