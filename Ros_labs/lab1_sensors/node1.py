#!/usr/bin/env python3

import rclpy
import csv
from rclpy.node import Node
from example_interfaces.msg import String
from sensor_msgs.msg import Imu
import numpy as np
from geometry_msgs.msg import Quaternion
from math import sin, cos, pi
import math


class my_node (Node):
    def __init__(self):
        super().__init__("node1")
        self.x = 0.0
        self.create_subscription(Imu, "/imu", self.callback2, 10)
        self.get_logger().info("Node is started")

    def callback2(self, msg):
        x = self.euler_from_quaternion(
            msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w)
        xdeg = x*180/pi

        if xdeg < 2 and xdeg > -2:
            print("The robot is nearly heading north .. Heading is : " +
                  str(xdeg) + " degrees")
        else:
            print("out of the limit")

        if abs(msg.linear_acceleration.x) > 0.3:
            print("Warning !! .. linear acceleration x exceeded the limit . Current acceleration is  : " +
                  str(msg.linear_acceleration.x) + " m/s^2")

        if abs(msg.angular_velocity.z) > 0.3:
            print("Warning !! .. angular velocity z exceeded the limit . Current Angular velocity is  " +
                  str(msg.angular_velocity.z) + " rad/sec")

    def euler_from_quaternion(self, x0, y0, z0, w0):
        x = x0
        y = y0
        z = z0
        w = w0

        sinr_cosp = 2 * (w * x + y * z)
        cosr_cosp = 1 - 2 * (x * x + y * y)
        roll = np.arctan2(sinr_cosp, cosr_cosp)

        sinp = 2 * (w * y - z * x)
        pitch = np.arcsin(sinp)

        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y * y + z * z)
        yaw = np.arctan2(siny_cosp, cosy_cosp)

        return yaw


def main(args=None):
    rclpy.init(args=args)
    node = my_node()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
