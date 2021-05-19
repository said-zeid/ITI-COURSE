#!/usr/bin/env python3

import rclpy
import csv
from rclpy.node import Node
from example_interfaces.msg import String
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from turtlesim.msg import Pose


class my_node (Node):
    def __init__(self):
        super().__init__("node1")
        self.x = 0.0
        self.y = 0.0
        self.x0 = 0.0
        self.y0 = 0.0
        self.obj_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.client2 = self.create_client(Empty, "/reset")
        self.create_subscription(Pose, "/turtle1/pose", self.callback2, 10)

        self.create_timer(1/1, self.timer_call)
        self.get_logger().info("Node is started")
        self.counter = 0
        self.c = 0
        self.list_S = []

    def read_file(self):
        with open('turtle_commands.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter='\t')
            for row in reader:
                self.x = row['linear x ']
                self.y = row['angular z']
                self.list_S.append(float(self.x))
                self.list_S.append(float(self.y))
                self.counter += 1
                if self.counter == 13:
                    break

    def timer_call(self):
        msg = Twist()
        self.read_file()
        msg.linear.x = self.list_S[self.c]
        msg.angular.z = self.list_S[(self.c)+1]
        print(msg.linear.x)
        print(msg.angular.z)

        self.obj_pub.publish(msg)
        self.c += 2

    def callback2(self, msg):
        self.x0 = msg.x
        self.y0 = msg.y
        print(msg.x)
        print(msg.y)

        if msg.x > 8.0:
            while self.client2.wait_for_service(0.25) == False:
                self.get_logger().warn("Wait for server node")
            request2 = Empty.Request()
            future_obj1 = self.client2.call_async(request2)
            future_obj1.add_done_callback(self.future_call_1)

        elif msg.x < 2.0:
            while self.client2.wait_for_service(0.25) == False:
                self.get_logger().warn("Wait for server node")
            request2 = Empty.Request()
            future_obj1 = self.client2.call_async(request2)
            future_obj1.add_done_callback(self.future_call_1)
        elif msg.y > 8.0:
            while self.client2.wait_for_service(0.25) == False:
                self.get_logger().warn("Wait for server node")
            request2 = Empty.Request()
            future_obj1 = self.client2.call_async(request2)
            future_obj1.add_done_callback(self.future_call_1)

        elif msg.y < 2.0:
            while self.client2.wait_for_service(0.25) == False:
                self.get_logger().warn("Wait for server node")
            request2 = Empty.Request()
            future_obj1 = self.client2.call_async(request2)
            future_obj1.add_done_callback(self.future_call_1)

    def future_call_1(self, msg):
        pass


def main(args=None):
    rclpy.init(args=args)
    node = my_node()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
