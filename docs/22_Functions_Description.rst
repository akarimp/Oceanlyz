Functions Description
=====================

OCEANLYZ toolbox consists of 1 class and 5 functions.
The main class in OCEANLYZ toolbox is the oceanlyz(). To run OCEANLYZ toolbox, only the oceanlyz() class is required to be run.
Based on parameters set by a user, oceanlyz() calls appropriate function(s) to analyze data.
Note that, any of the OCEANLYZ functions might be used separately as well.

OCEANLYZ requires time-series data which can be in a form of the water depth, water surface elevation, or water pressure.
If a pressure sensor is used for data collection, then data should be corrected for pressure attenuation in the water column. In such cases, only pressure data should be used as an input. In any other cases, either of water depth or water surface elevation time series can be used as an input.


The main class to Run OCEANLYZ toolbox is:

=======================   =======================================================================
Class                     Description
=======================   =======================================================================
``oceanlyz``              Calculate wave properties from water level or water pressure data (This the main class that runs OCEANLYZ)
=======================   =======================================================================

The functions that are used in OCEANLYZ toolbox are:

=======================   =======================================================================
Function                  Description
=======================   =======================================================================
``PcorFFTFun``            Corrects water depth data for pressure attenuation effect using spectral analysis
``PcorZerocrossingFun``   Corrects water depth data for pressure attenuation effect using zero-crossing
``SeaSwellFun``           Partition (separate) wind sea from swell in a power spectral density using an one dimensional method
``WaveSpectraFun``        Calculates wave properties from water surface elevation using spectral analysis
``WaveZerocrossingFun``   Calculates wave properties from water surface elevation using zero-crossing
=======================   =======================================================================
