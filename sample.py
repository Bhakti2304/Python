"""use of os and time module"""
import os
import time

#retreiev the current directory path
def current_directory():
    cwd=os.getcwd()
    print(f"my current directory is {cwd}")

#retreive the perticular file path starts from C drive
def file_path(filename):
    path=os.path.abspath((filename))
    print(f"my file path is {path}")


current_directory()
filename="sample.txt"
file_path(filename)

epc=time.time()
print(epc)
localtime=time.localtime(epc)
print(localtime)
print(localtime.tm_year) #\n
print(time.ctime(epc)) #\n