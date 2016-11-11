cmake_minimum_required(VERSION 2.8.3)
project(onshape_robot_tools)

find_package(catkin REQUIRED)

catkin_python_setup()

catkin_package()

#############
## Install ##
#############

install(PROGRAMS
  scripts/robot_from_assembly
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY
  launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

