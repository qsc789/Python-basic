import socket
socket_client=socket.socket()
socket_client.connect(("localhost",8888))
while True:
    # 发消息
    msg=input("输入：")
    if msg=='exit':
        break
    socket_client.send(msg.encode("utf-8"))
    # 收消息
    recv_data=socket_client.recv(1024)
    print(f"服务端回复的消息为：{recv_data.decode('utf-8')}")
# 关闭连接
socket_client.close()