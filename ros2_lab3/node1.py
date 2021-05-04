#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from saidmsg.msg import New


class my_node (Node):
    def __init__(self):
        super().__init__("node1")
        self.obj_pub = self.create_publisher(New, "number", 10)
        self.create_timer(1/1, self.timer_call)
        self.get_logger().info("Node is started")

    def timer_call(self):
        msg = New()
        msg.massage = "said is publishing "
        msg.number = 5
        self.get_logger().info(msg.massage + str(msg.number))
        self.obj_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = my_node()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
