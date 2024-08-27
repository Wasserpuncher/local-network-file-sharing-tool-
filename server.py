import socket

def start_server(host='0.0.0.0', port=5001):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'Server listening on {host}:{port}')

    conn, addr = server_socket.accept()
    print(f'Connection from {addr} has been established!')

    with open('received_file', 'wb') as file:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)

    print('File received successfully!')
    conn.close()

if __name__ == '__main__':
    start_server()
