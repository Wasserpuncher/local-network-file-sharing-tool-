# Local Network File Sharing Tool

## Overview

The Local Network File Sharing Tool is a simple application that allows users to share files over a local network using TCP/IP sockets. Users can easily send and receive files between devices.

## Features

- Send files from one device to another over the local network.
- Easy-to-use command line interface.
- Utilizes Python's socket library for network communication.

## Technologies Used

- Python 3.x
- Socket library for network communication

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Wasserpuncher/local-network-file-sharing-tool.git
   cd local-network-file-sharing-tool
No additional dependencies are required, as the socket library is included with Python.
Usage
Running the Server
Open a terminal window.
Navigate to the project directory.
Run the server script:

python server.py


Sending a File
Open another terminal window.

Navigate to the project directory.

Run the client script:

python client.py


# On the server terminal
$ python server.py
Server listening on 0.0.0.0:5001
Connection from ('192.168.1.2', 53000) has been established!
File received successfully!

# On the client terminal
$ python client.py
Enter the server IP address: 192.168.1.1
Enter the path of the file to send: /path/to/file.txt
File sent successfully!


Contribution
Feel free to contribute to this project by reporting issues, suggesting features, or submitting pull requests.

License
This project is licensed under the MIT License. See the LICENSE file for more information.

Acknowledgments
Thanks to the open-source community for providing tools and resources that made this project possible!

