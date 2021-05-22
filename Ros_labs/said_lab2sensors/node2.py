#!/usr/bin/env python3

import rclpy
import csv
from rclpy.node import Node
from example_interfaces.msg import String
from sensor_msgs.msg import Imu
import numpy as np
from geometry_msgs.msg import Quaternion
from math import sin, cos, pi
from sensor_msgs.msg import NavSatFix


class my_node (Node):
    def __init__(self):
        super().__init__("node1")
        self.msg = NavSatFix()
        self.x1 = 0.0
        self.x2 = "s"
        self.x3 = 0.0
        self.x4 = "s"
        self.x5 = 0.0
        self.x6 = 0.0
        self.y1 = 0.0
        self.y2 = 0.0
        self.y3 = 0.0

        self.list_S = []
        self.counterx = 0
        self.counter = 0
        self.obj_pub = self.create_publisher(NavSatFix, "fix", 10)
        self.create_timer(1/5, self.timer_call)
        self.get_logger().info("Node is started")
        self.read_file()

    def timer_call(self):

        # self.read_file()

        latitude_value = str(self.list_S[self.counterx])
        latitude_direction = self.list_S[self.counterx+1]
        longitude_value = str(self.list_S[self.counterx+2])
        longitude_direction = self.list_S[self.counterx+3]
        altitude_value = self.list_S[self.counterx+4]

        latitude = self.convert_latitude(latitude_value, latitude_direction)
        longitude = self.convert_longitude(
            longitude_value, longitude_direction)
        altitude = self.safe_float(altitude_value)

        hdop = float(self.list_S[self.counterx+5])
        lat_std_dev = float(self.list_S[self.counterx+6])
        lon_std_dev = float(self.list_S[self.counterx+7])
        alt_std_dev = float(self.list_S[self.counterx+8])

        self.msg.latitude = latitude
        self.msg.longitude = longitude
        self.msg.altitude = altitude

        self.msg.position_covariance[0] = (hdop * lon_std_dev) ** 2
        self.msg.position_covariance[4] = (hdop * lat_std_dev) ** 2
        self.msg.position_covariance[8] = (2 * hdop * alt_std_dev) ** 2
        self.obj_pub.publish(self.msg)
        self.counterx += 9

    def read_file(self):
        with open('GGA_GST.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                self.x1 = row['Latitude']
                self.x2 = row['Direction_of_latitude']
                self.x3 = row['Longitude']
                self.x4 = row['Direction_of_longitude']
                self.x5 = row['HDOP']
                self.x6 = row['altitude']

                self.y1 = row['Lat_sigma_error']
                self.y2 = row['Long_sigma_error']
                self.y3 = row['Height_sigma_error']

                self.list_S.append(self.x1)
                self.list_S.append(self.x2)
                self.list_S.append(self.x3)
                self.list_S.append(self.x4)
                self.list_S.append(self.x5)
                self.list_S.append(self.x6)

                self.list_S.append(self.y1)
                self.list_S.append(self.y2)
                self.list_S.append(self.y3)
                self.counter += 1
                if self.counter == 6267:
                    break
            # print(self.list_S)

    def convert_latitude(self, field_lat, lat_direction):
        latitude = self.safe_float(
            field_lat[0:2]) + self.safe_float(field_lat[2:]) / 60.0
        if lat_direction == 'S':
            latitude = -latitude
        return latitude

    def convert_longitude(self, field_long, long_direction):
        longitude = self.safe_float(
            field_long[0:2]) + self.safe_float(field_long[2:]) / 60.0
        if long_direction == 'W':
            longitude = -longitude
        return longitude

    def safe_float(self, field):
        try:
            return float(field)
        except ValueError:
            return float('NaN')


def main(args=None):
    rclpy.init(args=args)
    node = my_node()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
