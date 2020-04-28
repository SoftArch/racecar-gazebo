# Kudos to DOROWU for his amazing VNC 18.04 KDE image
FROM dorowu/ubuntu-desktop-lxde-vnc
LABEL maintainer "ahmet.kabaoglu@gmail.com"

#Install dirmngr
RUN apt-get update && apt-get install -y dirmngr

# Adding keys for ROS
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

# Installing ROS
RUN apt-get update && apt-get install -y ros-melodic-desktop-full \
		wget git nano
RUN rosdep init && rosdep update

# Update Gazebo 9
RUN sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
RUN wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
RUN apt-get update && apt-get install -y gazebo9 libignition-math2-dev

RUN apt-get install -y ros-melodic-gazebo-ros-control 
RUN apt-get install -y ros-melodic-ros-controllers

# Installing Atom Editor
RUN add-apt-repository ppa:webupd8team/atom && apt update && apt install -y atom

RUN /bin/bash -c "echo 'export HOME=/home/ubuntu' >> /root/.bashrc && source /root/.bashrc"
