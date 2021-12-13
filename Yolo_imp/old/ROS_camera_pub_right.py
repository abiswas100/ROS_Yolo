#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import os
import time
try:
    import cv2
except ImportError:
    import sys
    ros_path = '/opt/ros/kinetic/lib/python2.7/dist-packages'
    sys.path.remove(ros_path)
    import cv2
    sys.path.append(ros_path)


# Image Publisher 
def talker():
#   rospy.loginfo("here")
  pub = rospy.Publisher('Yolo_Publish_right', Image, queue_size=1)
  rospy.init_node('Yolo_Image_right', anonymous = False)
  rate = rospy.Rate(10)
  while not rospy.is_shutdown():
    os.chdir(r"Yolo_Output_right")
    for f in os.listdir():
      print(f)
      
      image = cv2.imread(f)
      # print(len(image))
      bridge = CvBridge()
      time.sleep(0.5)
      msg = bridge.cv2_to_imgmsg(image)
      # print(msg)
      pub.publish(msg)
    os.chdir("../")
    

  if rospy.is_shutdown():pass

    
if __name__ == '__main__':
  try: 
    talker()
  except rospy.ROSInterruptException: pass
  talker()

  while not rospy.is_shutdown():
    rospy.spin()