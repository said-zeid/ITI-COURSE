#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.srv import SetBool


class my_node2 (Node):
    def __init__(self):
        super().__init__("node2")
        self.create_subscription(String, "number", self.callback2, 10)
        self.obj_sub = self.create_publisher(String, "number_counter", 10)

        self.create_service(SetBool, "First_server", self.srv_call)
        self.massage = String()
        self.counter = 0
        self.f = 0
        self.activated = False

        self.get_logger().info("subscriber is started")

    def srv_call(self, rq, rsp):
        self.activated = rq.data
        self.counter = 0
        self.get_logger().info(str(self.counter))
        #rsp.success = True
        """
        if True:  # self.activated:
            self.counter = 0
            rsp.data = rq.data
            print(rsp.data)
        else:
            rsp.data = rq.data
        """
        return rsp

    def callback2(self, msg):
        self.massage.data = msg.data
        self.f += 1
        if self.f == 1:
            self.create_timer(1/1, self.timer2_call)
        else:
            x = 0
        # self.get_logger().info(msg.data)

    def timer2_call(self):
        self.counter += int(self.massage.data)
        self.get_logger().info(str(self.counter))
        new_msg = String()
        new_msg.data = str(self.counter)
        self.obj_sub.publish(new_msg)


def main(args=None):
    rclpy.init(args=args)
    node2 = my_node2()
    rclpy.spin(node2)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
