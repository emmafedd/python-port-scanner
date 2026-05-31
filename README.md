#🛡️ Python Port Scanner: The Robot on the Street
🤖 The Story (How it Works):
Imagine a street with a long line of houses (these are the Ports). I built a Robot (this Python script) to walk down that street and find out which doors are open.

.The Robot walks to a house and knocks on the door (socket.connect_ex).

.The Robot is instructed to wait exactly 0.5 seconds for an answer.

.If the door opens: The Robot shouts "OPEN!" and writes down the house number.

.If there is no response within 0.5 seconds, the Robot assumes the door is locked or the house is empty and moves immediately to the next one.

🛠️  (Functions & Tools)
In this project, I used specific Python "Tools" to give the Robot its abilities:

1. The Libraries :
import socket: The "Internet Library." This allows Python to open a connection to another computer over a network.

from datetime import datetime: The "Robot's Watch." This records the exact second the scan starts and ends.

2. The Network Settings :
AF_INET: This is the "Address Translator." It tells the robot to use IPv4 (the standard internet address format like 192.168.1.1).

SOCK_STREAM: This is the "Reliable Connection." It tells the robot to use TCP, which requires a "Three-Way Handshake" to confirm a door is truly open.

3. The Logic :
range(1, 101): The "Street Map." It tells the robot to check houses #1 through #100.

.settimeout(0.5): The "Patience Level." This makes the robot fast so it doesn't waste time waiting at dead ends.

🛡️ Error Handling :
I added a try / except block to ensure the robot doesn't "trip" and crash if something goes wrong:

KeyboardInterrupt: Allows the user to stop the robot safely by pressing Ctrl + C.

socket.gaierror: Handles cases where the user gives an address that doesn't exist.

socket.error: Handles cases where the computer has no internet connection.

 How to Run :
Run the script: python scanner.py

Enter a target (e.g., scanme.nmap.org)

Watch the Robot work!..
#end
