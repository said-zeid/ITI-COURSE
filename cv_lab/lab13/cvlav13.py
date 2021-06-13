#!/usr/bin/env python3

import rclpy
import numpy as np
import math
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from matplotlib import pyplot as plt

import time
#from skimage import img_as_float
#from PIL import Image
bridge = CvBridge()

"""
def show(img):
    if (len(img.shape) == 2):
        display(Image.fromarray(img))
    else:
        display(Image.fromarray(img[:, :, ::-1]))
"""


class my_node (Node):
    def __init__(self):
        super().__init__("sub_node")
        self.create_subscription(Image, "/intel_realsense_d435_depth/image_raw",
                                 self.img_cb, rclpy.qos.qos_profile_sensor_data)

        self.get_logger().info("subscriber is started")
        self.counter = 0
        self.img = 0
        self.img3 = 0
        self.gray = 0
        self.keypoints_1 = []
        self.descriptors_1 = 0
        self.c = 0
        #self.listx = []
        #self.listy = []
        self.list_kp1 = []
        self.list_kp2 = []

    def img_cb(self, message):
        self.counter += 1
        if self.counter == 1:
            orb = cv2.ORB_create()
            self.img = bridge.imgmsg_to_cv2(message, "bgr8")
            self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            self.keypoints_1, self.descriptors_1 = orb.detectAndCompute(
                self.gray, None)
            print(1)

        if self.counter == 4:
            orb = cv2.ORB_create()
            img2 = bridge.imgmsg_to_cv2(message, "bgr8")
            gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            keypoints_2, descriptors_2 = orb.detectAndCompute(img2, None)
            bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
            matches = bf.match(self.descriptors_1, descriptors_2)
            matches = sorted(matches, key=lambda x: x.distance)
            self.img3 = cv2.drawMatches(
                self.gray, self.keypoints_1, gray2, keypoints_2, matches, gray2, flags=2)
            if self.descriptors_1 is not None and descriptors_2 is not None:
                if (len(matches) != 0):

                    self.list_kp1 = [
                        self.keypoints_1[mat.queryIdx].pt for mat in matches]
                    self.list_kp2 = [
                        keypoints_2[mat.trainIdx].pt for mat in matches]
                    # print(len(self.list_kp1))
                    listx = []
                    listxleft1 = []
                    listxleft2 = []
                    listy = []
                    for x in self.list_kp2:
                        listx.append(self.list_kp2[self.c][0] -
                                     self.list_kp1[self.c][0])
                        listy.append(self.list_kp2[self.c][1] -
                                     self.list_kp1[self.c][1])
                        ####################################
                        if self.c > int(len(self.list_kp2)/2):
                            listxleft1.append(self.list_kp1[self.c][0])
                            listxleft2.append(self.list_kp2[self.c][0])
                        ###################################
                        self.c += 1
                    self.c = 0
                    avgx = sum(listx)/len(listx)
                    avgy = sum(listy)/len(listy)
                    ###############################
                    if len(listxleft1) != 0:
                        avgf1 = sum(listxleft1)/len(listxleft1)
                        avgf2 = sum(listxleft2)/len(listxleft2)
                        if avgf2 > avgf1:
                            print("forward")
                            cv2.putText(self.img3, "forward", (0, 35),
                                        cv2.FONT_HERSHEY_SIMPLEX, 1, 255, thickness=2)
                        """    
                        elif avgf2 == avgf1:
                            print("not moving")
                        else:
                            print("backward")
                        """
                    ########################
                    if avgx < 0:
                        x_s = 1
                        x_e = 3
                    else:
                        x_s = 3
                        x_e = 1
                    start_point = (
                        int(self.img3.shape[1]*(x_s/4)), int(self.img3.shape[0]/2))

                    # End coordinate
                    end_point = (int((self.img3.shape[1]*(x_e/4))+avgx),
                                 int((self.img3.shape[0]/2)+avgy))
                    self.img3 = cv2.arrowedLine(
                        self.img3, start_point, end_point, (0, 0, 255), 5)

            print(5)
            self.counter = 0
        cv2.imshow('Output', self.img3)
        cv2.waitKey(1)
        # if k == 27:
        #    cv2.destroyAllWindows()


# if cv2.waitKey(1) & 0xff == 27:
#    cv2.destroyAllWindows()


def main(args=None):
    rclpy.init(args=args)
    node = my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
