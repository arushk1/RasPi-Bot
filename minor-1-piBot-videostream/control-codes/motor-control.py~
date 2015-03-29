import RPi.GPIO as io
io.setmode(io.BCM)
import sys
import os

in1_pin = 4
in2_pin = 17

io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)

def clockwise():
    io.output(in1_pin, True)    
    io.output(in2_pin, False)

def right():
    os.system('echo 0=60% > /dev/servoblaster')

def left():
    os.system('echo 0=35% > /dev/servoblaster')

def center():
    os.system('echo 0=47% > /dev/servoblaster')


def counter_clockwise():
    io.output(in1_pin, False)
    io.output(in2_pin, True)
def stop():
    io.output(in1_pin, False)
    io.output(in2_pin, False)
clockwise()


while True:
    direction = str(sys.argv[1])
    
    if direction == "b":
        clockwise()
        break

    elif direction == "f" : 
        counter_clockwise()
        break

    elif direction == "r":
        right()
        stop()
        break

    elif direction == "l":
        left()
        stop()
        break

    elif direction == "c":
        center()
        stop()
        break

    else:
        stop()
        break
