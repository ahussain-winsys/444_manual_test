import argparse
import sys
import os
import serial

def cmdline_args():
        # Make parser object
    p = argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)

    group1 = p.add_mutually_exclusive_group(required=True)
    group1.add_argument('--tx',action="store_true",help="transmit a file")
    group1.add_argument('--rx',action="store_true",help="receive a file")

    p.add_argument("-f", "--filepath", help="filepath",required=True)
    p.add_argument("-p", "--port", help="COM port", required=True)
    p.add_argument("-b", "--baudrate", type=int, help="baudrate %(default)s", default=115200)
    p.add_argument("-d", "--debug", action="store_true", default=False, help="show bytes being sent or received")
                   
    return(p.parse_args())

def getFileSize(pathToFile):
    size = os.path.getsize(pathToFile)
    print(pathToFile + " is " + str(size) + " bytes")
    return size

def sendFile(pathToFile,port,baud,debug=False):
    filesize = os.path.getsize(pathToFile)
    s = serial.Serial(port,baudrate=baud)
    s.reset_output_buffer()
    print("Transmitting...")
    with open(pathToFile,"rb") as f:
        count = 0
        byte = f.read(1)
        while byte:
            count = count + 1
            s.write(byte)
            if debug:   print(byte.decode("utf-8","ignore"), end="")
            byte = f.read(1)
    s.close()
    if debug:   print("\n")
    print("Transmitted " + str(count) + " bytes")

def receiveFile(pathToFile,port,baud,debug=False):
    s = serial.Serial(port,baudrate=baud,timeout=5)
    s.reset_input_buffer()
    print("Waiting to receive...")
    with open(pathToFile,"wb") as f:
        count = 0
        while True:
            byte = s.read(1)
            if debug:   print(byte.decode("utf-8","ignore"), end="")
            if byte:
                f.write(byte)
                count = count + 1
            else:
                break
    s.close()
    if debug:   print("\n")
    print("Received " + str(count) + " bytes")

if __name__ == "__main__":
    args = cmdline_args()
    if args.debug:  print(args)
    if args.tx:
        getFileSize(args.filepath)
        sendFile(args.filepath,args.port,args.baudrate,args.debug)
    elif args.rx:
        receiveFile(args.filepath,args.port,args.baudrate,args.debug)
        getFileSize(args.filepath)