#!/bin/env python

import sys
import glob
from appJar import gui
import time
import serial
from serial.tools import list_ports

ser = None

app = gui("Leveling Assistant", "400x400")

""" 
Lists serial port names
    Credit: Thomas
    source: https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python 
"""
def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    return ports

def isConnected():
    global ser
    return ser != None

def connect(baudrate = 250000, serialport = '/dev/tty.SLAB_USBtoUART'):
    global ser
    if not isConnected():
        try:
            ser = serial.Serial(serialport, baudrate)
            time.sleep(2)
            goHome()
        except (OSError, serial.SerialException):
            app.errorBox("Error", "Connection not Possible", parent=None)


def closeConnection():
    global ser
    if isConnected():
        try:    
            ser.close()
            ser = None
        except (OSError, serial.SerialException):
            app.errorBox("Error", "Can't disconnect", parent=None)
    else:
        app.errorBox("Error", "No connection to disconnect was established yet", parent=None)

def goHome():
    global ser
    if isConnected():
        ser.write(str.encode("G28\r\n"))
    else:
        app.errorBox("Error", "No serial connection established", parent=None)


def setIndicator(x, y, z ):
    global ser
    if isConnected():
        destination = "G1 F5000.0 "

        destination += "X" + str(x) + " "

        destination += "Y" + str(y) + " "

        destination += "Z" + str(z)
            
        destination += "\r\n"
        print(destination)
        ser.write(str.encode(destination))
    else:
        app.errorBox("Error", "No serial connection established", parent=None)

def setIndicatorBottomLeft():
    setIndicator(0.0, 80.0, 10.0)
    indicatorToBed()

def setIndicatorBottomRight():
    setIndicator(160.0, 80.0, 10.0)
    indicatorToBed()

def setIndicatorTopLeft():
    setIndicator(0.0, 210.0, 10.0)
    indicatorToBed()

def setIndicatorTopRight():
    setIndicator(160.0, 210.0, 10.0)
    indicatorToBed()

def goHomeIndicator():
    goHome()
    setIndicator(0.0, 80.0, 10.0)
    indicatorToBed()

def indicatorToBed():
    global ser
    if isConnected():
        destination = "G1 F5000.0 "
        destination += "Z" + str(2.0)
        destination += "\r\n"
        print(destination)
        ser.write(str.encode(destination))
    else:
        app.errorBox("Error", "No serial connection established", parent=None)





def press(button):
    
    if button == "Connect":
        connect(250000, app.getOptionBox("Ports"))
    elif button == "Disconnect":
        closeConnection()
    elif button == "Home":
        goHome()
    elif button == "Home Indicator":
        goHomeIndicator()
    elif button == "Top Right":
        setIndicatorTopRight()

    elif button == "Top Left":
        setIndicatorTopLeft()

    elif button == "Bottom Left":
        setIndicatorBottomLeft()

    elif button == "Bottom Right":
        setIndicatorBottomRight()
    else:
        print("Stop! Thats illegal")
        app.stop()



app.addLabel("title", "Welcome to the Leveling Assistant")
app.setLabelBg("title", "white")
app.setFont(15)


app.addLabelOptionBox("Ports",serial_ports())

app.addButtons(["Connect", "Disconnect"], press)
app.addButtons(["Home"], press)
app.addButtons(["Home Indicator"], press)
app.addButtons(["Top Left", "Top Right"], press)
app.addButtons(["Bottom Left", "Bottom Right"], press)
app.go()

