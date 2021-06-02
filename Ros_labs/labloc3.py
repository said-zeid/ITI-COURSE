#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from turtlesim.msg import Pose
import math
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose


class saidclass2(Node):

    def __init__(self):
        super().__init__("state_publisher")
        self.obj_pos = self.create_subscription(
            Path, "/plan", self.call_sub, 10)
        self.curve = 0.0
        self.x1 = 0.0
        self.y1 = 0.0
        self.x2 = 0.0
        self.y2 = 0.0
        self.x3 = 0.0
        self.y3 = 0.0

    def call_sub(self, msg):
        if len(msg.poses) <= 20:
            print("The path arr is short")
        else:
            self.x1 = msg.poses[2].pose.position.x
            self.y1 = msg.poses[2].pose.position.y
            self.x2 = msg.poses[10].pose.position.x
            self.y2 = msg.poses[10].pose.position.y
            self.x3 = msg.poses[20].pose.position.x
            self.y3 = msg.poses[20].pose.position.y
            self.curve = self.menger_curvature(self.x1, self.y1, self.x2,
                                               self.y2, self.x3, self.y3)
            if self.curve > 0.3:
                print("The robot is turning with a curvature ")
            else:
                print("this is a straight line")
            print(self.curve)
            # print(self.x1)
            #self.get_logger().info(str(msg.x) + "," + str(msg.y))

    def menger_curvature(self, point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y):
        triangle_area = 0.5 * abs((point_1_x*point_2_y) + (point_2_x*point_3_y) + (point_3_x*point_1_y) - (
            point_2_x*point_1_y) - (point_3_x*point_2_y) - (point_1_x*point_3_y))  # Shoelace formula

        curvature = (4*triangle_area) / (math.sqrt(pow(point_1_x - point_2_x, 2)+pow(point_1_y - point_2_y, 2)) * math.sqrt(pow(point_2_x - point_3_x,
                                                                                                                                2)+pow(point_2_y - point_3_y, 2)) * math.sqrt(pow(point_3_x - point_1_x, 2)+pow(point_3_y - point_1_y, 2)))  # Menger curvature
        return curvature


def main(args=None):
    rclpy.init(args=args)
    node = saidclass2()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
