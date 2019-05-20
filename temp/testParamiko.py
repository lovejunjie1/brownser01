#!/usr/bin/env python
#coding=utf-8

import paramiko
import os
import sys

#hostname='192.168.50.130'
#username='uploadUser'
#password='uploadUser'
#port=22

hostname='192.168.50.59'
username='figo'
password='WFfigo!23'
port=22

t = paramiko.Transport((hostname, port))
t.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(t)
# 这里的os.path.join 只是个人需要 可以直接sftp.put(local_file_path, remote_file_path)
sftp.put('D:/test.py', '/tmp/test.py')
t.close()
# 目标机器需要打开ssh服务端才行