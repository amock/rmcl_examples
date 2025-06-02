# rmcl_examples

Examples to test and demonstrate the functionalities of the [rmcl](https://github.com/uos/rmcl) ROS package.

## Simulation

In the [`rmcl_examples_sim`](/rmcl_examples_sim/) packages are placed several simulation environments to spawn a mobile robot in.



The robot can be loaded into one simulation by calling

```console
ros2 launch rmcl_examples_sim start_robot_launch.py map:=tray
```

The environment can be changed by either changing the launch file's default arguments or via command line. For further details and what maps are available, see [`rmcl_examples_sim`](/rmcl_examples_sim/).

## Maps

The [`rmcl_examples_maps`](/rmcl_examples_maps/) contains mesh maps each of which corresponds to one (same named) simulation environment.

- [mesh_tools](https://github.com/naturerobots/mesh_tools)

```console
ros2 launch rmcl_examples_maps show_map.launch map:=tray
```

Those maps can are used throughout the examples as reference map for [RMCL](https://github.com/uos/rmcl) to localize a robot. See [`rmcl_examples_maps`](/rmcl_examples_maps/) for further details.

## MICP-L - Quickstart

To start MICP-L (Mesh ICP Localization), run

```console
ros2 launch rmcl_examples rmcl_micp.launch map:=tray gui:=True
```

**Note**: the map has to match the environment that have been used with the simulation!

The argument `gui:=True` courses a preconfigured RViz windows to open.
After that you can set a pose in RViz via `2D Pose Estimate` and see the robot localizing itself given the range measurements of the Velodyne LiDAR. Alternatively, you can use the `Mesh Pose Guess` tool of [`mesh_tools`](https://github.com/naturerobots/mesh_tools) to provide a pose guess on the mesh.

![MICP](.media/rmcl_micp_1280.gif)


### MICP-L - Examples

#### 1. [Overview](/rmcl_examples_micpl/)

Three sensors, four wheels, and many worlds.

#### 2. [Conversions](/rmcl_examples_conversions/)

Use you own data for MICP-L. Message conversions explained.

#### 3. [Segmentation](/rmcl_examples_micpl_segmentation/)

Filter expected parts of you sensor data and mark the unexpected parts of the data and the map.

#### 4. [Node Composition](/rmcl_examples_micpl_composition/)

Let the sensor data flow more efficiently to MICP-L.

#### 5. [Sensor Combinations](/rmcl_examples_micpl_combinations/)

Combine several sensors and use all at once.

#### 6. [GPU Acceleration](/rmcl_examples_micpl_gpu/)

Accelerate the registration process using hardware-accelerated ray tracing.

#### 7. [Parameters](/rmcl_examples_micpl_parameters)

Tune the parameters of MICP-L for your needs.



## Branch Compatibility

|  RMCL Branch    |  Supported ROS 2 versions    |
|:----|:----|
|  main   |  humble, jazzy |
