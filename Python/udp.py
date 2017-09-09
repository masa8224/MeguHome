def main(n):
    import socket
    UDP_IP = "192.168.88.246"
    UDP_PORT = 8888
    MESSAGE = "0"+n
    SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    SOCK.sendto(MESSAGE, (UDP_IP, UDP_PORT))

if __name__ == "__main__":
    import sys
    ARGV = sys.argv[1]
    if ARGV != "":
        main(ARGV)
