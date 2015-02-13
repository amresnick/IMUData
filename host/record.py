import serial
import time

# set up serial port
ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=0)

# create/open an output file
f = open("imuData.csv", "w")

print "Starting to record..."
offset = time.time()
# get data and write into file for 10 second
while (time.time()-offset) < 10:
    data = ser.read()
    f.write(data)
    f.flush()

# close file
f.close()

# close serial port
ser.close()

print "Done recording."
