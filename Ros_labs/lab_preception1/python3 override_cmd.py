#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from turtlesim.msg import Pose
import math
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class saidclass2(Node):

    def __init__(self):
        super().__init__("state_publisher")
        self.obj_pos = self.create_subscription(
            Twist, "key_cmd_vel", self.call_sub, 10)
        self.obj1_pos = self.create_subscription(
            LaserScan, "/scan", self.call_su2, 10)
        self.pos_pub = self.create_publisher(Twist, "/cmd_vel", 10)
        self.create_timer(1/10, self.timer_call)
        self.lx = 0.0
        self.ly = 0.0
        self.lz = 0.0
        self.ax = 0.0
        self.ay = 0.0
        self.az = 0.0
        self.flag = 0
        self.msg = Twist()

    def timer_call(self):

        if self.flag == 0:
            self.msg.linear.x = self.lx
            self.msg.angular.x = self.ax
            self.msg.angular.y = self.ay
            self.msg.angular.z = self.az

        else:
            self.msg.linear.x = 0.0
            self.msg.angular.x = self.ax
            self.msg.angular.y = self.ay
            self.msg.angular.z = self.az

        self.pos_pub.publish(self.msg)

    def call_sub(self, msg):
        self.lx = msg.linear.x
        self.ly = msg.linear.y
        self.lz = msg.linear.z
        self.ax = msg.angular.x
        self.ay = msg.angular.y
        self.az = msg.angular.z

    def call_su2(self, message):
        laser_data = message.ranges
        laser_data1 = laser_data[0:44:1]
        laser_data2 = laser_data[315:359:1]
        max_value1 = max(laser_data1)
        max_value2 = max(laser_data2)
        if max_value1 > max_value2:
            maximum = max_value1
        else:
            maximum = max_value2
        if maximum < 1:
            self.flag = 1
        else:
            self.flag = 0


def main(args=None):
    rclpy.init(args=args)
    node = saidclass2()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
