# -*- coding: UTF-8 -*-
import socket
import time
import sys

#定义服务器IP地址和端口
IP = sys.argv[1]
PORT = 5002

#打开序列号配置文件，读取序列号。初始时，此序列号为0，程序运行后，会写入序列号。当程序意外推出，再运行时，可以读取序列号继续进行
c=open("config-tcp.txt",'r')
c_data=c.readline()
c.close()
if c_data == '0':
    n = 1
else:
    n=int(c_data)+1

#定义TCP的sock
sock = socket.socket()
sock.connect((IP,PORT))

#循环发包
while True:
    #发送信息：时间+序列号
    t=time.time()
    MESSAGE = str(t)+','+str(n)

    #日志内容：本地+IP+端口+时间+序列号
    loginfo=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+','+IP+','+str(PORT)+','+str(t)+','+str(n)

    #发送数据到服务器端
    byt=MESSAGE.encode()
    sock.send(byt)

    #本地日期
    t_d = time.strftime("%Y-%m-%d", time.localtime())

    #写日志，tcp日志部署在/root/tcplog目录中
    filename = '/root/tcplog/' + t_d + 'sendlog.txt'
    f=open(filename,'a')
    f.write(loginfo+'\n')
    f.close()

    #写序列号到配置文件
    g=open("config-tcp.txt",'w+')
    g.write(str(n))
    g.close()

    #序列号+1
    n=n+1

    #每秒发送2次
    time.sleep(0.5)