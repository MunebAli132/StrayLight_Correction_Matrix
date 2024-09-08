from MS260 import MS260

#connect to the spectrograph (mapped to com8)
spectr = MS260('COM3')
#open the shutter
spectr.command('shutter o')

#goto grating 2
spectr.command('GRAT 3')
# #goto a center wavelength of 600nm
spectr.command('gowave 530')


