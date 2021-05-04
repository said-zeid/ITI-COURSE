#!/usr/bin/env python3

from example_interfaces.srv import SetBool
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from saidmsg.msg import New
from saidmsg.srv import Firstone


class my_node2 (Node):
    def __init__(self):
        super().__init__("node2")
        self.create_subscription(New, "number", self.callback2, 10)
        self.obj_sub = self.create_publisher(New, "number_counter", 10)

        self.create_service(Firstone, "First_server", self.srv_call)
        self.massage = New()
        self.counter = 0
        self.f = 0
        self.activated = False

        self.get_logger().info("subscriber is started")

    def srv_call(self, rq, rsp):
        req_a = rq.f
        rsp.avg = req_a
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
        self.massage.number = msg.number
        self.f += 1
        if self.f == 1:
            self.create_timer(1/1, self.timer2_call)
        else:
            x = 0
        # self.get_logger().info(msg.data)

    def timer2_call(self):
        self.counter += self.massage.number
        self.get_logger().info(str(self.counter))
        new_msg = New()
        new_msg.number = self.counter
        self.obj_sub.publish(new_msg)


def main(args=None):
    rclpy.init(args=args)
    node2 = my_node2()
    rclpy.spin(node2)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
