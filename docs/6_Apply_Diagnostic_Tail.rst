Apply Diagnostic Tail
=====================

A diagnostic tail is used to correct a high frequency section of the wave spectrum. It is not recommended to use a diagnostic tail for measured data, unless data are recorded with a low sampling frequency which leads to no data in higher frequency, or in case that the noise in higher frequency contaminated the data. In these cases, a higher section of the spectrum can be replaced by a diagnostic tail as (Siadatmousavi et al. 2012):

|

:math:`S_{yy}(f)=S_{yy}(f_{tail}) \times (\frac{f}{f_{tail}})^{(-n)}`  for  :math:`f>f_{tail}`

|

where, :math:`S_{yy}(f)` is a water surface elevation power spectral density, f is a frequency, :math:`f_{tail}` is a frequency that a tail applied after that, and n is a power coefficient. The f_tail typically set at 2.5f_m, where :math:`f_m=1/T_{m01}` is a mean frequency (Ardhuin et al. 2010). A value of n depends on deployment conditions, however, typically it is -5 for deep and -3 for shallow water (e.g. Kaihatu et al. 2007, Siadatmousavi et al. 2012).

For more details on this topic refer to Karimpour and Chen (2017) and Karimpour (2018).

