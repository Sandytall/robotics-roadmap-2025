# Basic RobotState class.
# Run: `python robot_state.py`

from dataclasses import dataclass

@dataclass
class RobotState:
    x: float = 0.0
    y: float = 0.0
    vx: float = 0.0
    vy: float = 0.0

    def step(self, dt: float) -> None:
        # Advance the state by dt seconds.
        self.x += self.vx * dt
        self.y += self.vy * dt

def demo() -> None:
    s = RobotState(x=0, y=0, vx=1.0, vy=0.5)
    for i in range(5):
        s.step(0.1)
        print(f"t={(i+1)*0.1:.1f}s -> pos=({s.x:.3f},{s.y:.3f}), vel=({s.vx:.2f},{s.vy:.2f})")

if __name__ == "__main__":
    demo()
