import RPi.GPIO as io 
io.setmode(io.BCM) 
import sys 
import os

in1_pin = 4
in2_pin = 17

lpin = 9
rpin = 10

io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)
io.setup(lpin, io.OUT)
io.setup(rpin, io.OUT)

def clockwise():
    io.output(in1_pin, True)    
    io.output(in2_pin, False)

def right():
    io.output(rpin, True)
    io.output(lpin, False)
    os.system('echo 0=65% > /dev/servoblaster')
    os.system('touch /home/pi/test')

def left():
    io.output(lpin, True)
    io.output(rpin, False)
    os.system('echo 0=38% > /dev/servoblaster')

def center():
    os.system('echo 0=54% > /dev/servoblaster')


def counter_clockwise():
    io.output(in1_pin, False)
    io.output(in2_pin, True)


def stop():
    io.output(in1_pin, False)
    io.output(in2_pin, False)
clockwise()


while True:

    #direction = str(raw_input("Enter Direction : "))
    direction = str(sys.argv[1])
    
    if direction == "b":
        clockwise()
        break

    elif direction == "f" : 
        counter_clockwise()
        break

    elif direction == "r":
        right()
        #stop()
        break

    elif direction == "l":
        left()
        #stop()
        break

    elif direction == "c":
        center()
        #stop()
        break

    else:
        stop()
	center()
        break
