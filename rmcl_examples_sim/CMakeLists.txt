cmake_minimum_required(VERSION 3.8)
project(rmcl_examples_sim VERSION 2.2.0)

# find dependencies
find_package(ament_cmake REQUIRED)

# Install Directories
install(DIRECTORY config models urdf worlds launch rviz
    DESTINATION share/${PROJECT_NAME}
)

ament_package()
