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

def bag_to_image():
    print("hello")
    FILENAME = 'camera'
    ROOT_DIR = '/home/avhi/Desktop/ROS_Yolo'
    BAGFILE = ROOT_DIR + '/' + FILENAME + '.bag'

    # if __name__ == '__main__':
    bag = rosbag.Bag(BAGFILE)
    # print(type(bag))
    for i in range(2):
        if (i == 0):
            TOPIC = '/multisense_sl/camera/camera_front/left/camera_front/image_raw'
            DESCRIPTION = 'image_raw'
            # print("in if")
        else:
            TOPIC = 'multisense_sl/camera/camera_front/left/camera_front/image_raw'
            DESCRIPTION = 'image_raw'
            # print("in else")

        image_topic = bag.read_messages(TOPIC)

        # im = np.frombuffer(bag.data, dtype=np.uint8).reshape(bag.height, bag.width, -1)
        # print(im)
        for k, b in enumerate(image_topic):
            bridge = CvBridge()
            cv_image = bridge.imgmsg_to_cv2(b.message, b.message.encoding)
            cv_image.astype(np.uint8)
            
        # gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        # print("Hello! mate")
        # print(gray)
        # print(len(gray))

        # file1 = open("Image.txt","a")
        # print(cv_image)
        # print(ROOT_DIR  + DESCRIPTION + str(b.timestamp) + '.png')
        # cv2.imwrite(ROOT_DIR + DESCRIPTION + str(b.timestamp) + '.png', cv_image)
        # cv2.imshow('image window', cv_image)
        # add wait key. window waits until user presses a key
        # cv2.waitKey(0)
        # and finally destroy/close all open windows
        # cv2.destroyAllWindows()
    

            # if (DESCRIPTION == 'depth_'):
            #     print(1)
            #     depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(cv_image, alpha=0.03), cv2.COLORMAP_JET)
            #     cv2.imwrite(ROOT_DIR + '/depth/' + DESCRIPTION + str(b.timestamp) + '.png', cv_image)
            # else:
            #     print(2)
            #     location = ROOT_DIR + '/color/' + DESCRIPTION + str(b.timestamp) + '.png', cv_image
            #     print(location)
            #     cv2.imwrite(ROOT_DIR + '/color/' + DESCRIPTION + str(b.timestamp) + '.png', cv_image)
            # exit(1)    
            # print('saved: ' + DESCRIPTION + str(b.timestamp) + '.png')
    return  cv_image
