import serial

tx_msg = (b'hello')

ser = serial.Serial('/dev/ttymxc1', baudrate=115200, timeout=1)  # open first serial port
print(ser.portstr)       # check which port was really used
ser.write(tx_msg)      # write a string
print("Sending - " + str(tx_msg))
msg = ser.read(size=100) #read the content of the input buffer until you get 100 byte or a timeout event
print("Received - " + str(msg)) #print the content you might need to decode it print(decode(msg))
ser.close()

if str(tx_msg) == str(msg):
    print("PASS")
else:
    print("FAIL")