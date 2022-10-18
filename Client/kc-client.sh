#!/bin/sh
while true
do
        #获取tcp-client进程号，如果没有，就运行，地址是对端的IP地址
        process1=$(ps -ef | grep tcp-client | grep -v grep);
        if [ "$process1" = "" ]; then
                echo "tcp-client.py not running";
                python3 tcp-client.py 10.2.0.4 &
        else
                echo "tcp-client.py is running";
        fi
        #获取udp-client进程号，如果没有，就运行，地址是对端的IP地址
        process2=$(ps -ef | grep udp-client | grep -v grep);
        if [ "$process2" = "" ]; then
                echo "udp-client.py not running";
                python3 udp-client.py 10.2.0.4 &
        else
                echo "udp-client.py is running";
        fi
        #每15s运行一次
        sleep 15
done