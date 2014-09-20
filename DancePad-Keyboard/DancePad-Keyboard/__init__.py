import serial, time, uinput

ser = serial.Serial('/dev/ttyUSB0', 9600)

#keyList = [uinput.KEY_1, uinput.KEY_0]

#device = uinput.Device(keyList)

#print "Warning Keyboard will start outputting in 5 seconds!"

#time.sleep(5)
ser.write("a")
while True:
    a =  ser.read() 
    #device.emit_click(uinput.KEY_1)
    #time.sleep(.5)
    ser.write(a)
    print a
    #device.emit_click(uinput.KEY_0)
    #time.sleep(.5)
