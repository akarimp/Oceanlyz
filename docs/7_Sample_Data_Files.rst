Sample Data Files
=================

Three sample data files are provided to be used with OCEANLYZ:

1. The 3rd file is named "waterlevel_5burst.csv", and contains 5 bursts of synthetic water level data generated from the JONSWAP spectrum in a single column.
2. The 1st file is named "waterpressure_1burst.csv", and contains 1 burst of water pressure data recorded with a pressure sensor in a single column.
3. The 2nd file is named "waterpressure_5burst.csv", and contains 5 bursts of water pressure data recorded with a pressure sensor in a single column.

Data in either of these files can be used as input data for OCEANLYZ.

Download
--------

Download sample data files:

* waterlevel_5burst.csv: https://github.com/akarimp/Oceanlyz/releases/download/2.0/waterlevel_5burst.csv
* waterpressure_1burst.csv: https://github.com/akarimp/Oceanlyz/releases/download/2.0/waterpressure_1burst.csv
* waterpressure_5burst.csv: https://github.com/akarimp/Oceanlyz/releases/download/2.0/waterpressure_5burst.csv

Data and Wave Properties for "waterlevel_5burst.csv" File
------------------------------------------------------------

Measurement properties for a file named "waterlevel_5burst.csv" are:

===============================================   ========================   ========================
Properties                                        Value                      OCEANLYZ Properties
===============================================   ========================   ========================
File name                                         waterlevel_5burst.csv
Data type                                         Water level (m)            obj.InputType='waterlevel'
Number of recorded burst (n_burst)                5                          obj.n_burst=5
Sampling frequency (fs)                           2 (Hz)                     obj.fs=2
Recording duration (burst_duration)               1024 (second)              obj.burst_duration=1024
Mean water depth (h)                              Varies in each burst
===============================================   ========================   ========================

If files "waterlevel_5burst.csv" is used as input data in OCEANLYZ then output results (approximately) would be as follow:

============   =======   ======   =======   ======   ======   ======   ======
Burst Number   Hm0 (m)   Tp (s)   fp (Hz)   Hs (s)   Hz (m)   Tz (s)   Ts (s)
============   =======   ======   =======   ======   ======   ======   ======
Burst 1        0.64      3.01     0.33      0.59     0.39     2.61     2.88
Burst 2        0.59      2.84     0.35      0.53     0.34     2.44     2.71
Burst 3        0.36      2.21     0.45      0.32     0.20     1.94     2.13
Burst 4        0.83      3.28     0.30      0.77     0.48     2.74     3.14
Burst 5        0.47      2.61     0.38      0.41     0.26     2.25     2.49
============   =======   ======   =======   ======   ======   ======   ======

Data and Wave Properties for "waterpressure_1burst.csv" File
------------------------------------------------------------

Measurement properties for a file named "waterpressure_1burst.csv" are:

===============================================   ========================   ========================
Properties                                        Value                      OCEANLYZ Properties
===============================================   ========================   ========================
File name                                         waterpressure_1burst.csv
Data type                                         Water pressure (Pa)        obj.InputType='pressure'
Number of recorded burst (n_burst)                1                          obj.n_burst=1
Sampling frequency (fs)                           10 (Hz)                    obj.fs=10
Recording duration (burst_duration)               1024 (second)              obj.burst_duration=1024
Pressure sensor height from bed (heightfrombed)   0.05 (m)                   obj.heightfrombed=0.05
Mean water depth (h)                              1.07 (m)
===============================================   ========================   ========================

If files "waterpressure_1burst.csv" is used as input data in OCEANLYZ then output results (approximately) would be as follow:

============   =======   ======   =======   ======   ======   ======   ======
Burst Number   Hm0 (m)   Tp (s)   fp (Hz)   Hs (s)   Hz (m)   Tz (s)   Ts (s)
============   =======   ======   =======   ======   ======   ======   ======
Burst 1        0.30      2.84     0.36      0.28     0.19     2.72     2.61
============   =======   ======   =======   ======   ======   ======   ======

Data and Wave Properties for "waterpressure_5burst.csv" File
------------------------------------------------------------

Measurement properties for a file named "waterpressure_5burst.csv" are:

===============================================   ========================   ========================
Properties                                        Value                      OCEANLYZ Properties
===============================================   ========================   ========================
File name                                         waterpressure_5burst.csv
Data type                                         Water pressure (Pa)        obj.InputType='pressure'
Number of recorded burst (n_burst)                5                          obj.n_burst=5
Sampling frequency (fs)                           10 (Hz)                    obj.fs=10
Recording duration (burst_duration)               1024 (second)              obj.burst_duration=1024
Pressure sensor height from bed (heightfrombed)   0.05 (m)                   obj.heightfrombed=0.05
Mean water depth (h)                              Varies in each burst
===============================================   ========================   ========================

If files "waterpressure_5burst.csv" is used as input data in OCEANLYZ then output results (approximately) would be as follow:

============   =======   ======   =======   ======   ======   ======   ======
Burst Number   Hm0 (m)   Tp (s)   fp (Hz)   Hs (s)   Hz (m)   Tz (s)   Ts (s)
============   =======   ======   =======   ======   ======   ======   ======
Burst 1        0.32      2.84     0.35      0.29     0.20     2.68     2.62
Burst 2        0.33      2.84     0.35      0.30     0.21     2.72     2.67
Burst 3        0.35      2.84     0.35      0.32     0.22     2.69     2.67
Burst 4        0.35      3.01     0.33      0.31     0.21     2.79     2.82
Burst 5        0.36      3.01     0.34      0.33     0.23     2.84     2.68
============   =======   ======   =======   ======   ======   ======   ======

Parameters
----------

Hm0
    Zero-moment wave height (m)
Tp
    Peak wave period (s)
fp
    Peak wave frequency (Hz)
Hs
    Significant wave height (m)
Hz
    Zero-crossing mean wave height (m)
Tz
    Zero-crossing mean wave period (s)
Ts
    Significant wave period (s)
