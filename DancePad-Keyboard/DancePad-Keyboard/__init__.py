import serial, time, uinput

ser = serial.Serial('/dev/ttyUSB0', 9600)

keyList = [uinput.KEY_LEFT, uinput.KEY_RIGHT, uinput.KEY_UP, uinput.KEY_DOWN]

device = uinput.Device(keyList)

#print "Warning Keyboard will start outputting in 5 seconds!"

#time.sleep(5)
ser.write("a")
while True:
    a =  ser.read() 
    #device.emit_click(uinput.KEY_1)
    #time.sleep(.5)
    ser.write(a)
    print a
    a = ord(a)
    if a & 1 is 1:
        device.emit_click(uinput.KEY_LEFT)
    if a & 2 is 2:
        device.emit_click(uinput.KEY_DOWN)
    if a & 4 is 4:
        device.emit_click(uinput.KEY_UP)
    if a & 8 is 8:
        device.emit_click(uinput.KEY_RIGHT)
    #time.sleep(.5)
