#! /usr/bin/env python3

# Here we create a subscriber node which listens the msg send by publishher

import rclpy
from rclpy.node import Node

from std_msgs.msg import String



class MinimalPySubscriber(Node):
    """
    MinimalPySubscriber Node
    """
    def __init__(self):
        """
        Custom class for subscribing the node
        """
        # Initialize the node with a name
        super().__init__('minimal_py_subscriber')

        # Create a subscriber
        self.subscriber_1 = self.create_subscription(
            String,
            'py_example_topic',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        """
        Calls this function everytime a new message is published on the topic
        """
        # Log a message indicating that the message has been published
        self.get_logger().info(f'I heard: {msg.data}')

def main(args=None):
    """
    Main function to start the ROS2 Node 
    """
    # Initialize the Ros2 Communication
    rclpy.init(args=args)

    # Create an instance of the minimal py subscriber class
    minimal_py_subscriber = MinimalPySubscriber()

    # Keep the node running and processing events
    rclpy.spin(minimal_py_subscriber)

    # Desptroy the node explicitly
    minimal_py_subscriber.destroy_node()

    # Shutdown ros2 communication
    rclpy.shutdown()

if __name__ == "__main__":
    main()


