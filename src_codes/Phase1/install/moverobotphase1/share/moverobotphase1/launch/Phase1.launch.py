from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="moveRobotPhase1",
                executable="pub1_node",
                name="pub1_node"
            ),
            Node(
                package="moveRobotPhase1",
                executable="sub1_node",
                name="sub1_node"
            )
        ]
    )