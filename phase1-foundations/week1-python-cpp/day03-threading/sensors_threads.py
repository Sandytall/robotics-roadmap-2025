# Two sensor threads printing at different rates.
# Run: `python sensors_threads.py`
import threading, time

def sensor(name, period_s=0.2, count=5):
    for i in range(count):
        print(f"[{name}] reading {i}")
        time.sleep(period_s)

if __name__ == "__main__":
    t1 = threading.Thread(target=sensor, args=("imu", 0.1, 10))
    t2 = threading.Thread(target=sensor, args=("lidar", 0.25, 6))
    t1.start(); t2.start()
    t1.join(); t2.join()
    print("done")
