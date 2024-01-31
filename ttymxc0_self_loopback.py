import serial

ser = serial.Serial('/dev/ttymxc0', baudrate=115200, timeout=1)  # open first serial port
print(ser.portstr)       # check which port was really used
ser.write(b'hello')      # write a string
msg = ser.read(size=100) #read the content of the input buffer until you get 100 byte or a timeout event
print(msg) #print the content you might need to decode it print(decode(msg))
ser.close()