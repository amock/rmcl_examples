import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, FindExecutable
from launch.substitutions import LaunchConfiguration, PythonExpression, PathJoinSubstitution


def generate_launch_description():
    # path to this pkg
    pkg_rmcl_sim = get_package_share_directory(
        "rmcl_sim"
    )

    # Launch arguments
    launch_args = [
        DeclareLaunchArgument(
            "map",
            description="Name of the map used for simulation"
            + '(see mesh_navigation_tutorials\' "worlds" directory).',
            default_value="tray",
            choices=["tray", "cube", "sphere", "cylinder", "corridor", "trays", "avz"],
        ),
        DeclareLaunchArgument(
            "start_gazebo_gui",
            description="Start Gazebo GUI",
            default_value="True",
            choices=["True", "False"],
        ),
        DeclareLaunchArgument(
            "velodyne_vlp16",
            description="Simulate Velodyne VLP-16 Sensor (3D LiDAR)",
            default_value="True",
            choices=["True", "False"],
        ),
        DeclareLaunchArgument(
            "sick_tim",
            description="Simulate Sick Tim sensor (2D LiDAR)",
            default_value="False",
            choices=["True", "False"],
        ),
        DeclareLaunchArgument(
            "asus_xtion",
            description="Simulate Asus Xtion sensor",
            default_value="False",
            choices=["True", "False"],
        ),
    ]
    map_name = LaunchConfiguration("map")
    map_path = PathJoinSubstitution(
        [
            pkg_rmcl_sim,
            "worlds",
            PythonExpression(['"rmcl_', map_name, '.sdf"']),
        ]
    )
    start_gazebo_gui = LaunchConfiguration("start_gazebo_gui")

    # sensors
    velodyne_vlp16 = LaunchConfiguration("velodyne_vlp16")
    sick_tim = LaunchConfiguration("sick_tim")
    asus_xtion = LaunchConfiguration("asus_xtion")

    robot_description = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution([pkg_rmcl_sim, "urdf/ceres.urdf.xacro"]),
            " name:=robot",
            " prefix:='robot'",
            " is_sim:=true",
            PythonExpression(['" sick_tim:=true" if ', sick_tim, ' else " sick_tim:=false"']),
            PythonExpression(['" velodyne_vlp16:=true" if ', velodyne_vlp16, ' else " velodyne_vlp16:=false"']),
            PythonExpression(['" asus_xtion:=true" if ', asus_xtion, ' else " asus_xtion:=false"']),
        ]
    )

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[
            {
                "use_sim_time": True,
                "publish_frequency": 100.0,
                "robot_description": robot_description,
            }
        ],
    )

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [get_package_share_directory("ros_gz_sim"), "launch", "gz_sim.launch.py"]
            )
        ),
        launch_arguments={
            "gz_args": [
                "-r ",
                map_path,  # which world to load
                PythonExpression(
                    ['"" if ', start_gazebo_gui, ' else " -s"']
                ),  # whether to start gui
            ]
        }.items(),
    )

    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        name="spawn_robot",
        output="screen",
        arguments=[
            "-topic",
            "robot_description",
            "-name",
            # The robot's name in simulation is always "robot", regardless of which model is chosen
            # This facilitates easier topic bridging.
            "robot",
            "-z",
            "1",
        ],
        parameters=[
            {"use_sim_time": True},
        ],
    )

    # Bridge between ROS and Gazebo
    bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        parameters=[
            {
                "config_file": PathJoinSubstitution(
                    [pkg_rmcl_sim, "config", "ros_gazebo_bridge.yaml"]
                ),
            }
        ],
        output="screen",
    )

    # odom -> base_footprint
    ekf = Node(
        package="robot_localization",
        executable="ekf_node",
        name="ekf_filter_node",
        output="screen",
        parameters=[
            {"use_sim_time": True},
            PathJoinSubstitution([pkg_rmcl_sim, "config", "ekf.yaml"]),
        ],
    )

    return LaunchDescription(launch_args + [gz_sim, spawn_robot, bridge, robot_state_publisher, ekf])