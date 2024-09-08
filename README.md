
# Stray Light Correction Project

This repository contains the code, analysis, and supporting materials for the **Stray Light Correction Project**. The project aims to correct stray light effects in spectroradiometers using matrix-based correction methods. This work is inspired by the research paper *“Simple spectral stray light correction method for array spectroradiometers”* by Yuqin Zong et al.

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

## References

- Zong, Y., Brown, S. W., Johnson, B. C., Lykke, K. R., & Ohno, Y. (2008). *Simple spectral stray light correction method for array spectroradiometers*. Journal of Atmospheric and Oceanic Technology, 26(1), 57-73.
- Additional resources:
  - [Correction of Stray Light in Spectroradiometers and Imaging Instruments | NIST](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=841127)
 
 ## Future work

 Future work requires investigating which can be seen at the end of `DataAnalysis.ipynb`file .
