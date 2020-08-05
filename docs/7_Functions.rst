Functions
=========

This code contains 5 main functions to analyze wave data (water level data) time series. Water level could be in a form of the total depth or it can be in the form of surface elevation. If a pressure sensor is used for data collection, then it is required to correct the data for pressure attenuation in the water column. In such cases, only water depth data should be used as an input. In any other cases, either of water surface elevation or water depth time series can be used for data analysis.

The provided “RunOceanlyz.m” file analyzes the the entire time series by calling an appropriate function(s). Note that any of these functions may be called by a user in his/her own code as well.

|

The main functions that are used in this toolbox are:

===================   =======================================================================
Function	          Description
===================   =======================================================================
WaveSpectraFun        Calculates wave properties from spectral analysis
WaveZerocrossingFun   Calculates wave properties from zero-crossing
PcorFFTFun            Corrects pressure attenuation effect using Fast Fourier transform (FFT)
PcorZerocrossingFun   Corrects pressure attenuation effect using zero-crossing
SeaSwellFun           Separates wind sea and swell
===================   =======================================================================
 
