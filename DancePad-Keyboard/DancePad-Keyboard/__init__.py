import serial, time
from pykeyboard import PyKeyboard

ser = serial.Serial('/dev/ttyUSB0', 9600)

k = PyKeyboard()
#keyList = [uinput.KEY_LEFT, uinput.KEY_RIGHT, uinput.KEY_UP, uinput.KEY_DOWN]

#device = uinput.Device(keyList)

#print "Warning Keyboard will start outputting in 5 seconds!"

#time.sleep(5)
ser.write("a")
while True:
    a =  ser.read() 
    ser.write(a)
    #print a
    a = ord(a)
    if a & 1 is 1:
	k.tap_key(k.left_key)
    if a & 2 is 2:
	k.tap_key(k.down_key)
    if a & 4 is 4:
	k.tap_key(k.up_key)
    if a & 8 is 8:
	k.tap_key(k.right_key)
