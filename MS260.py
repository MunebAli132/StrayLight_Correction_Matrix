#Oriel 74055 MS260 spectrograph
#this class uses a rs232 commands to control the spectrograph MS260
#Author: J. Audenaert
# default units are in nm check this using
# UNITS?
#
# GOWAVE XXX.XXX
#   
# shutter commands (shutter open, shutter close and get shutter status)
# SHUTTER O
# SHUTTER C
# SHUTTER?
#
# grating control (goto grating 1, 1200 lines/mm, label for the grating)
# GRAT 1,1200,BLUE
# set the lines/mm for grating 1 to XXXX
# GRAT1LINES XXXX
# 
# grating 1 zero offset should be set to 0.0872665 when using a double grating configuration
# GRAT1ZERO XXX.XXX
import serial
from time import sleep
import io

class MS260:
    def __init__(self,comPort,baud=9600):
        self._comPort = comPort
        self._con= serial.Serial(self._comPort, 
                                 baud,
                                 bytesize=serial.EIGHTBITS,
                                 parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE,
                                 timeout=0.1
                                 )
     
        
        
    def command(self,c):
        """send a command c to the com port associated with this object
        the command is a string"""
        if(not self._con.is_open):
            self._con.open()
            
        c = c+"\n"
           
        #write the command to the port together with a line feed
        self._con.flush()
        self._con.write(c.encode())
        #read the response back = first echo then possible response
        c = self._con.readline()
        answer = self._con.readline()
        

        return answer.decode().replace("\r\n","")

    
    #upon deletion of the object close the port as well
    def __del__(self):
        self._con.close()
        
        
        
        
