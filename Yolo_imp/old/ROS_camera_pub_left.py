#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import os
import time
import glob
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
  files = []
  # rospy.loginfo("here")
  pub = rospy.Publisher('Yolo_Publish_Left', Image, queue_size=1)
  rospy.init_node('Yolo_Image_Left', anonymous = False)
  rate = rospy.Rate(10)
  while not rospy.is_shutdown():
    try:
      os.chdir(r"Yolo_Output_left")
    except FileNotFoundError: time.sleep(0.5)
    # print(os.getcwd())
    # for i in 
    # list_of_files = glob.glob('/home/avhi/Desktop/ROS_Yolo/Yolo_imp/Yolo_Output_left') # * means all if need specific format then *.csv
    # print(list_of_files)
    # latest_file = max(list_of_files, key=os.path.getmtime)
    # print(latest_file)
    for f in os.listdir():
      time_begin = rospy.Time.now()
      print(f)      
      image = cv2.imread(f)
      # print(len(image))
      bridge = CvBridge()
      # time.sleep(0.5)
      try:
        msg = bridge.cv2_to_imgmsg(image)
      except TypeError:print("file - ",f)
      # print(msg)
      
      pub.publish(msg)
      
      if os.getcwd() == '/home/avhi/Desktop/ROS_Yolo/Yolo_imp/Yolo_Output_left':os.remove(f)
      
      time_end = rospy.Time.now()
      duration = time_end - time_begin
      print(duration.to_sec() , "secs")

    # os.chdir("../")
        

  if rospy.is_shutdown():pass

    
if __name__ == '__main__':
  try: 
    talker()
  except rospy.ROSInterruptException: pass
  talker()

  while not rospy.is_shutdown():
    rospy.spin()