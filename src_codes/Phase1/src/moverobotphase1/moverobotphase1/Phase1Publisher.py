import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Phase1Publisher(Node):
    def __init__(self):
        super().__init__('phase1_publisher')
        self.publisher_=self.create_publisher(
            String,
            'Phase1Topic',
            10
        )
        self.get_logger().info("Publisher Node Started")
    
    def get_user_input(self):
        print("\nAvailable Commands:")
        print("Can Command \033[94mmove to\033[0m or \033[94mmove arm\033[0m with the values or")
        print("Can Just Enter the Number (Only Number) Assigned for the Command or the Command itself (Not Case Sensitive), without values.")
        print("A prompt will follow-up to fetch values, if it's just commands without values.")
        print("\033[95mSelection:\033[0m")
        print("1. Move To")
        print("2. Move Arm")
        print("3. Emergency Abort or EA\n")
        while rclpy.ok():
            msg=String()
            choice=input("\033[96mEnter Option Number or Command:\033[0m ").lower()
            try:
                choice=int(choice)
            except:
                pass
            if isinstance(choice,int):
                match choice:
                    case 1:
                        corrds=input("Enter X, Y, Z (Can use Space or Comma to Separate): ")
                        if len(corrds.split(","))!=3 or corrds[-1]==",":
                            print("\033[93mEnter exact 3 values and don't add , at the end.\033[0m")
                            continue
                        else:
                            msg.data=f"{choice}|{corrds}"
                    case 2:
                        corrds=input("Enter X, Y, Z, W (can use spaces or comma to separate): ")
                        if len(corrds.split(","))!=4 or corrds[-1]==",":
                            print("\033[93mEnter exact 4 values and don't add , at the end.\033[0m")
                            continue
                        else:
                            msg.data=f"{choice}|{corrds}"
                    case 3: 
                        msg.data="0"
                    case _:
                        print("\033[91mInvalid Choice\033[0m")
                        continue
            else:
                if (choice.strip()!="emergency abort" or choice.strip()!="ea") and len(choice.strip())<=8:
                    match choice.strip():
                        case "move to":
                            corrds=input("Enter X, Y, Z (Can use Space or Comma to Separate): ")
                            if len(corrds.split(","))!=3 or corrds[-1]==",":
                                print("\033[93mEnter exact 3 values and don't add , at the end.\033[0m")
                                continue
                            else:
                                msg.data=f"{choice}|{corrds}"
                        case "move arm":
                            corrds=input("Enter X, Y, Z, W (can use spaces or comma to separate): ")
                            if len(corrds.split(","))!=4 or corrds[-1]==",":
                                print("\033[93mEnter exact 4 values and don't add , at the end.\033[0m")
                                continue
                            else:
                                msg.data=f"{choice}|{corrds}"
                        case "emergency abort" | "ea":
                            msg.data="0"
                        case _:
                            print("\033[91mInvalid Choice\033[0m")
                            continue
                else:
                    try:
                        choiceNew=choice[:8] if choice.strip().find("arm")!=-1 else choice[:7]
                        if choiceNew=="move to":
                            corrds=choice[8:13]
                        elif choiceNew=="move arm":
                            corrds=choice[9:17]
                        else:
                            print("\033[91mInvalid Entry\033[0m")
                            continue
                        print(f"Corrds, {corrds}")
                        if (choiceNew=="move arm" and (len(corrds.split(","))!=4 or corrds[-1]==",")) or (choiceNew=="move to" and (len(corrds.split(","))!=3 or corrds[-1]==",")):
                                print("\033[93mEnter exact 4 values and don't add , at the end.\033[0m")
                                continue
                        else:
                         msg.data=f"{choiceNew}|{corrds}"
                    finally:
                        pass
                        # print("\033[91mInvalid Entry\033[0m")
            self.publisher_.publish(msg)
            self.get_logger().info(f"Published Command: {choice}")
            if choice==3 or choice=="emergency abort" or choice=="ea":
                self.get_logger().info("\033[93mEmergency Shutdown Activated, Shutting Down RCLPY\033[0m")
                break
            
try:
    def main(args=None):
        rclpy.init(args=args)
        node=Phase1Publisher()
        node.get_user_input()
        node.destroy_node()
        rclpy.shutdown()
except Exception as e: 
    print("Error: ",e)
