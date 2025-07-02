cmake_minimum_required(VERSION 3.8)
project(rmcl_examples_maps VERSION 2.2.0)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)

install(DIRECTORY maps launch rviz
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
