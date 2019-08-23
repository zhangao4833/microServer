# -*- coding: utf-8 -*-
import socket

# 创建socket（实现网络之间的通信，还可以实现进程间通信）
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定host和port
server.bind(('0.0.0.0',7000))

# 监听并接受客户端连接
server.listen()

# 等待接受客户端连接
client, addr = server.accept() # 阻塞的方法

print('%s 已连接' % str(addr))


# 向客户端发送消息
client.send('你好，AI'.encode('utf-8'))

msg = client.recv(4096)
print(addr, msg.decode('utf-8'))
# 等着客户端发来消息

client.close()
server.close()