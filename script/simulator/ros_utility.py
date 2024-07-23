import rclpy
from rclpy.node import Node

def get_ros_param(param_name: str, default):
    '''
    Read a parameter from the ROS parameter server. If the parameter does not exist, return the default value.
    Args:
        param_name: string, name of the parameter
        default: default value
    Return:
        value of the parameter
    '''
    if Node.has_parameter(param_name):
        return Node.get_parameter(param_name).value
    else:
        # try seach parameter
        if param_name[0] == '~':
            search_param_name = Node.get_parameter(param_name[1:]).value
        else:
            search_param_name = Node.get_parameter(param_name).value

        if search_param_name is not None:
            Node.get_logger().info('Parameter %s not found, search found %s, using it', param_name, search_param_name)
            return Node.get_parameter(search_param_name).value
        else:
            Node.get_logger().warn("Parameter '%s' not found, using default: %s", param_name, default)
            return default

