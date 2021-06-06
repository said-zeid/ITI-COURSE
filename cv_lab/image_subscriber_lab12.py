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
bridge = CvBridge()


class my_node (Node):
    def __init__(self):
        super().__init__("sub_node")
        self.create_subscription(Image, "/intel_realsense_d435_depth/image_raw",
                                 self.img_cb, rclpy.qos.qos_profile_sensor_data)

        self.get_logger().info("subscriber is started")

    def img_cb(self, message):

        img = bridge.imgmsg_to_cv2(message, "bgr8")
        black_img = np.zeros((240, 320, 1), np.uint8)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        first_shot = time.time()
        corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
        corners = np.int0(corners)
        time_calculated = time.time() - first_shot

        print(time_calculated)

        for i in corners:
            x, y = i.ravel()
            cv2.circle(black_img, (x, y), 3, 255, -1)

            cv2.imshow("cv2_img", img)
            cv2.imshow("blank", black_img)

        if cv2.waitKey(1) & 0xff == 27:
            cv2.destroyAllWindows()


def main(args=None):
    rclpy.init(args=args)
    node = my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
