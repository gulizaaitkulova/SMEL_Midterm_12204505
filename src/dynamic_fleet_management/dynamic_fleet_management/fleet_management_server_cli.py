import time


import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from fleet_action_interfaces.action import Fleet


class FleetActionServer(Node):

    def __init__(self):
        super().__init__('fleet_management_server_cli')
        self._action_server = ActionServer(
            self,
            Fleet,
            'fibonacci',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')


        feedback_msg = Fleet.Feedback()

        feedback_msg.partial_sequence = [0, 1]


        for i in range(1, goal_handle.request.order):

            feedback_msg.partial_sequence.append(

                feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1])

            self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))

            goal_handle.publish_feedback(feedback_msg)

            time.sleep(1)


        goal_handle.succeed()

        result = Fleet.Result()

        result.sequence = feedback_msg.partial_sequence

        return result


def main(args=None):
    rclpy.init(args=args)

    fleet_management_server_cli = FleetActionServer()

    rclpy.spin(fleet_management_server_cli)


if __name__ == '__main__':
    main()
