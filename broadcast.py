import socket
import time

def broadcast_thread(data_to_send,ip_list):
    time.sleep(4)
    print("starting broadcast")
    print(data_to_send)
        
    # configure socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.settimeout(.001)
    for i in ip_list:
        print(f"ip:{i}")
        server_address = (i,8000)
        sock.connect(server_address)
        for i in data_to_send:
            msg = str(i) 
            print(msg)
            sock.sendall(msg.encode())

    # send neighbour topology to everyone

