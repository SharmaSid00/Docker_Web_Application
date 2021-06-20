#!/usr/bin/python3
import cgi
import subprocess
import time
print("content-type: text/html")
print()

s=cgi.FieldStorage()
cmd=s.getvalue("x")

if cmd=="images":
    cmd= "docker images"
    output = subprocess.getoutput("sudo "+cmd)

elif cmd=="list":
    cmd= "docker ps"
    output = subprocess.getoutput("sudo "+ cmd)

elif cmd=="run":
    cmd= "docker run -dit "+ s.getvalue("y")
    output = subprocess.getoutput("sudo "+ cmd)

elif cmd=="exec":
    cmd= "docker exec -i "+ s.getvalue("y")+" "+s.getvalue("z")
    output = subprocess.getoutput("sudo "+ cmd)

elif cmd=="download":
    cmd= "docker pull "+ s.getvalue("y")
    output = subprocess.getoutput("sudo "+ cmd)

elif cmd=="rm":
    cmd= "docker rm -f "+s.getvalue("y")+" --force"
    output = subprocess.getoutput("sudo "+ cmd)

print("<br>")
print("<pre>")
print(output)
print("</pre>")