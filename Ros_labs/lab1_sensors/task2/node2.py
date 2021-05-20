#!/usr/bin/env python3

import rclpy
import csv
from rclpy.node import Node
from example_interfaces.msg import String
from sensor_msgs.msg import Imu
import numpy as np
from geometry_msgs.msg import Quaternion
from math import sin, cos, pi


class my_node (Node):
    def __init__(self):
        super().__init__("node1")
        self.msg = Imu()
        self.msg.header.frame_id = "zed2_imu_link"
        self.list_S = []
        self.counter = 0
        self.obj_pub = self.create_publisher(Imu, "/zed2_imu", 10)
        self.create_timer(1/30, self.timer_call)
        self.get_logger().info("Node is started")

    def timer_call(self):

        self.read_file()

    def read_file(self):
        with open('imu_data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for i in range(self.counter):
                next(reader)
            row = next(reader)
            self.list_S = row
            self.msg.linear_acceleration.x = float(self.list_S[0])*9.80665
            self.msg.linear_acceleration.y = float(self.list_S[1])*9.80665
            self.msg.linear_acceleration.z = float(self.list_S[2])*9.80665
            self.msg.angular_velocity.x = float(self.list_S[3])
            self.msg.angular_velocity.y = float(self.list_S[4])
            self.msg.angular_velocity.z = float(self.list_S[5])
            self.msg.orientation.z = float(
                self.quaternion_from_euler(0.0, 0.0, float(self.list_S[6])))

            if float(self.list_S[5]) < 0.3:
                # small variance to be very acurate
                self.msg.angular_velocity_covariance[8] = 0.0001
                self.msg.orientation_covariance[8] = 0.0001
            else:
                # large variance to be less acurate
                self.msg.angular_velocity_covariance[8] = 0.1
                self.msg.orientation_covariance[8] = 0.1

            self.obj_pub.publish(self.msg)

            self.counter += 1
            if self.counter == 347:
                self.counter = 0
            # print(self.counter)

    def quaternion_from_euler(self, roll, pitch, yaw):
        qx = sin(roll/2) * cos(pitch/2) * cos(yaw/2) - \
            cos(roll/2) * sin(pitch/2) * sin(yaw/2)
        qy = cos(roll/2) * sin(pitch/2) * cos(yaw/2) + \
            sin(roll/2) * cos(pitch/2) * sin(yaw/2)
        qw = cos(roll/2) * cos(pitch/2) * cos(yaw/2) + \
            sin(roll/2) * sin(pitch/2) * sin(yaw/2)
        qz = cos(roll/2) * cos(pitch/2) * sin(yaw/2) - \
            sin(roll/2) * sin(pitch/2) * cos(yaw/2)
        return qz


def main(args=None):
    rclpy.init(args=args)
    node = my_node()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
