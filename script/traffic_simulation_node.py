#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from simulator import TrafficSimulator


def main():
    node = Node('traffic_simulation_node')
    node.get_logger().info("Start traffic simulation node")
    map_file = node.get_parameter("~map_file").value
    sim = TrafficSimulator(map_file)
    rclpy.spin(sim)

if __name__ == '__main__':
    main()
