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
from nav_msgs.msg import Odometry


class my_node (Node):
    def __init__(self):
        super().__init__("node1")
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.counter = 0
        self.c = 0
        self.list_S = []
        self.create_subscription(Odometry, "/odom", self.callback2, 10)
        self.get_logger().info("Node is started")
        self.read_file()

    def callback2(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        yaw = msg.pose.pose.orientation.z
        z = (self.euler_from_quaternion(0.0, 0.0, yaw, 0.0))*180/pi
        sx = self.list_S[self.c]
        sy = self.list_S[self.c+1]
        sz = self.list_S[self.c+2]
        if x <= sx+0.5 and x >= sx-0.5 and y <= sy+0.5 and sy-0.5 and z <= sz+5 and z >= sz-5:
            print("position is reached")
            if self.c < 9:
                self.c += 3
        else:
            print("BL7")

        if self.c == 9:
            print('i excuted all the positions and the last one is ' +
                  str(sx)+str(sy)+str(sz))
           # self.c = 0

    def read_file(self):
        with open('odom_data.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                self.x = row['pose (x) m']
                self.y = row['pose (y) m']
                self.z = row['yaw (degree)']
                self.list_S.append(float(self.x))
                self.list_S.append(float(self.y))
                self.list_S.append(float(self.z))
                self.counter += 1
                if self.counter == 4:
                    break
        print(self.list_S)

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
