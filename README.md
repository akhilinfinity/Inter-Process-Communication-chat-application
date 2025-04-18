Inter-Process Communication Chat Application (Client-Server TCP)
This project demonstrates a simple Client-Server Chat Application using Inter-Process Communication (IPC) and TCP in Python. The chat application enables two or more processes (clients) to communicate with each other over a network. This project is built using Python's socket programming and multithreading for handling multiple clients simultaneously.

Project Overview
The chat application consists of:

Server: The central point where clients connect and send messages.

Client: The user interface for sending and receiving messages.

IPC Mechanism: Enables communication between processes via TCP sockets.

Features
Real-time communication between multiple clients.

Server-side message handling to broadcast messages to all connected clients.

Threaded client handling, allowing multiple clients to connect and interact concurrently.

Technologies Used
Python (Socket programming, Multithreading)

TCP/IP for network communication

Inter-Process Communication (IPC)

Installation
Clone this repository to your local machine:

bash
Copy
Edit

cd IPC-Chat-Application
Ensure Python 3.x is installed on your machine.

To check:

bash
Copy
Edit
python --version
Install the required dependencies (if any):

bash
Copy
Edit
pip install -r requirements.txt
Usage
Start the Server:

In the project directory, open a terminal and run:

bash
Copy
Edit
python server.py
The server will start listening for incoming client connections on a specified port.

Start a Client:

Open another terminal window and run:

bash
Copy
Edit
python client.py
You can run multiple instances of the client on different terminals to simulate multiple users.

Communicate:

Once the server and clients are running, you can start chatting! All clients connected to the server can send and receive messages in real-time.

Directory Structure
bash
Copy
Edit
IPC-Chat-Application/
│
├── server.py           # Server-side code to handle client connections
├── client.py           # Client-side code for chat interface
├── requirements.txt    # List of required Python packages (if any)
├── README.md           # Project documentation
Contributing
Fork this repository.

Create a new branch (git checkout -b feature-branch).

Make your changes.

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin feature-branch).

Open a pull request.

