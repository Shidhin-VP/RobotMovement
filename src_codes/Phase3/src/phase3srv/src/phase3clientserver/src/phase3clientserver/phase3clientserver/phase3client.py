import rclpy
from rclpy.node import Node
from phase3srv.srv import PhaseMessageType

class Phase3Client(Node):
    def __init__(self):
        super().__init__("phase3_client")
        self.cli=self.create_client(PhaseMessageType,"Phase3ClientService")
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for Service.....")
        self.req=PhaseMessageType.Request()

    def send_command(self,command,x=0.0,y=0.0,z=0.0,w=0.0):
        self.req.command=command
        self.req.x=x
        self.req.y=y
        self.req.z=z
        self.req.w=w
        waitResponse=self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self,waitResponse)
        if waitResponse.result() is not None:
            self.get_logger().info(f"\033[95mResponse Status:\033[0m \033[92m{waitResponse.result().success}\033[0m, \033[95mResponse Message:\033[0m \033[92m{waitResponse.result().message}\033[0m")
        else:
            self.get_logger().error("Service Call Failed.")
    
    def get_numeric(self,x):
        x=x.strip()
        if isinstance(x,(int,float)):
            return True
        try:
            float(x)
            return True
        except (ValueError,TypeError):
            return False

    def get_user_input(self):
        print("\nAvailable Commands:")
        print("Can Command be: \033[94mmove to\033[0m or \033[94mmove arm\033[0m with the values or")
        print("Can Just Enter the Number \033[93m(Only Number)\033[0m Assigned for the Command or the Command itself \033[93m(Not Case Sensitive)\033[0m, without values.")
        print("A prompt will follow-up to fetch values, if it's just commands without values.")
        print("\033[95mSelection:\033[0m")
        print("\033[93m1\033[0m. Move To")
        print("\033[93m2\033[0m. Move Arm")
        print("\033[93m3\033[0m. Emergency Abort or EA\n")
        while rclpy.ok():
            command=input("\033[96mEnter Your Command:\033[0m ").lower().strip()
            try:
                try:
                    command=int(command)
                except:
                    pass
                if(isinstance(command,int)):
                    match command:
                        case 1:
                            coord=input("\033[36mEnter X, Y, Z (Can use Comma Without Spaces to Separate Values):\033[0m ")
                            coord=list(filter(self.get_numeric,coord.strip().split("," or " ")))
                            if(len(coord)<3):
                                print("\033[93mTry entering exactly 3 values for coordinates\033[0m")
                                continue
                            else:
                                sendCommand="move to"
                                x=float(coord[0])
                                y=float(coord[1])
                                z=float(coord[2])
                                self.send_command(sendCommand,x,y,z)
                        case 2:
                            coord=input("\033[36mEnter X, Y, Z, W (Can use Comma Without Spaces to Separate Values):\033[0m ")
                            coord=list(filter(self.get_numeric,coord.strip().split("," or " ")))
                            if(len(coord)<4):
                                print("\033[93mTry entering exactly 4 values for coordinates\033[0m")
                            else: 
                                sendCommand="move arm"
                                x=float(coord[0])
                                y=float(coord[1])
                                z=float(coord[2])
                                w=float(coord[3])
                                self.send_command(sendCommand,x,y,z,w)
                        case _:
                            print("\033[93mEnter the Correct Input\033[0m")
                else:
                    if(command not in ["ea", "emergency abort"] and len(command.strip().split())<=2):
                        match command.strip():
                            case "move to":
                                coord=input("\033[36mEnter X, Y, Z (Can use Comma Without Spaces to Separate Values):\033[0m ")
                                coord=list(filter(self.get_numeric,coord.strip().split("," or " ")))
                                if(len(coord)<3):
                                    print("\033[93mTry entering exactly 3 values for coordinates\033[0m")
                                    continue
                                else:
                                    sendCommand="move to"
                                    x=float(coord[0])
                                    y=float(coord[1])
                                    z=float(coord[2])
                                    self.send_command(sendCommand,x,y,z)
                            case "move arm":
                                coord=input("\033[36mEnter X, Y, Z, W (Can use Comma Without Spaces to Separate Values):\033[0m ")
                                coord=list(filter(self.get_numeric,coord.strip().split("," or " ")))
                                if(len(coord)<4):
                                    print("\033[93mTry entering exactly 4 values for coordinates\033[0m")
                                else: 
                                    sendCommand="move arm"
                                    x=float(coord[0])
                                    y=float(coord[1])
                                    z=float(coord[2])
                                    w=float(coord[3])
                                    self.send_command(sendCommand,x,y,z,w)
                            case _:
                                print("\033[93mEnter the Correct Input\033[0m")
                    elif(command not in ["ea", "emergency abort"] and len(command.strip().split())>2):
                        splitter=command.strip().split()
                        if(splitter[1]=="to"):
                            toTarget=1
                            toSaver=[]
                            for i in splitter[2:]:
                                if(toTarget==3):
                                    sendCommand="move to"
                                    x=toSaver[0]
                                    y=toSaver[1]
                                    z=toSaver[2]
                                    self.send_command(sendCommand,x,y,z)
                                    break
                                content=i.strip().split(',' or " ")
                                if content[-1]=='':
                                    del content[-1]
                                if(len(content)==3 and toTarget<2):
                                    try:
                                        sendCommand="move to"
                                        x=float(content[0])
                                        y=float(content[1])
                                        z=float(content[2])
                                        self.send_command(sendCommand,x,y,z)
                                        break
                                    except:
                                        print("\033[93mEnter Correct Format for the Coordinates\033[0m")
                                else:
                                    for i in content:
                                        try:
                                            toSaver.append(float(i))
                                            toTarget+=1
                                        except Exception as e:
                                            print(f"\033[91mError: {e}\033[0m")
                                            break
                        elif(splitter[1]=="arm"):
                            armTarget=1
                            armSaver=[]
                            for i in splitter[2:]:
                                if(armTarget==4):
                                    sendCommand="move arm"
                                    x=armSaver[0]
                                    y=armSaver[1]
                                    z=armSaver[2]
                                    w=armSaver[3]
                                    self.send_command(sendCommand,x,y,z,w)
                                    break
                                content=i.strip().split("," or " ")
                                if content[-1]=='':
                                    del content[-1]
                                if(len(content)==4 and armTarget<2):
                                    try:
                                        sendCommand="move arm"
                                        x=float(content[0])
                                        y=float(content[1])
                                        z=float(content[2])
                                        w=float(content[3])
                                        self.send_command(sendCommand,x,y,z,w)
                                        break
                                    except Exception as e:
                                        print(f"\033[91mError: {e}\033[0m")
                                        break
                                else:
                                    for i in content:
                                        try:
                                            armSaver.append(float(i))
                                            armTarget+=1
                                        except Exception as e:
                                            print(f"\033[91mError: {e}\033[0m")
                                            break
                    elif(command=="ea" or command=="emergency abort"):
                        sendCommand="ea"
                        self.send_command(sendCommand)
                        print("You can Close the Session")
                        break
                    else:
                        print("\033[93mEnter Valid Input\033[0m")
            except Exception as e:
                print(f"\033[91mError: {e}\033[0m")
                print("\033[91mTry again, don't use space to separate values, use commas\033[0m")

def main(args=None):
    rclpy.init(args=args)
    client=Phase3Client()
    client.get_user_input()
    client.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()
