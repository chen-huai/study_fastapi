# web服务器
import socket

sock = socket.socket()

sock.bind(("127.0.0.1", 8088))

sock.listen(5)
while 1:
    # 阻塞等待客户端连接
    conn, addr = sock.accept()

    data = conn.recv(10240)
    print("客户端发送的请求信息：\n%s" % data)

    # conn.send(b"hello world")  # 这种方式没有响应首行,没有响应头无法返回
    conn.send(b"HTTP/1.1  200  ok\r\nserver:yuan\r\n\r\nhello world")
    conn.close()
