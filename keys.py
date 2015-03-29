import sys
import os
while True:
    char = sys.stdin.read(1)
    if char == "w":
        os.system('sudo python motor-control.py f')
    elif char == "s":
        os.system('sudo python motor-control.py b')
    elif char == "x":
        os.system('sudo python motor-control.py s')
    elif char == "d":
        os.system('sudo python motor-control.py r')
    elif char == "a":
        os.system('sudo python motor-control.py l')
    elif char == "c":
        os.system('sudo python motor-control.py c')
    else:
        pass
