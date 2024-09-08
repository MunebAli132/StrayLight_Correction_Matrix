from ctypes import create_string_buffer, c_double, c_long, create_unicode_buffer, windll, byref, c_char_p,c_uint8
import ctypes as cts
from time import sleep
import sys

cfgFile = c_char_p('./system.cfg'.encode('utf-8'))

atrFile = c_char_p('./system.atr'.encode('utf-8'))

error_report = c_char_p((' '*255).encode('utf-8'))
ret = 0
mono =  windll.LoadLibrary('./benhw32_stdcall.dll')

ret = mono.BI_report_error()
print(ret)

ret = mono.BI_build_system_model(cfgFile,error_report)
print(ret)

ret = mono.BI_report_error()
print(ret)

ret = mono.BI_load_setup(atrFile)
print(ret)
mono.BI_initialise()
mono.BI_park()
a = c_long(1)
mono.BI_select_wavelength(c_double(470),byref(a))

del mono

# //-----------------------------------------------------------------------------
# // Bentham Instruments Spectroradiometer Control DLL
# // Error code definition file
# //-----------------------------------------------------------------------------

#define BI_OK 0
#define BI_error -1
#define BI_invalid_token -2
#define BI_invalid_component -3
#define BI_invalid_attribute -4
#define BI_no_setup_window -5

#define BI_no_error 0

#define BI_PMC_timeout 1
#define BI_MSC_timeout 2
#define BI_MSD_timeout 3
#define BI_MAC_timeout 4
#define BI_MAC_invalid_cmd 5

#define BI_225_dead 10
#define BI_265_dead 11
#define BI_267_dead 12
#define BI_277_dead 13

#define BI_262_dead 14

#define BI_ADC_read_error 20
#define BI_ADC_invalid_reading 21
#define BI_ADC_Overload 22

#define BI_AMP_invalid_channel 30
#define BI_AMP_invalid_wavelength 31
#define BI_SAM_invalid_wavelength 32
#define BI_turret_invalid_wavelength 33
#define BI_turret_incorrect_pos 34
#define BI_MVSS_invalid_width 35

#define BI_undefined_error 100