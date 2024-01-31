import sys
import argparse
from time import sleep
import gpiod
    
def main():
    
    status = False
    gpiochip = "gpiochip0"
    gpolist = [0,1]
    gpilist = [3,5]
    outlines = []
    inlines = []
    
    outcfg = gpiod.line_request()
    outcfg.consumer = "Line"
    outcfg.request_type = gpiod.line_request.DIRECTION_OUTPUT
    
    incfg = gpiod.line_request()
    incfg.consumer = "Line"
    incfg.request_type = gpiod.line_request.DIRECTION_INPUT
    
    chip = gpiod.chip(gpiochip)
    
    outlines = chip.get_lines(gpolist)
    inlines = chip.get_lines(gpilist)
    
    outlines.request(outcfg)
    inlines.request(incfg)
    
    for x in range(4):
        val = [int(i) for i in list('{0:0b}'.format(x))]
        while len(val) is not len(outlines):
            val.insert(0,0)
        print("OUT\t" + str(val))
        outlines.set_values(val)
        i = inlines.get_values()
        print("IN\t" + str(i))
        a = set(val)
        b = set(i)
        if a != b:
            status = False
            break
        else:
            status = True

    if status is True: print("PASS")
    else: print("FAIL")

if __name__ == '__main__':
    sys.exit(main())