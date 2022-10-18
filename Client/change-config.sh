#!/bin/bash

#获取client端监控进程、tcp、udp客户端的进程，并kill掉
ps01=`ps -ef | grep kc-client.sh | grep -v grep | awk '{print $2}'`
kill -9 $ps01
ps02=`ps -ef | grep tcp-client.py | grep -v grep | awk '{print $2}'`
kill -9 $ps02
ps03=`ps -ef | grep udp-client.py | grep -v grep | awk '{print $2}'`
kill -9 $ps03

#杀掉进程后等待2s，把序列号文件置0
sleep 2
echo 0 > /root/config-udp.txt
echo 0 > /root/config-tcp.txt
sleep 2

#运行监控程序，会自动拉起tcp/udp客户端程序
/bin/sh /root/kc-client.sh &