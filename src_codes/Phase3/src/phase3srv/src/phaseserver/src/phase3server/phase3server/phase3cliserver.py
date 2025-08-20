import rclpy 
from rclpy.node import Node 
from phase3srv.srv import RosMessage

class Phase3ServiceFlutter(Node):
    def __init__(self):
        super().__init__("phase3_service_flutter")
        self.srv=self.create_service(RosMessage,"Phase3Server",self.handle_message)
        self.get_logger().info("Phase 3 Server Started and Ready")

    def handle_message(self,request,response):
        self.get_logger().info(f"Received Command")
        if request.command=="move to":
            self.get_logger().info(f"Moved to: {request.x}, {request.y}, {request.z}")
            response.success=True
            response.message=f"Command Accepted!"
        elif request.command=="move arm":
            self.get_logger().info(f"Moving Arm: {request.x}, {request.y}, {request.z}, {request.w}")
            response.success=True
            response.message=f"Command Accepted!"
        elif request.command=="ea":
            self.get_logger().info("Emergency Abort Command Received!")
            self.get_logger().info("Shutting Down......")
            response.success=True
            response.message=f"Command Accepted!"
        else: 
            response.success=False
            response.message="Unknown Command"
        return response
    
def main(args=None):
    rclpy.init(args=args)
    node=Phase3ServiceFlutter()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()