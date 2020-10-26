Sample Data Files
=================

Two sample data files are provided to be used with OCEANLYZ.
The first file is named “waterpressure_1burst.csv”, and contains one burst of water pressure data recorded with a pressure sensor.
The second file is named “waterpressure_5burst.csv”, and contains five bursts of water pressure data recorded with a pressure sensor.
Data in either of these two files can be used as input data for OCEANLYZ.

Download
--------

Download sample data files:

* waterpressure_1burst.csv: https://github.com/akarimp/oceanlyz/releases/download/2.0/waterpressure_1burst.csv
* waterpressure_5burst.csv: https://github.com/akarimp/oceanlyz/releases/download/2.0/waterpressure_5burst.csv

Properties
----------

Measurement properties for a file named “waterpressure_1burst.csv” are:

===============================================   ========================   ========================
Properties                                        Value                      OCEANLYZ Properties
===============================================   ========================   ========================
File name                                         waterpressure_1burst.csv
Data type                                         Water pressure             obj.InputType='pressure'
Number of recorded burst (n_burst)                1                          obj.n_burst=1
Sampling frequency (fs)                           10 (Hz)                    obj.fs=10
Recording duration (burst_duration)               1024 (second)              obj.burst_duration=1024
Pressure sensor height from bed (heightfrombed)   0.05 (m)                   obj.heightfrombed=0.05
Mean water depth (h)                              1.07 (m)
===============================================   ========================   ========================

Measurement properties for a file named “waterpressure_5burst.csv” are:

===============================================   ========================   ========================
Properties                                        Value                      OCEANLYZ Properties
===============================================   ========================   ========================
File name                                         waterpressure_5burst.csv
Data type                                         Water pressure             obj.InputType='pressure'
Number of recorded burst (n_burst)                5                          obj.n_burst=5
Sampling frequency (fs)                           10 (Hz)                    obj.fs=10
Recording duration (burst_duration)               1024 (second)              obj.burst_duration=1024
Pressure sensor height from bed (heightfrombed)   0.05 (m)                   obj.heightfrombed=0.05
Mean water depth (h)                              Varies in each burst
===============================================   ========================   ========================
