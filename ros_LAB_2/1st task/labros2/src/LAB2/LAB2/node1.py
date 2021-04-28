#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class my_node (Node):
    def __init__(self):
        super().__init__("node1")

        self.create_timer(1/1, self.timer_call)
        self.obj_pub = self.create_publisher(String, "number", 10)

        self.get_logger().info("Node is started")

    def timer_call(self):
        msg = String()
        msg.data = "3"
        self.get_logger().info(msg.data)
        self.obj_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = my_node()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
