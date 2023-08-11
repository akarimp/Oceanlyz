Functions List
==============

OCEANLYZ toolbox consists of 1 class and 5 functions.
The main class in OCEANLYZ toolbox is the ``oceanlyz()``. To run OCEANLYZ toolbox, only the ``oceanlyz()`` class is required to be run.
Based on parameters set by a user, ``oceanlyz()`` calls appropriate function(s) to analyze data.
Note that, any of the OCEANLYZ functions might be used separately as well.

OCEANLYZ requires time-series data which can be in a form of the water depth, water surface elevation, or water pressure.
If a pressure sensor is used for data collection, then data should be corrected for pressure attenuation in the water column. In such cases, only pressure data should be used as an input. In any other cases, either of water depth or water surface elevation time series can be used as an input.

The class and functions that are used in OCEANLYZ toolbox are:

=======================   ========   =======================================================================
Function                  Type       Description
=======================   ========   =======================================================================
``oceanlyz``              Class      Calculate wave properties from water level or water pressure data (This is the main class to run OCEANLYZ toolbox)
``PcorFFTFun``            Function   Corrects water depth data for pressure attenuation effect using spectral analysis
``PcorZerocrossingFun``   Function   Corrects water depth data for pressure attenuation effect using zero-crossing
``SeaSwellFun``           Function   Partition (separate) wind sea from swell in a power spectral density using an one dimensional method
``WaveSpectraFun``        Function   Calculates wave properties from water surface elevation using spectral analysis
``WaveZerocrossingFun``   Function   Calculates wave properties from water surface elevation using zero-crossing
=======================   ========   =======================================================================

Functions (MATLAB)
------------------

.. toctree::
    :maxdepth: 1

    matlab_functions/oceanlyz.rst
    matlab_functions/PcorFFTFun.rst
    matlab_functions/PcorZerocrossingFun.rst
    matlab_functions/SeaSwellFun.rst
    matlab_functions/WaveSpectraFun.rst
    matlab_functions/WaveZerocrossingFun.rst

Functions (Python)
------------------

.. toctree::
    :maxdepth: 1
    
    python_functions/oceanlyz.rst
    python_functions/PcorFFTFun.rst
    python_functions/PcorZerocrossingFun.rst
    python_functions/SeaSwellFun.rst
    python_functions/WaveSpectraFun.rst
    python_functions/WaveZerocrossingFun.rst
