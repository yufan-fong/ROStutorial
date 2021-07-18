#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
import sys    
from cv_bridge import CvBridge, CvBridgeError
  
def main(args):
    global bridge, i
    
    # video input from a file
    video_capture = cv2.VideoCapture('/home/yufanana/catkin_ws/src/ros_essentials/src/topic03_perception/video/tennis-ball-video.mp4')
    
    rospy.init_node('tennis_ball_publisher', anonymous=True)
    image_pub = rospy.Publisher("tennis_ball_image",Image, queue_size=10)

    # publish at 30Hz
    rate = rospy.Rate(30)

    while not rospy.is_shutdown():
        ret, cv_frame = video_capture.read()

        # convert cv image to a ros msg
        ros_frame = bridge.cv2_to_imgmsg(cv_frame,encoding = "passthrough")
        
        if ret == False:
            print('ret is False')
            break

        image_pub.publish(ros_frame)
        rospy.loginfo("Published a frame {}".format(i))
        i += 1

        rate.sleep()
    
    video_capture.release()
    cv2.destroyAllWindows()

bridge = CvBridge()
i = 0
if __name__ == '__main__':
    main(sys.argv)