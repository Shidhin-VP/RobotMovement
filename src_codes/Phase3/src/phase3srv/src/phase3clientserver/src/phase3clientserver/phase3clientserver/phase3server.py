import rclpy
from rclpy.node import Node
from phase3srv.srv import PhaseMessageType

class Phase3Server(Node):
    def __init__(self):
        super().__init__("phase3_server")
        self.srv=self.create_service(PhaseMessageType,"Phase3ClientService",self.handle_incomming)
        self.get_logger().info("Phase 3 Server Started and Ready")

    def handle_incomming(self,request,response):
        self.get_logger().info(f"\033[96Command Received\033[0m")
        if request.command=="move to":
            self.get_logger().info(f"\033[92mMoving to: {request.x}, {request.y}, {request.z}\033[0m")
            response.success=True
            response.message=f"Command Received and Robot Moved to the Position"
        elif request.command=="move arm":
            self.get_logger().info(f"\033[92mMoving Arm to: {request.x}, {request.y}, {request.z}, {request.w}\033[0m")
            response.success=True
            response.message=f"Command Received and Robot Moved Arm to the Position"
        elif request.command=="ea":
            self.get_logger().info("\033[91mEmergency Abort Initiated\033[0m")
            self.get_logger().info("\033[93mShutting Down.....\033[0m")
            response.success=True
            response.message="Shutdown Completed"
            self.destroy_node()
            rclpy.shutdown()
        else:
            response.success=False
            response.message="Unknown Command"

        return response
        
def main(args=None):
    rclpy.init(args=args)
    node=Phase3Server()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()