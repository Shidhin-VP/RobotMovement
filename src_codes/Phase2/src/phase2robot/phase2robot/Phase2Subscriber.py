import rclpy 
from rclpy.node import Node
from std_msgs.msg import String
import sys

class Phase1Sub(Node):
    def __init__(self):
        super().__init__('phase1_sub')
        self.subscription_=self.create_subscription(
            String,
            'Phase2Topic',
            self.listner_callback,
            10
        )
        self.get_logger().info("Subscriber Node Started")

    def outputCommand(self,value,position):
        command={
            "1":f"Moving to {position}",
            "move to": f"Moving to {position}",
            "2":f"Moving Arm to {position}",
            "move arm": f"Moving Arm to {position}",
        }
        print(f"\033[92m{command.get(value)}\033[0m")

    def listner_callback(self,msg):
        self.get_logger().info(f"\033[1;96mCommand Received.\033[0m")

        if msg.data!="0":
            choice,corrd=msg.data.split("|")
            self.outputCommand(choice,corrd)
        else:
            self.get_logger().info("\033[91mCommand Received, Emergency Abort.\033[0m")
            self.get_logger().info("\033[93mStutting Down....\033[0m")
            self.destroy_node()
            rclpy.shutdown()
            sys.exit(0)
            raise KeyboardInterrupt()


try: 
    def main(args=None):
        rclpy.init(args=args)
        node=Phase1Sub()
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()
except Exception as e:
    print("Error: ",e)