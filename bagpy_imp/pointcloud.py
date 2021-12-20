try:
    import rosbag
except ImportError or ModuleNotFoundError :
    import sys
    ros_path = '/opt/ros/kinetic/lib/python2.7/dist-packages'
    sys.path.remove(ros_path)
    import rosbag 
    sys.path.append(ros_path)

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
from bagpy import bagreader

b = bagreader('pointcloud.bag')
print(b.topic_table)