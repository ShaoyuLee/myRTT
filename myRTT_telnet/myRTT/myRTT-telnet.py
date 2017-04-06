import sys
import os
import time  

import telnetlib

def main():

    ret=os.system('taskkill -im jlink.exe') # restart Jlink
    print(ret)
    try:
        ret=os.system(r'start "" "c:\Program Files (x86)\SEGGER\JLink_V512g\JLink.exe" -device nrf51822 -if swd -speed 4000 -autoconnect 1')
    except IOError:
        print("Start JLink.exe Failed\n")
    print(ret)
    
    time.sleep(1)  
    try:
        rtt = telnetlib.Telnet('localhost', 19021)
        while(True):
            try:
                data = rtt.read_until('\n',0.1) # below 0.2 may has space
                #data = rtt.read_all            # always stop
                #data = rtt.read_eager()        # read may has space
                #data = rtt.read_very_eager()   # read may has space
                #data = rtt.read_lazy()         # no data
                #data = rtt.read_very_lazy()    # no data
                #data = rtt.read_sb_data()      # no data
            except:
                print("Read Error\n")
                break
            if data:
                #print data,  # one may do further processing here
                sys.stdout.write(data)
        rtt.close()
    except IOError:
        print("Connect Error\n")

    try:
        input("Press \"Enter\" to continue")
    except SyntaxError:
        pass

    return 0

if __name__ == '__main__':
    sys.exit(main())