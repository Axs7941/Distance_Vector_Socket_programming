import socket
import threading
import argparse
import read
import broadcast

BUFFER_SIZE = 1024

def handle_message(message, client_address):
    print(f"Received message from {client_address}: {message.decode()}")

def run_server():
    # create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # bind the socket to the IP address and port number
    server_socket.bind((args.ip, args.port))
    
    print(f"Server is listening on {args.ip}:{args.port}")

    # listen for incoming messages
    while True:
        message, client_address = server_socket.recvfrom(BUFFER_SIZE)
        
        # handle incoming message in a new thread
        t = threading.Thread(target=handle_message, args=(message, client_address))
        t.start()

def broadcasting(ip):
    data_to_send,ip_list=read.read_config(ip,'table.csv')
    broadcast.broadcast_thread(data_to_send,ip_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip', type=str, default='127.0.0.1', help='the ip of the host')
    parser.add_argument('-p', '--port', type=int, default=8000, help='the port number to listen on')
    args = parser.parse_args()
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    broadcast_thread = threading.Thread(target=broadcasting, args=(args.ip,))
    broadcast_thread.start()
    broadcast_thread.join()
