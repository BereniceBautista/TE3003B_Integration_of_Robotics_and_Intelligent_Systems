# Install script for directory: /home/jose/Documents/8th_semester/robotica_final/TE3003B_Integration_of_Robotics_and_Intelligent_Systems/team_ws/src/mini_challenge_1

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/jose/Documents/8th_semester/robotica_final/TE3003B_Integration_of_Robotics_and_Intelligent_Systems/team_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/jose/Documents/8th_semester/robotica_final/TE3003B_Integration_of_Robotics_and_Intelligent_Systems/team_ws/build/mini_challenge_1/catkin_generated/installspace/mini_challenge_1.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/mini_challenge_1/cmake" TYPE FILE FILES
    "/home/jose/Documents/8th_semester/robotica_final/TE3003B_Integration_of_Robotics_and_Intelligent_Systems/team_ws/build/mini_challenge_1/catkin_generated/installspace/mini_challenge_1Config.cmake"
    "/home/jose/Documents/8th_semester/robotica_final/TE3003B_Integration_of_Robotics_and_Intelligent_Systems/team_ws/build/mini_challenge_1/catkin_generated/installspace/mini_challenge_1Config-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/mini_challenge_1" TYPE FILE FILES "/home/jose/Documents/8th_semester/robotica_final/TE3003B_Integration_of_Robotics_and_Intelligent_Systems/team_ws/src/mini_challenge_1/package.xml")
endif()
