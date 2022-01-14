#include <ros/ros.h>
#include <std_msgs/String.h>
// #include "std_msgs/ImZZ

void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
    ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "listner");
}

ros::NodeHandle n;

ros::Subscriber sub = n.subscribe("/multisense_sl/camera/camera_front/left/camera_front/image_raw",1000,chatterCallback);