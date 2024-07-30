#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from simulator import Simulator


def main():
    node = Node("simulation_node")
    rclpy.init(anonymous=True)
    node.get_logger().info("Start simulation node")

    sim = Simulator()
    rclpy.spin(sim)

if __name__ == '__main__':
    main()
