#! /usr/bin/env python
from tf import TransformBroadcaster
try:
    from tf import TransformBroadcaster
except ImportError:
    import sys
    ros_path = '/opt/ros/kinetic/lib/python2.7/dist-packages'
    sys.path.remove(ros_path)
    from tf import TransformBroadcaster
    sys.path.append(ros_path)
import rospy
from rospy import Time 

def main():
    rospy.init_node('my_broadcaster')
    
    b = TransformBroadcaster()
    
    translation = (0.0, 0.0, 0.0)
    rotation = (0.0, 0.0, 0.0, 1.0)
    rate = rospy.Rate(5)  # 5hz
    
    x, y = 0.0, 0.0
    
    while not rospy.is_shutdown():
        if x >= 2:
            x, y = 0.0, 0.0 
        
        x += 0.1
        y += 0.1
        
        translation = (x, y, 0.0)
        
        
        b.sendTransform(translation, rotation, Time.now(), 'ignite_robot', '/world')
        rate.sleep()
    


if __name__ == '__main__':
    main()