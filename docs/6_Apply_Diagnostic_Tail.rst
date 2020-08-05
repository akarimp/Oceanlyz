Apply Diagnostic Tail
=====================

A diagnostic tail is used to correct a high frequency section of the wave spectrum. It is not recommended to use a diagnostic tail for measured data, unless data are recorded with a low sampling frequency which leads to no data in higher frequency, or in case that the noise in higher frequency contaminated the data. In these cases, a higher section of the spectrum can be replaced by a diagnostic tail as (Siadatmousavi et al. 2012):

|

:math:`S_{yy}(f)=S_{yy}(f_{tail}) \times (\frac{f}{f_{tail}})^{(-n)}`  for  :math:`f>f_{tail}`

|

where, :math:`S_{yy}(f)` is a water surface elevation power spectral density, f is a frequency, :math:`f_{tail}` is a frequency that a tail applied after that, and n is a power coefficient. The f_tail typically set at 2.5f_m, where :math:`f_m=1/T_{m01}` is a mean frequency (Ardhuin et al. 2010). A value of n depends on deployment conditions, however, typically it is -5 for deep and -3 for shallow water (e.g. Kaihatu et al. 2007, Siadatmousavi et al. 2012).

For more details on this topic refer to Karimpour and Chen (2017) and Karimpour (2018).

References
----------

* Ardhuin, F., Rogers, E., Babanin, A. V., Filipot, J. F., Magne, R., Roland, A., ... & Collard, F. (2010). Semiempirical dissipation source functions for ocean waves. Part I: Definition, calibration, and validation. Journal of Physical Oceanography, 40(9), 1917-1941.
* Kaihatu, J. M., Veeramony, J., Edwards, K. L. & Kirby, J. T. 2007 Asymptotic behaviour of frequency and wave number spectra of nearshore shoaling and breaking waves. J. Geophys. Res. 112, C06016
* Karimpour, A., & Chen, Q. (2017). Wind Wave Analysis in Depth Limited Water Using OCEANLYZ, a MATLAB toolbox. Computers & Geosciences, 106,181-189.
* Karimpour A., (2018), Ocean Wave Data Analysis: Introduction to Time Series Analysis, Signal Processing, and Wave Prediction, KDP.
* Siadatmousavi, S. M., Jose, F., & Stone, G. W. (2011). On the importance of high frequency tail in third generation wave models. Coastal Engineering.
