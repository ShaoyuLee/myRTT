import sys
import os
import time  

import socket
  
if __name__ == '__main__':  
    ret=os.system('taskkill -im jlink.exe') # restart Jlink
    print(ret)
    try:
        ret=os.system(r'start "" "c:\Program Files (x86)\SEGGER\JLink_V612d\JLink.exe" -device NRF52832_XXAA -if swd -speed 4000 -autoconnect 1')
    except IOError:
        print("Start JLink.exe Failed\n")
    print(ret)    
    
    time.sleep(1)  
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        sock.connect(('localhost', 19021))  #localhost 127.0.0.1

        while(True):

            try:
                 sock.send('')
            except IOError:
                print("Connection break\n")
                break

            try:
                data = sock.recv(1024000)
                if data:
                    #print data,
                    sys.stdout.write(data)
            except IOError:
                #print("Read Error\n") 
                pass

            time.sleep(0.1)  
                    
    except IOError:
        print("Connect Failed\n") 

    try:
        sock.close()  
    except IOError:
        print("Close Failed\n")
 
    try:
        input("Press \"Enter\" to continue")
    except SyntaxError:
        pass