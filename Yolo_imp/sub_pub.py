from numba import jit, cuda
from posix import listdir
import rospy
from sensor_msgs.msg import Image
from sensor_msgs.msg import PointCloud2 as pc2
from sensor_msgs.msg import LaserScan
import sensor_msgs.point_cloud2
import pcl as pc
import matplotlib.pyplot as plt
try:
    import cv2
except ImportError:
    import sys
    ros_path = '/opt/ros/kinetic/lib/python2.7/dist-packages'
    sys.path.remove(ros_path)
    import cv2
    sys.path.append(ros_path)
from cv_bridge import CvBridge
# import multiprocessing
# import threading


import yolo as Yolo

rospy.init_node('Yolo', anonymous = False)
pub_left = rospy.Publisher('Yolo_Sub_Pub_Left', Image, queue_size=-1)
pub_right = rospy.Publisher('Yolo_Sub_Pub_Right', Image, queue_size=-1)
bridge = CvBridge()  

# @jit
def image_processing_left(cv_img):
           
    yolo_output = Yolo.Yolo_imp(cv_img)
    print("for left")
    left_output = bridge.cv2_to_imgmsg(yolo_output)
    pub_left.publish(left_output)
    
# @jit
def image_processing_right(cv_img):
    
    yolo_output = Yolo.Yolo_imp(cv_img)
    print("for right")
    right_output = bridge.cv2_to_imgmsg(yolo_output)
    pub_right.publish(right_output)


def image_callback_left(msg: Image):
    cv_img =  bridge.imgmsg_to_cv2(msg)
    image_processing_left(cv_img)
    # left = threading.Thread(target=image_processing_left(cv_img))
    # left.start()
    # left.join()

def image_callback_right(msg: Image):
    cv_img =  bridge.imgmsg_to_cv2(msg)
    image_processing_right(cv_img)
    # right = threading.Thread(target=image_processing_right(cv_img))
    # right.start()
    # right.join()
    
def point_cloud_callback(msg:pc2): 
    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')
    # rospy.loginfo(msg)
    # print("here")
    
    # print(msg.fields)
    # print(msg._full_text)
    # n = msg.fields
    # for i in n:print(i,type(i))
    # araay = i.
    
    # data = []
    # data_set = []
    # for i in msg.fields:
    #     data.append(i)
    #     for j in data:
    #         print(type(j))
    #         data_set.append(j)
    #         print('-------------------------------------------')
    points_list = []
    for point in sensor_msgs.point_cloud2.read_points(msg, skip_nans=True):
            # print(point)        
            pt_x = point[0]
            pt_y = point[1]
            pt_z = point[2]   
            # print([pt_x,pt_y,pt_z])
            pt_i = point
            # print(pt_i)
            points_list.append([point[0],point[1],point[2],point[3]])
            # ax.plot_surface(point[0],point[1],point[2])
            # ax.show()
    pcl_data = pc.PointCloud_PointXYZRGB()
    pcl_data.from_list(points_list)
    
def laserscan_callback(msg:LaserScan):
    rospy.loginfo(msg)
    
    pass
            
 

def main():

    # rospy.Subscriber("/multisense_sl/camera/camera_front/left/camera_front/image_raw", Image, image_callback_left, queue_size=-1)
    # rospy.Subscriber("/multisense_sl/camera/camera_front/left/camera_front/image_raw", Image, image_callback_right, queue_size=-1)
    rospy.Subscriber("/velodyne_points",pc2,point_cloud_callback,queue_size=1)
    rospy.Subscriber("/pcl_laserscan", LaserScan, laserscan_callback, queue_size=10)
    while not rospy.is_shutdown():
        rospy.spin()   


if __name__ == "__main__":
    main()