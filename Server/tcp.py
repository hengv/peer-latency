# -*- coding: UTF-8 -*-
import socket
import time
import datetime
import os

#定义监听地址和端口
address = ('0.0.0.0',5002)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen()
s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)

#监听
while True:
    #接收TCP数据
    conn, addr = s.accept()

    while True:
        #接收数据
        data = conn.recv(2048)
        if not data:
            break

        #取出时间和序列号
        data_arr = (data.decode("utf-8")).split(",")
        data_time = data_arr[0]
        data_number = data_arr[1]

        #本地时间
        t_d = time.time()
        t_s = float(data_time)

        #计算时延
        delta = ("%.2f" % ((t_d-t_s)*1000))

        #本地时间
        t_l = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        today = datetime.datetime.now()

        #昨天的时间
        yesterday = today + datetime.timedelta(days=-1)
        yt = yesterday.strftime("%Y-%m-%d")

        #文件名
        filename = '/root/tcplog/latency' + yt + '.log'

        #如果序列号为1，把前一天的日志命名为latency+日期.log
        oscmd = 'mv /root/tcplog/latency.log ' + filename
        if data_number == '1':
            #print(oscmd)
            os.system(oscmd)

        #日志写入latency.log文件
        f=open('/root/tcplog/latency.log','a')
        f.write(t_l+','+str(delta)+','+data_number+'\n')
        f.close()
        #print('received:',delta, 'from',addr)

#关闭sock
s.close()