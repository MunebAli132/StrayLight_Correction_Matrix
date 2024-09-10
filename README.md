
# Stray Light Correction Project

This repository contains the code related to data acquisition and analysis for the **Stray Light Correction Project**. The project aims to correct stray light effects in spectroradiometers using matrix-based correction methods. This work is inspired by the research paper *“Simple spectral stray light correction method for array spectroradiometers”* by Yuqin Zong et al.

## Project Overview

Stray light in spectroradiometers leads to errors in the spectral data, and correcting for these errors is essential for accurate measurements. This project implements a method for calculating and applying a stray light correction matrix, which improves the quality of the data collected from the spectrometer.

## Contents

### Notebooks:
- **Algorithms.ipynb**: Contains the implementation of various correction algorithms and data analysis routines, including noise handling and correction matrix computations.
- **DataAnalysis.ipynb**: Focuses on the data processing steps, including readout noise, dark noise, and the validation process for the corrected spectral data.

## Workflow

1. **Setting up the environment**:
   - A 32-bit Anaconda environment with Python 3.7 is used.
   - Key software components:
     - Andor CCD library (driver pack version: 2.104.30065.0)
     - MS260 spectrograph with COM port connection.
   - DLL configuration files for the spectrometer.
   
2. **Data Acquisition**:
   - **Readout and Dark Noise**: Measure and store noise data across a range of integration times.
   - **Light Measurement**: Capture spectral data and adjust integration times to avoid saturation.
   - **Line Spread Function (LSF)** and **Stray Light Signal Distribution Function (SDF)** are calculated and used to correct the acquired data.

3. **Data Analysis**:
   - Computation of the **Correction Matrix** for stray light using predefined algorithms.
   - Analysis of the signal components including light, dark noise, and stray light.
   - Validation of the correction matrix with ongoing improvements.
## Visuals From data analysis 

 ![image](https://github.com/user-attachments/assets/3d6053f1-b3e6-43ad-b4f7-952c59397d65)
![image](https://github.com/user-attachments/assets/5040398f-7139-4351-ad6b-f513b0d57a56)
![image](https://github.com/user-attachments/assets/cbc93c67-9467-4ead-b427-2c34f9ec6c66)
![image](https://github.com/user-attachments/assets/67b44ac7-7cad-461b-8dbf-b41f73f8da83)
![image](https://github.com/user-attachments/assets/60a0cd87-ef7e-4941-a10d-11ac8b9374fb)





## Requirements

- Python 3.7
- Anaconda
- Required Libraries:
  - NumPy
  - Matplotlib
  - Ctypes (for handling DLLs)
  - CSV (for data storage)

Ensure the Andor driver is installed and the monochromator’s DLL is loaded properly for accurate measurements.

## How to Run

1. Set up the environment using the provided configurations.
2. Run the `Algorithms.ipynb` notebook to initialize the correction matrix algorithms.
3. Use the `DataAnalysis.ipynb` notebook to process and validate the spectrometer data.

## Future work
Our future work will investigate the spike present in the spectrometer response, as observed at the end of the 'DataAnalysis.ipynb' file. It should be noted that this spike is specific to the spectrometers used. This unexpected response is also observed when using the He-Ne laser beam (632.8 nm). A comprehensive description of the starry light matrix will necessitate the elimination of all forms of unexpected responses.
![image](https://github.com/user-attachments/assets/d1a0854f-5496-4a13-82cb-4cbc6eefa381)


## References

- Zong, Y., Brown, S. W., Johnson, B. C., Lykke, K. R., & Ohno, Y. (2008). *Simple spectral stray light correction method for array spectroradiometers*. Journal of Atmospheric and Oceanic Technology, 26(1), 57-73.
- Additional resources:
  - [Correction of Stray Light in Spectroradiometers and Imaging Instruments | NIST](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=841127)
 
