import socket

socket_server=socket.socket()
# 绑定ip地址和端口
socket_server.bind(("localhost",8888))# 绑定到本机的8888端口
# 监听
socket_server.listen(1)# 允许连接的数量
# 等待客户端连接

# result:tuple=socket_server.accept()
# conn=result[0]                 # 客户端和服务端的连接对象
# address=result[1]              # 客户端地址
conn,address=socket_server.accept() # 如果没有连接，则阻塞等待
print(f"客户端信息：{address}")
while True:
    # 接收客户端信息，用客户端和服务端的连接作为对象
    data=conn.recv(1024).decode("utf-8")# recv接受的参数是缓冲区大小，返回值是一个字节数组，不是字符串，通过decode转换为字符串
    print(f"客户端发来的消息为：{data}")
    # 回复
    msg=input("请输入回复：")# 将字符串编码为字符数组
    if msg=="exit":
        break

    conn.send(msg.encode("utf-8"))
# 关闭连接
conn.close()
socket_server.close()