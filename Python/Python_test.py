"""This is Python file for Sending UDP Packet to Arduino :)"""
import socket
import time
UDP_IP = "192.168.88.246"
UDP_PORT = 8888
MESSAGE1 = "Oon"
MESSAGE2 = "Ooff"
print "Sending On command to: ", UDP_IP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE1, (UDP_IP, UDP_PORT))
time.sleep(2)
sock.sendto(MESSAGE2, (UDP_IP , UDP_PORT))
