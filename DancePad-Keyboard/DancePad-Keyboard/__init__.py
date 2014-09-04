import serial, time

ser = serial.Serial('/dev/ttyUSB1', 9600)

while True:
    ser.write('255\n')
    time.sleep(.5)
    ser.write('0\n')
    time.sleep(.5)
