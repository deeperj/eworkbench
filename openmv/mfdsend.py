


ser = serial.Serial('/dev/ttyACM0')  # open serial port
ser.baudrate = 115200

# This is just a simplified version, I am sure the correct section of the data is captured
# since data separators are used.
size = struct.unpack("<L", ser.read(4))[0]
data = ser.read(size) # Read data

f = open("img.jpg", 'wb')  # open in binary
f.write(data)
f.close()
