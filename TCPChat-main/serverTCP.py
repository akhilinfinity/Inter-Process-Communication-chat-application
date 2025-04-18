import socket

host = "127.0.0.1"
port = 5001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)  # Allow multiple clients

print(f"Server listening on {host}:{port}")

conn, addr = server_socket.accept()
print(f"Connection established with: {addr}")

while True:
    try:
        message = conn.recv(1024).decode()
        if not message:
            break  # Exit loop if client disconnects

        print(f"Client: {message}")
        response = input("Server: ")  # Allow server to type a response
        conn.send(response.encode())  # Send response to client

    except Exception as e:
        print(f"Error: {e}")
        break

conn.close()
server_socket.close()
print("Server closed.")
