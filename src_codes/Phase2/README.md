# Phase 2
## About Phase 2
Phase 2 is creating a **Publisher** and a **Subscriber**, but connecting to the subscriber via **Websocket**, and 
publish commands via a **Mobile Application**. 

## How to Run.
I have created **runPhase2.sh**, which does the same automation as before, by eleminating manual entries. 
### ⚠️ Important:
  If you are running the program on **WSL** after running please run **deactivePermission.sh** as **runPhase2.sh** 
  will create a portforwarding and create a firewall rule to connect the Mobile App as it uses **Websockets** and need to do this process to send commands. 
### Running Process
* Open Terminal, either WSL or on Native Linux
* Run:
  ```
  ./runPhase2.sh
  ```
* If it's not working, type the below command and try agani the above one:
  ```
  chmod +x runPhase2.sh
  ```
* After running the above command, you will see two terminal open along with window powershell (if working on WSL)
    <img width="1203" height="721" alt="{12738047-2845-4D0D-A313-D71061317353}" src="https://github.com/user-attachments/assets/8b1e4ee8-5113-48c3-bbde-dd82c2c5b0ac" />
#### Things to Remember:
1. One of the terminal that opened will ask for password to get required websocket for connecton.
2. If working on WSL you will get a prompt to run as administrator to create the required rules and portforwarding, please accept it.
3. Run:
     ```
     ./deactivePermissions.sh
     ```
    * If not working follow the below command and run the above one next:
       ```
       chmod +x deactivePermissions.sh
       ```
## Where to Find APK. 
In this folder, there will be a folder named apk, that apk can be downloaded and can check the real-time working model.

## Reference 
<img width="2147" height="1521" alt="image" src="https://github.com/user-attachments/assets/e97f9ce4-d827-40e8-b0e9-1916081cf42e" />

# Demo
![Phase2_V1](https://github.com/user-attachments/assets/837143d6-d66c-4b32-8c9c-266657cf7bc0)


