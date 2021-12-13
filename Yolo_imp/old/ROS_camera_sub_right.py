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
import Yolo_new_right as Yolo

# import ROS_camera_pub as pub

import os
import shutil

def image_callback(msg: Image):
    
    # rospy.loginfo(Image)

    bridge = CvBridge()
    cv_img =  bridge.imgmsg_to_cv2(msg)
    
    
    yolo_output = Yolo.Yolo_imp(cv_img)
    # pub.talker(yolo_output)
    # # cv2.imshow('image window', yolo_output)
    # # # add wait key. window waits until user presses a key
    # # cv2.waitKey(0)
    # # # and finally destroy/close all open windows
    # # cv2.destroyAllWindows()



def main():
    
    path = os.getcwd()

    folder_path = path+'/Yolo_Output_right'
    
    if os.path.isdir(folder_path) is True: 
        # print(folder_path)
        shutil.rmtree(folder_path)
    
    rospy.init_node("Image_Sub_right")
    rospy.Subscriber("/multisense_sl/camera/camera_front/right/camera_front/image_raw", Image, image_callback, queue_size=1)
    
    while not rospy.is_shutdown():
        rospy.spin()
        # rospy.Subscriber("/multisense_sl/camera/camera_front/left/camera_front/image_raw", Image, image_callback, queue_size=1)

if __name__ == "__main__":
    main()