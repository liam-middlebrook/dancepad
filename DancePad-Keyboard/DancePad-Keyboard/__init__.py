import serial, time, uinput

ser = serial.Serial('/dev/ttyUSB1', 9600)

keyList = [uinput.KEY_1, uinput.KEY_0]

device = uinput.Device(keyList)

print 'Warning Keyboard will start outputting in 5 seconds!'

time.sleep(5)

while True:
    ser.write('255\n')
    device.emit_click(uinput.KEY_1)
    time.sleep(.5)
    ser.write('0\n')
    device.emit_click(uinput.KEY_0)
    time.sleep(.5)
