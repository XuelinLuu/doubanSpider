import socket
import sys
def sock_client_data():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # s.connect(('192.168.20.1', 6666))  #服务器和客户端在不同的系统或不同的主机下时使用的ip和端口，首先要查看服务器所在的系统网卡的ip
            s.connect(('127.0.0.1', 80))  #服务器和客户端都在一个系统下时使用的ip和端口
        except socket.error as msg:
            print(msg)
            print(sys.exit(1))
        data = input("input data:")   #输入要传输的数据
        s.send(data.encode())  #将要传输的数据编码发送，如果是字符数据就必须要编码发送
        data = s.recv(1024)
        print(data.decode())
        #s.close()
if __name__ == '__main__':
    sock_client_data()