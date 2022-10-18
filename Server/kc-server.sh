#!/bin/sh
while true
do
        #获取udp进程号，如果没有，就运行
        process1=$(ps -ef | grep udp.py | grep -v grep);
        if [ "$process1" = "" ]; then
                echo "udp.py not running";
                nohup python3 udp.py &
        else
                echo "udp.py is running";
        fi
        #获取tcp进程号，如果没有，就运行
        process2=$(ps -ef | grep tcp.py | grep -v grep);
        if [ "$process2" = "" ]; then
                echo "tcp.py not running";
                nohup python3 tcp.py &
        else
                echo "tcp.py is running";
        fi
        #每15s运行一次
        sleep 15
done