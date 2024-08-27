import socket
import os

def send_file(server_ip, server_port, file_path):
    if not os.path.isfile(file_path):
        print(f"The file {file_path} does not exist.")
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    with open(file_path, 'rb') as file:
        data = file.read(1024)
        while data:
            client_socket.send(data)
            data = file.read(1024)

    print('File sent successfully!')
    client_socket.close()

if __name__ == '__main__':
    server_ip = input("Enter the server IP address: ")
    server_port = 5001
    file_path = input("Enter the path of the file to send: ")
    send_file(server_ip, server_port, file_path)
