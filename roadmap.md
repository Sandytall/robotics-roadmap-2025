# 📅 Daily Plan (Aug 19 → Nov 15, 2025)

## Phase 1: Foundations (Aug 19 – Sep 8, 3 weeks)
**Goal:** Python, C++, Math, Core CV  
**Simulator:** Not yet, focus on math + perception

### Week 1: Python & C++ Foundations
1. **Day 1 (Aug 19):** Python OOP for robot states → *Task:* Build `RobotState` class with position/velocity. → [log](logs/Day01.md)
2. **Day 2:** NumPy & SciPy → *Task:* Simulate robot trajectory with equations of motion. → [log](logs/Day02.md)
3. **Day 3:** Python threading → *Task:* Simulate two sensors running in parallel. → [log](logs/Day03.md)
4. **Day 4:** C++ OOP → *Task:* C++ class for a motor driver. → [log](logs/Day04.md)
5. **Day 5:** Smart pointers, templates → *Task:* Create generic `Sensor<T>` template class. → [log](logs/Day05.md)
6. **Day 6:** CMake & real-time → *Task:* Compile + run threaded sensor code. → [log](logs/Day06.md)
7. **Day 7:** Mini-project → Hybrid Python+C++ sensor simulator. → [log](logs/Day07.md)

### Week 2: Math Foundations
8. **Day 8:** Rotation matrices/quaternions → *Task:* Implement rotation conversions in Python. → [log](logs/Day08.md)
9. **Day 9:** Homogeneous transforms → *Task:* Transform 3D point between frames. → [log](logs/Day09.md)
10. **Day 10:** Eigenvalues, SVD → *Task:* PCA on noisy 2D robot path. → [log](logs/Day10.md)
11. **Day 11:** Probability basics → *Task:* Gaussian noise generator. → [log](logs/Day11.md)
12. **Day 12:** Bayes filtering → *Task:* Bayesian update for a 1D sensor. → [log](logs/Day12.md)
13. **Day 13:** Monte Carlo → *Task:* Particle motion simulator. → [log](logs/Day13.md)
14. **Day 14:** Mini-project → 2D noisy robot localization with particles. → [log](logs/Day14.md)

### Week 3: Computer Vision Basics
15. **Day 15:** OpenCV basics → *Task:* Apply filters on live webcam feed. → [log](logs/Day15.md)
16. **Day 16:** Feature detection → *Task:* Compare ORB vs FAST on test images. → [log](logs/Day16.md)
17. **Day 17:** Optical flow → *Task:* Track moving ball in video. → [log](logs/Day17.md)
18. **Day 18:** Camera calibration → *Task:* Calibrate webcam with chessboard. → [log](logs/Day18.md)
19. **Day 19:** Distortion correction → *Task:* Undistort live webcam feed. → [log](logs/Day19.md)
20. **Day 20:** Stereo basics → *Task:* Create disparity map from stereo dataset. → [log](logs/Day20.md)
21. **Day 21:** Mini-project → Feature tracker on video feed. → [log](logs/Day21.md)

## Phase 2: Core Robotics (Sep 9 – Oct 6, 4 weeks)
**Goal:** ROS2, TF2, LiDAR, Fusion  
**Simulator:** Start Gazebo + Isaac Sim

### Week 4: ROS2
22. **Day 22:** ROS2 nodes/topics → *Task:* Publish/subscribe to sensor topic. → [log](logs/Day22.md)
23. **Day 23:** Services & actions → *Task:* Implement a “move robot” service. → [log](logs/Day23.md)
24. **Day 24:** QoS → *Task:* Experiment with best-effort vs reliable messages. → [log](logs/Day24.md)
25. **Day 25:** Lifecycle nodes → *Task:* Node startup/shutdown transitions. → [log](logs/Day25.md)
26. **Day 26:** Custom ROS2 message → *Task:* Define `SensorReading.msg`. → [log](logs/Day26.md)
27. **Day 27:** Launch files → *Task:* Multi-node launch with parameters. → [log](logs/Day27.md)
28. **Day 28:** Mini-project → Gazebo TurtleBot3 teleop package. → [log](logs/Day28.md)

### Week 5: TF2 & Frames
29. **Day 29:** TF2 basics → *Task:* Broadcast `base_link → laser` frame. → [log](logs/Day29.md)
30. **Day 30:** Frame hierarchy → *Task:* `map–odom–base_link` tree in RViz. → [log](logs/Day30.md)
31. **Day 31:** TF listener → *Task:* Transform laser scan points to `base_link`. → [log](logs/Day31.md)
32. **Day 32:** Time sync → *Task:* Handle delayed transform lookup. → [log](logs/Day32.md)
33. **Day 33:** Multi-sensor calibration → *Task:* Align camera + LiDAR. → [log](logs/Day33.md)
34. **Day 34:** Debug TF tree → *Task:* Visualize in RViz. → [log](logs/Day34.md)
35. **Day 35:** Mini-project → TF2 tree for TurtleBot3 simulation. → [log](logs/Day35.md)

### Week 6: LiDAR & PCL
36. **Day 36:** Load LiDAR scan → *Task:* Convert ROS2 scan → PCL cloud. → [log](logs/Day36.md)
37. **Day 37:** Filtering → *Task:* Apply voxel grid + passthrough filter. → [log](logs/Day37.md)
38. **Day 38:** Segmentation → *Task:* Cluster obstacles in RViz. → [log](logs/Day38.md)
39. **Day 39:** ICP registration → *Task:* Align two point clouds. → [log](logs/Day39.md)
40. **Day 40:** NDT → *Task:* Compare ICP vs NDT mapping. → [log](logs/Day40.md)
41. **Day 41:** Ground plane removal → *Task:* RANSAC plane fit. → [log](logs/Day41.md)
42. **Day 42:** Mini-project → Obstacle detection in Gazebo LiDAR sim. → [log](logs/Day42.md)

### Week 7: Sensor Fusion
43. **Day 43:** EKF → *Task:* 1D robot tracking with wheel odometry. → [log](logs/Day43.md)
44. **Day 44:** EKF in ROS2 → *Task:* Fuse odometry + IMU with `robot_localization`. → [log](logs/Day44.md)
45. **Day 45:** UKF → *Task:* Nonlinear heading tracking. → [log](logs/Day45.md)
46. **Day 46:** Particle filter → *Task:* Localize TurtleBot3 in Gazebo. → [log](logs/Day46.md)
47. **Day 47:** Camera + LiDAR fusion → *Task:* Align depth map with cloud. → [log](logs/Day47.md)
48. **Day 48:** Factor graph basics → *Task:* Pose graph optimization. → [log](logs/Day48.md)
49. **Day 49:** Mini-project → Sensor fusion for localization (Gazebo + Isaac Sim). → [log](logs/Day49.md)

## Phase 3: Applications (Oct 7 – Nov 3, 4 weeks)
**Goal:** SLAM, Nav2, AMRs, Deployment  
**Simulator:** Gazebo for Nav2, Isaac Sim for multi-robot

### Week 8: SLAM
50. **Day 50:** ORB-SLAM2 → *Task:* Run on recorded dataset. → [log](logs/Day50.md)
51. **Day 51:** Loop closure → *Task:* Visualize map corrections. → [log](logs/Day51.md)
52. **Day 52:** RTAB-Map → *Task:* Run in Gazebo TurtleBot3. → [log](logs/Day52.md)
53. **Day 53:** Cartographer → *Task:* LiDAR SLAM in Gazebo. → [log](logs/Day53.md)
54. **Day 54:** Hector/GMapping → *Task:* Compare performance. → [log](logs/Day54.md)
55. **Day 55:** Isaac Sim visual SLAM → *Task:* Run Isaac navigation demo. → [log](logs/Day55.md)
56. **Day 56:** Mini-project → SLAM + Nav2 TurtleBot3 world map. → [log](logs/Day56.md)

### Week 9: Path Planning
57. **Day 57:** A* → *Task:* Grid-based path planner in Python. → [log](logs/Day57.md)
58. **Day 58:** RRT → *Task:* Generate random tree planner. → [log](logs/Day58.md)
59. **Day 59:** RRT* → *Task:* Optimize path planning. → [log](logs/Day59.md)
60. **Day 60:** DWA → *Task:* Simulate robot avoidance. → [log](logs/Day60.md)
61. **Day 61:** MPC basics → *Task:* Implement in Python. → [log](logs/Day61.md)
62. **Day 62:** Nav2 deep dive → *Task:* Custom planner plugin. → [log](logs/Day62.md)
63. **Day 63:** Mini-project → Nav2 custom planner in Gazebo. → [log](logs/Day63.md)

### Week 10: AMR Systems
64. **Day 64:** AMR fleet management → *Task:* Multi-robot tasks in Gazebo. → [log](logs/Day64.md)
65. **Day 65:** Auction-based allocation → *Task:* Assign tasks to 2 robots. → [log](logs/Day65.md)
66. **Day 66:** Dynamic obstacle avoidance → *Task:* Add moving humans in Isaac Sim. → [log](logs/Day66.md)
67. **Day 67:** Human-robot safety → *Task:* Define safe zones. → [log](logs/Day67.md)
68. **Day 68:** Docking → *Task:* TurtleBot auto-docking simulation. → [log](logs/Day68.md)
69. **Day 69:** ISO safety standards → *Task:* Implement E-stop in ROS2 node. → [log](logs/Day69.md)
70. **Day 70:** Mini-project → Multi-robot coordination in Isaac Sim. → [log](logs/Day70.md)

### Week 11: Deployment
71. **Day 71:** Real-time OS → *Task:* Priority scheduling test. → [log](logs/Day71.md)
72. **Day 72:** ROS2 DDS tuning → *Task:* Compare FastDDS vs CycloneDDS. → [log](logs/Day72.md)
73. **Day 73:** Docker → *Task:* Containerize ROS2 SLAM stack. → [log](logs/Day73.md)
74. **Day 74:** CI/CD → *Task:* GitHub Actions for ROS2 build/test. → [log](logs/Day74.md)
75. **Day 75:** OTA updates → *Task:* Push Docker image to Pi/Jetson. → [log](logs/Day75.md)
76. **Day 76:** Hardware-in-loop → *Task:* Run robot_localization with real IMU. → [log](logs/Day76.md)
77. **Day 77:** Mini-project → ROS2 Dockerized SLAM on Jetson. → [log](logs/Day77.md)

## Phase 4: Specialization (Nov 4 – Nov 15, 1.5 weeks)
**Goal:** Advanced CV, AI/ML, RL  
**Simulator:** Isaac Sim for RL & multi-sensor

78. **Day 78:** Transformers for vision → *Task:* Run ViT on dataset. → [log](logs/Day78.md)
79. **Day 79:** Multi-modal learning → *Task:* Fuse camera + LiDAR with deep learning. → [log](logs/Day79.md)
80. **Day 80:** 3D semantic mapping → *Task:* Semantic SLAM in Isaac. → [log](logs/Day80.md)
81. **Day 81:** RL basics → *Task:* Train robot to reach goal in Isaac Sim. → [log](logs/Day81.md)
82. **Day 82:** Sim-to-real RL → *Task:* Domain randomization test. → [log](logs/Day82.md)
83. **Day 83:** Edge AI → *Task:* Quantize CNN with TensorRT. → [log](logs/Day83.md)
84. **Day 84:** Swarm robotics → *Task:* 3 robots cooperative navigation in Isaac Sim. → [log](logs/Day84.md)
85–87. **Days 85–87:** Capstone Build → SLAM + Nav2 + Fusion + Fleet Coordination. → [log](logs/Day85-87.md)
88. **Day 88 (Nov 15):** Portfolio polish + video demos. → [log](logs/Day88.md)
