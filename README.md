# racecar-gazebo
[MIT Racecar](https://github.com/mit-racecar) samples on gazebo-based simulator with Docker

Sample Video - ["ROS and Gazebo on Docker and show Lidar datas"](https://www.youtube.com/watch?v=M1NWQW8Tv60)

## Docker - ros/gazebo

#### Pull and Run Docker
  ```docker run -it --rm -p 6080:80 softarch/ros-gazebo```
  
  With Volume
  ```docker run -v racecar:/root/Desktop -it --rm -p 6080:80 softarch/ros-gazebo```

#### Connect VNC with browser
Open [http://localhost:6080/](http://localhost:6080/)



## Run Ros And Gazebo
#### Download Repo (step 1)
        cd Desktop/
        git clone https://github.com/SoftArch/racecar-gazebo.git

#### Build Workspace (step 2)
        cd Desktop/racecar-gazebo
        source /opt/ros/melodic/setup.bash
        catkin_make
        

#### Run Ros - Terminal 1 (step 3)
        cd Desktop/racecar-gazebo
        source devel/setup.bash
        roscore
        
        

#### Run Gazebo Empty World - Terminal 2 (step 4)
        cd Desktop/racecar-gazebo
        source devel/setup.bash
        roslaunch racecar_gazebo racecar.launch


#### Run Gazebo Simple World - Terminal 2 (step 4 alternative)
        cd Desktop/racecar-gazebo
        source devel/setup.bash
        roslaunch racecar_gazebo racecar_empty2.launch


#### Run Gazebo MIT Tunnel World - Terminal 2 (step 4 alternative)
        cd Desktop/racecar-gazebo
        source devel/setup.bash
        roslaunch racecar_gazebo racecar_tunnel.launch

  


