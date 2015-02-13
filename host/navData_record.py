import serial
import time

# set up serial port
ser = serial.Serial(port=6,baudrate=921600,timeout=0)

# create/open an output file
f = open("navData.txt","wb")

print "Starting to record."

# get data and write into file for 1 second
while time.clock() < 10:
  data = ser.read()
  f.write(data)
  f.flush()

# close file
f.close()

# close serial port
ser.close()

print "Done recording."