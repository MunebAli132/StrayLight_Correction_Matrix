
import matplotlib.pyplot as plt
import os, sys
#wrapper library to control the andor ccd
from AndorCCD import AndorCCD
from AndorErrorCodes import AndorErrorCodes
import time
try:
       ccd 
except NameError:
       ccd = AndorCCD('./Andor_420OE_CC_001/','Atmcd32d.dll')

#retrieve the detectorsize (stored in ccd.pixelX and ccd.pixelY)
ccd.getDetectorSize()

#define integration time for the ccd
intTime = 0.016
#define wanted ccd temperature
desiredTemp = 10

#turn on the cooler of the ccd and wait untill the temperature is reached
ccd.coolerOn(-20)
# while(ccd.E!=AndorErrorCodes.DRV_TEMPERATURE_STABILIZED):
#               #update temperature
              # print(ccd.E)
              # ccd.getTemperature()
              # print('currentTemp:'+str(ccd.currentTemp))
#               #wait 5 seconds
#               time.sleep(5)
# print('Temperature stabilized...')

#perform aqcuisition of an image 
#if we get here the temperature has reached the desired temperature
ccd.performAqcuisition(1,1);
#wait untill aqcuisition is complete
while(ccd.readyForNextAqc == False):
       time.sleep(1)
#aqcuisition is done so store the data in the dataholder
data = ccd.data


plt.figure()
plt.plot(data)