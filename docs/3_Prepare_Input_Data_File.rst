Prepare Input Data File
=======================

This section explains about a format of input data file that is being used in a calculation. An input data file contains a time series of water surface elevation or water depth. An input data file should be prepared as a single file, with only one column. An input data file should not contain any text. Most of file formats such as ".mat", ".txt", ".xlsx", and ".csv" can be imported by the program. The schematics of input data file for data recorded in a burst mode and a continuous mode are demonstrated in following sections. 


Data Recorded in Burst Mode
---------------------------

If data are recorded in a burst mode, then an instrument records data for a specific duration, such as 20 minutes, and then it goes to sleep to save the battery for a predefined duration, such as 60 minutes, before it wakes up again and repeats the recording/sleeping procedure again. Assuming there are M bursts of data, and each burst contains N data points, then a schematic of input data file is:


======================= ===
======================= ===
Burst 1, data point 1
Burst 1, data point 2
Burst 1, data point 3
.
.
.
Burst 1, data point N-2
Burst 1, data point N-1
Burst 1, data point N
Burst 2, data point 1
Burst 2, data point 2
Burst 2, data point 3
.
.
.
Burst 2, data point N-2
Burst 2, data point N-1
Burst 2, data point N
.
.
.
Burst M, data point 1
Burst M, data point 2
Burst M, data point 3
.
.
.
Burst M, data point N-2
Burst M, data point N-1
Burst M, data point N
======================= ===

If data recorded with a sampling frequency of fs, then an input data file has a size of:

(fs * duration of each burst in seconds * total number of recorded bursts , 1)


In this mode, the total number of bursts is M. The total number of samples in each burst is:

N= fs * duration of each burst in seconds


Data Recorded in Continuous Mode:
---------------------------------

If data are recorded in a burst mode, and the total number of recorded data points is equal to N, then a schematic of input data file is:
 

============== ===
============== ===
data point 1
data point 2
data point 3
.
.
.
data point N-2
data point N-1
data point N
============== ===


If data recorded with a sampling frequency of fs for a total duration equal to hr hours, then an input data file has a size of:

(fs * hr * 3600,1)


To define a number of bursts when data are collected in a continuous mode, a length (duration) of each burst should be defined. The total number of bursts is equal to the total duration that data are collected divided by a duration one burst. For example, consider data that were recorded continuously for 24 hours. Now, if 30 minutes of data is selected to represent one burst, then the total number of bursts is equal to the 24 hours divided by 0.5 hour (30 minutes), i.e. (24 / 0.5)=48. In this example, the total number of samples in each burst is (fs * 30 * 60).

