#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool


class my_server(Node):
    def __init__(self):
        super().__init__("node3")
        self.client = self.create_client(SetBool, "First_server")
        self.request = SetBool.Request()
        self.service_client()

    def service_client(self):
        #client = self.create_client(SetBool, "First_server")
        while self.client.wait_for_service(0.25) == False:
            self.get_logger().warn("wating for server")

        self.get_logger().info("client_request_sent")
        self.request.data = True
        futur_obj = self.client.call_async(self.request)
        futur_obj.add_done_callback(self.future_call)

    def future_call(self, future_msg):
        print("future msg")
        # self.get_logger().info(str(future_msg.result().data))


def main(args=None):
    rclpy.init(args=args)
    node3 = my_server()
    # node3.service_client()
    rclpy.spin(node3)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
