import serial
import time

# set up serial port
ser = serial.Serial(port='dev/ttyACM0', baudrate=921600, timeout=0)

# create/open an output file
f = open("imuData.csv", "w")

print "Starting to record..."

# get data and write into file for 10 second
while time.clock() < 10:
    data = ser.read()
    f.write(data)
    f.flush()

# close file
f.close()

# close serial port
ser.close()

print "Done recording."
