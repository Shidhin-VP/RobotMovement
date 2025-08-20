if grep -qEi "Microsoft|WSL" /proc/version;then
    powershell.exe -Command "Start-Process powershell -ArgumentList 'netsh interface portproxy delete v4tov4 listenport=9090 listenaddress=0.0.0.0; Remove-NetFirewallRule -DisplayName \"Shidhin_Assestment: WSL Port 9090\"' -Verb RunAs"
    echo "Permissions Removed."
    echo "You are Good to Go."
    echo "Have a Great Programming, Fun Day. :)"
else
    echo "There is nothing to deactive, you are good to go."
    echo "This is only for WSL"
    echo "Have a Great Programming, Fun Day. :)"
fi