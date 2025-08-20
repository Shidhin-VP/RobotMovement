import rclpy
from rclpy.node import Node
from phase3srv.srv import RosMessage

class Phase3ServerFlutter(Node):
    def __init__(self):
        super().__init__('phase3_server_flutter')
        self.srv=self.create_service(RosMessage,'phase3server',self.handle_message)
        self.get_logger().info("Phase 3 Service Started..")

    def handle_message(self,request,response):
        self.get_logger().info("Command Received")

        if request.command=="move to":
            self.get_logger().info(f"Moved to Position: {request.x}, {request.y}, {request.z}")
            response.success=True
            response.message=f"Command Accepted!"
        elif request.command=="move arm":
            self.get_logger().info(f"Moved Arm: {request.x}, {request.y}, {request.z}, {request.w}")
            response.success=True
            response.message=f"Command Accepted!"
        elif request.command=="ea":
            self.get_logger().info("Got Emergency Input")
            self.get_logger().info("Shutting Down")
            response.success=True
            response.message=f"Command Accepted!"
        else:
            response.success=False
            response.message="Unknown Command"
        return response
    

def main(args=None):
    rclpy.init(args=args)
    node=Phase3ServerFlutter()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()