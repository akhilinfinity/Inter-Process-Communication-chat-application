import socket

host = "127.0.0.1"
port = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((host, port))
    print("Connected to the server. Type messages below:")

    while True:
        message = input("Client: ")  # Allow client to type a message
        if message.lower() == "exit":
            break  # Exit if user types 'exit'
        
        client_socket.send(message.encode())

        response = client_socket.recv(1024).decode()
        print(f"Server: {response}")

except ConnectionRefusedError:
    print("[ERROR] Could not connect to server. Make sure the server is running!")

client_socket.close()
print("Disconnected from the server.")
