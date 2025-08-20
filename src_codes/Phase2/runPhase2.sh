#!/bin/bash

runSocket="cd $(pwd) && source /opt/ros/humble/setup.bash && source install/setup.bash && sudo apt install -y ros-humble-rosbridge-server && ros2 launch rosbridge_server rosbridge_websocket_launch.xml"
runSub="cd $(pwd) && source /opt/ros/humble/setup.bash && source install/setup.bash && ros2 run phase2robot phase2_sub"

open_native_ubuntu_terminal(){
    if ! command -v gnome-terminal >/dev/null 2>&1;then
        echo "Gnome Terminal Not Found. Installing Gnome....."
        sudo apt update
        sudo apt install -y gnome-terminal
    fi
    colcon build
    gnome-terminal -- bash -c "$runSocket"
    gnome-terminal -- bash -c "$runSub"
}

open_wsl_terminal(){
    colcon build
    cmd.exe /c start wsl -e bash -c "$runSocket"
    cmd.exe /c start wsl -e bash -c "$runSub"
}

if grep -qEi "Microsoft|WSL" /proc/version;then
    echo "Running Phase 2"
    echo "Running on WSL"
    ip=$(hostname -I)
    echo "Choose Your Correct Windows IP Address to Enter in Mobile Application"
    cmd.exe /c IPConfig | grep "IPv4"
    powershell.exe -Command "Start-Process powershell -ArgumentList 'netsh interface portproxy add v4tov4 listenport=9090 listenaddress=0.0.0.0 connectport=9090 connectaddress=$ip; New-NetFirewallRule -DisplayName \"Shidhin_Assestment: WSL Port 9090\" -Direction Inbound -LocalPort 9090 -Protocol TCP -Action Allow' -Verb RunAs"
    open_wsl_terminal
else
    echo "Running Phase 2"
    echo "Running on Native Linux"
    open_native_ubuntu_terminal
fi