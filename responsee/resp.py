import socket
import sys
import datetime
import responsee.readCsv as csvFile




def socket_service_data():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('127.0.0.1', 80))  # 在同一台主机的ip下使用测试ip进行通信
        # s.bind(('192.168.20.1', 6666))  #在不同主机或者同一主机的不同系统下使用实际ip
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    print("Wait for Connection..................")

    while True:
        sock, addr = s.accept()
        print(sock, "\n", addr)
        buf = sock.recv(1024)  # 接收数据
        buf = buf.decode()  # 解码
        print(buf)
        print("The data from " + str(addr[0]) + " is " + str(buf))
        print("Successfully")
        resp_data = csvFile.readCsv(buf)
        print(resp_data.encode())
        return resp_data
        #sock.close()


if __name__ == '__main__':
    socket_service_data()