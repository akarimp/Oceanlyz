Changelog (MATLAB and Python)
=============================

Version 2.0
-----------

What is new in ver 2.0:

* From version 2.0, in addition to MATLAB and GNU Octave, OCEANLYZ is available for Python language through OCEANLYZ package
* From version 2.0, OCEANLYZ is a class (instead of function). It allows OCEANLYZ to be called inside user code.
* Bug fix (MATLAB): remove 'obj' as an input arguments from oceanlyzmodule() and oceanlyzecalcwave() methods (2021-07-08)
* Bug fix: removed '/(Rho*1000)' from mean water depth calculation in oceanlyzecalcwave() method (2021-08-03)
* Bug fix (Python): removed -1 from index of if autofmaxpcorr=='on': in PcorFFTFun function (2021-08-07)
* Bug fix : Add 'if tailcorrection=='jonswap' or tailcorrection=='tma':' in WaveSpectraFun and SeaSwellFun functions (2021-10-26)
* Release date: 2020-10-27

Version 1.5
-----------

What is new in ver 1.5:

* Now, a wave spectrum in PcorFFTFun function is obtained from pwelch function instead of fft function
* Parameter 'burst' changed to 'n_burst'
* Parameter 'duration' changed to 'burst_duration'
* Release date: 2020-8-5

Version 1.4
-----------

What is new in ver 1.4:

* Now, OCEANLYZ can be run on both Matlab and GNU Octave
* ​Now, a separate input file is used to define calculation parameters
* Wavenumber calculation performance is improved 
* TMA diagnostic tail is improved
* User manual is re-written
* Release date: 2018-6-22

Version 1.3
-----------

What is new in ver 1.3:

* Tail correction for spectral analysis is improved
* Correcting pressure data for pressure attenuation is improved
* Sea/Swell partitioning is improved 
* Release date: 2017-6-27

Version 1.2
-----------

What is new in ver 1.2:

* The NFFT now can be assigned as an input.
* Automatic calculation of the upper limit frequency for the dynamic pressure corrections added.
* Zero-Crossing method modified.
* Mean water level calculation modified.
* Significant wave period added.
* Calculation of peak wave frequency based on the weighted integral added.
* Parameter notations are updated.
* Release date: 2014-12

Version 1.1
-----------

What is new in ver 1.1:

* Initial version of OCEANLYZ is released
* Release date: 2013-12
