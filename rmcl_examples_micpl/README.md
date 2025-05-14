# MICP-L Overview

Three sensors, four wheels, and many worlds.




See all options:
```console
ros2 launch rmcl_examples_sim start_robot_launch.py -s
```

In the following example we vary the three parameters `lidar3d`, `lidar2d`, `rgbd_camera` to enable certain sensors and `map` to select a world.

First, we want to see how each sensor data looks like. So we enable every sensor and select, eg, the `avz` world:

```console
ros2 launch rmcl_examples_sim start_robot_launch.py lidar3d:=True lidar2d:=True rgbd_camera:=True map:=avz
```

![RMCL sim all sensors](.media/rmcl_examples_sim_allsensors_avz.png)

With RViz you can visualize the sensor data of all three sensors:
```console
ros2 launch rmcl_examples_micpl rmcl_rviz_sensors.launch
```

![RViz all sensors](.media/rmcl_examples_rviz_allsensors_avz.png)



## MICP-L

Now we want to localize the robot continuously relative to the map using the MICP-L method.

### 3D LiDAR

Start the simulation with only the LiDAR enabled:

```console
ros2 launch rmcl_examples_sim start_robot_launch.py lidar3d:=True lidar2d:=False rgbd_camera:=False map:=avz
```

Start MICP-L via

```console
ros2 launch rmcl_examples_micpl rmcl_micpl_lidar3d.launch map:=avz gui:=True
```

an RViz window opens

![MICP-L LiDAR3D](.media/rmcl_examples_micpl_lidar3d.png)

Now you can provide new pose guesses using the `2D Pose Estimate` or `Mesh Pose Estimate` tool from the tools panel on top.
The correspondences are visualized as marker gray-ish hair.

### Depth Camera

Start the simulated robot and enable only the RGB-D camera.

```console
ros2 launch rmcl_examples_sim start_robot_launch.py lidar3d:=False lidar2d:=False rgbd_camera:=True map:=tray
```

Start the following launch file

```console
ros2 launch rmcl_examples_micpl rmcl_micpl_depth.launch gui:=True
```

![RMCL MICP-L RGB-D](.media/rmcl_examples_micpl_depth.png)


- MICP-L uses a filtered version of the RGB-D camera (`RGB-D Camera/PreProcessed`). Visualize the original point cloud by enabling `RGB-D Camera/Data`.
- Teleop the robot


### 2D LiDAR


### Wheels


## Worlds
