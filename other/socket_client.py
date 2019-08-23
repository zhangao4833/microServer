# -*- coding: utf-8 -*-

import socket

# 创建socket
import time

socket = socket.socket()

# 连接服务端
socket.connect(('127.0.0.1', 7000))

msg = socket.recv(4096) # 阻塞

print(msg.decode('utf-8'))

socket.send('你好，AI服务'.encode('utf-8'))

# socket.close()