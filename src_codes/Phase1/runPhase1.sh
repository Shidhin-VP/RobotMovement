#!/bin/bash

runPub="cd $(pwd) && source /opt/ros/humble/setup.bash && source install/setup.bash && ros2 run moverobotphase1 pub1_node; exec bash"
runSub="cd $(pwd) && source /opt/ros/humble/setup.bash && source install/setup.bash && ros2 run moverobotphase1 sub1_node; exec bash"

open_native_ubuntu_terminal() {
    if ! command -v gnome-terminal >/dev/null 2>&1; then
        echo "Gnome Terminal Not Found. Installing Gnome......"
        sudo apt update
        sudo apt install -y gnome-terminal
    fi
    echo "Running Phase 1"
    gnome-terminal -- bash -c "$runPUb"
    gnome-terminal -- bash -c "$runSub"
}

open_wsl_terminal(){
    echo "Running Phase 1"
    cmd.exe /c start wsl -e bash -c "$runPub"
    cmd.exe /c start wsl -e bash -c "$runSub"
}


if grep -qEi "Microsoft|WSL" /proc/version;then
    echo "Running on WSL"
    open_wsl_terminal
else 
    echo "Running on Native Linux"
    open_native_ubuntu_terminal
fi