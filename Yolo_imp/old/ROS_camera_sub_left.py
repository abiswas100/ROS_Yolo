from posix import listdir
import rospy
from sensor_msgs.msg import Image
try:
    import cv2
except ImportError:
    import sys
    ros_path = '/opt/ros/kinetic/lib/python2.7/dist-packages'
    sys.path.remove(ros_path)
    import cv2
    sys.path.append(ros_path)
from cv_bridge import CvBridge
import numpy as np
import Yolo_new_left as Yolo

import Yolo_new_left as Yolo_left
import Yolo_new_right as Yolo_right

import time
# import ROS_camera_pub as pub

import os
import shutil



rospy.init_node('Yolo', anonymous = False)
pub_left = rospy.Publisher('Yolo_Sub_Pub_Left', Image, queue_size=1)
# rospy.sleep(1)
pub_right = rospy.Publisher('Yolo_Sub_Pub_Right', Image, queue_size=1)
# rospy.sleep(1)
  

def image_callback_left(msg: Image):
    bridge = CvBridge()
    cv_img =  bridge.imgmsg_to_cv2(msg)
    
    yolo_output = Yolo_left.Yolo_imp(cv_img)
       
    left_output = bridge.cv2_to_imgmsg(yolo_output)
    pub_left.publish(left_output)


def image_callback_right(msg: Image):
    bridge = CvBridge()
    cv_img =  bridge.imgmsg_to_cv2(msg)
    # cv2.imwrite("waka1.jpg", cv_img)
    # end_time = time.perf_counter ()
    # print("Subsciber - ",end_time - start_time, "seconds")
    
    yolo_output = Yolo_right.Yolo_imp(cv_img)
       
    right_output = bridge.cv2_to_imgmsg(yolo_output)
    pub_right.publish(right_output)


def main():
    
    path = os.getcwd()

    folder_path_left = path+'/Yolo_Output_left'
    
    if (os.path.isdir(folder_path_left) is True) and (bool(os.listdir(folder_path_left)) == False): 
        # print(folder_path)
        shutil.rmtree(folder_path_left)
    
    
    folder_path_right = path+'/Yolo_Output_right'
    
    if (os.path.isdir(folder_path_right) is True) and (bool(os.listdir(folder_path_right)) == False): 
        # print(folder_path)
        shutil.rmtree(folder_path_right)
    
    # rospy.init_node("Image_Sub_Left")
    # print("getting here")
    rospy.Subscriber("/multisense_sl/camera/camera_front/left/camera_front/image_raw", Image, image_callback_left, queue_size=1)
    rospy.Subscriber("/multisense_sl/camera/camera_front/left/camera_front/image_raw", Image, image_callback_right, queue_size=1)
    
    while not rospy.is_shutdown():
        rospy.spin()
        
if __name__ == "__main__":
    main()