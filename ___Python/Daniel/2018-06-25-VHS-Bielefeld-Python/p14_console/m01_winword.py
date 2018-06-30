import os
import subprocess

cmd = 'cmd /C "C:/Program Files (x86)/Microsoft Office/Office16/winword.exe"'

p = subprocess.Popen(cmd) # asynchron

#os.system(cmd) # synchron

print("Hello")
