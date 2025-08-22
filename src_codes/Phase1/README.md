# Phase 1

## About Phase 1. 
Phase 1 is creating Publisher and Subscriber and sending commands that simulates non-graphical real-time like output.

## How to run. 
I have created a **runPhase1.sh** file, which will automate all the manual workflows. 
  * Open Terminal, either WSL or Native Linux.
  * Try running the below command from the file directory:
      ```
      ./runPhase1.sh
      ```
* If this is not workig, type this:
   ```
   chmod +x runPhase1.sh
   ```
    * After it ran you can see 2 windows popping up like the below shown image:
        <img width="1228" height="748" alt="{83AD6CC6-8007-4F6B-9B25-38EB01D10896}" src="https://github.com/user-attachments/assets/fefd0849-d196-4890-920c-08c7318fcdba" />

      Everything else is straightforward, as the consol walks through the process.

##  Types of Commands the Program Takes (Not Case-Sensitive). 
  1. **Move to** with a followup question or input asking to enter x, y, z axis values.
  2. **moVe ArM** follows the same process as above.
  3. Take's Integer, **1**, **2** or **3** for respective to **move to**, **Move Arm**, **Emergency Abort** or **EA**.
  4.  Can give the commands straight as **Move To 1,2,3**, **Move arM 0.5,2,2,0.5**, and **Emergency Abort** or **EA**

# Demo
![Phase1Gif_V1](https://github.com/user-attachments/assets/355d085c-c326-4400-9d7e-5a7bb6ac3539)
