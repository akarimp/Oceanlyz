Getting Started
===============

In order to use OCEANLYZ toolbox, first, one of the MATLAB or GNU Octave programming language should be installed with required packages (Refer to required packages for MATLAB/GNU Octave). 

Then, the OCEANLYZ toolbox should be downloaded and unzip in a folder of your choice. For example, if the OCEANLYZ is unzipped on C: derive, then OCEANLYZ folder would be “C:\oceanlyz” on a windows machine.

Before using the Oceanlyz, these steps should be followed first:

1. Setting values representing the properties of the dataset needs to be analyzed
2. Defining what type of analysis is required to be done
3. Preparing dataset in a format that the OCEANLYZ can use

These steps are explained in detail in following sections. 


Set up Input, Output, and Calculation parameters
------------------------------------------------

Values that define input, output, and calculation parameters are defined in a file named “oceanlyzinput.m”. To set up these parameters, first, open file “oceanlyzinput.m” by following these steps:

* Open MATLAB or GNU Octave
* Change a current folder (current directory) to a folder that contains OCEANLYZ toolbox in MATLAB or GNU Octave. For example, open “C:\oceanlyz” directory.
* Open a file named “oceanlyzinput.m” in MATLAB or GNU Octave editor and modify it based on the properties of the collected dataset and required analysis. 

Parameters that can be defined in “oceanlyzinput.m” are described in following.


Input, Output, and Calculation Parameters
-----------------------------------------

**InputFileName**
    It defines a name of the input data file

    Notes:
        Enter name of the file contains water depth or surface elevation (Eta) time series.

        Data should be in a single column vector file without any text, each burst of data should follow the previous burst.

        Most file formats such as '.mat', '.txt', '.csv' can be imported.

    Example: 
        InputFileName='waterdepthsample.mat';

**InputFileFolder**
    It defines a location of the input data file

    Notes:
        Enter a location of the file contains water depth or surface elevation (Eta) time series.

        For Linux or Mac, use '/' instead of '\\'

    Example:
        InputFileFolder='C:\\oceanlyz\\Sample';

**SaveOutput**
    It defines if to save output(s) and a location the output(s) to be saved

        SaveOutput='off';     :Does not save output(s)
        
        SaveOutput='on';     :Save output(s)

**OutputFileFolder**
    Location of the output file to be saved

        OutputFileFolder='C:\\oceanlyz';

    Notes:
        For Linux or Mac, use '/' instead of '\\'.

        Output is a structure array

        Name of output file is 'wave.mat'

        After wave.mat is loaded in Matlab, field(s) in structure array can be called by using '.'

    Example: Output peak wave period is : "wave.Tp"

**AnalysisMethod**
    It defines analysis method

        AnalysisMethod='spectral';     :Use spectral analysis method / Fast Fourier Transform
        
        AnalysisMethod='zerocross';     :Use zero-crossing method

**WaveParameterCalc**
    It defines if to calculate wave parameters or not

        WaveParameterCalc='off';     :Does not calculate/report wave properties
        
        WaveParameterCalc='on';     :Calculates/reports wave properties

    Notes:
        Use WaveParameterCalc='off' to only report corrected water level data measured by a pressure sensor.

        If WaveParameterCalc='off', then pressureattenuation should be pressureattenuation='on' or 'all'.

        If WaveParameterCalc='off', it reports corrected water level data measured by a pressure sensor.

        by accounting for pressure attenuation (pressure loss) in depth.

        If WaveParameterCalc='on' and pressureattenuation='on' or 'all', it reports both waves and corrected water level data measured by a pressure sensor.

**burst**
    it defines number of burst(s) in the input file 

        burst=5;     :Number of burst(s) in the input file

    Notes:
        burst=total number of data points/(duration*fs).

    Example: 
        For 12 bursts of data, which each burst has a duration of 30 minutes, and collected at sampling frequency of 10 Hz:

        duration=(30*60)

        total number of data points = number of burst * duration of each burst * sampling frequency = 12*(30*60)*10

**duration**
    it defines duration time that data collected in each burst in (second)

        duration=1024;     :Duration time that data collected in each burst in (second)

**fs**
    It defines sampling frequency that data are collected at in (Hz)

        fs=10;     :Sampling frequency that data are collected at in (Hz)

**heightfrombed**
    It defines pressure sensor height from a bed in (m)

        heightfrombed=0.05;     :Pressure sensor height from a bed in (m)

    Notes:
        Leave heightfrombed=0.0; if data is not measured by a pressure sensor or if a sensor sits on the seabed.

**nfft**
    It defines NFFT for Fast Fourier Transform

        nfft=2^10;     :NFFT for Fast Fourier Transform

    Notes:
        Results will be reported for frequency range of 0 <= f <= (fs/2) with (nfft/2+1) data points.

    Example: 
        If fs=4 Hz and nfft=1024, then output frequency has a range of 0 <= f <= 2 with 513 data points.

**seaswellCalc**
    it defines if to separate wind sea and swell waves or not

        seaswellCalc='off';     :Does not separate wind sea and swell waves
        
        seaswellCalc='on';     :Separates wind sea and swell waves

**fminswell**
    It defines minimum frequency that swell can have

        fminswell=0.1;     :Minimum frequency that swell can have (it is used for Tpswell calculation) in (Hz)

**fmaxswell**
    It defines maximum frequency that swell can have

        fmaxswell=0.25;     :Maximum frequency that swell can have (It is about 0.2 in Gulf of Mexico) in (Hz)

**pressureattenuation**
    It defines if to apply pressure attenuation factor or not

        pressureattenuation='off';     :No pressure attenuation is applied
        
        pressureattenuation='on';     :Pressure attenuation is applied without correction after fmaxpcorr
        
        pressureattenuation='all';     :Pressure attenuation is applied with constant correction after fmaxpcorr

    Notes:
        Pressure attenuation factor is used to account for pressure attenuation (pressure loss) in depth.

        For pressureattenuation='on' or 'all', input data should be water depth.

**autofmaxpcorr**
    It defines if to calculate fmaxpcorr and ftailcorrection based on water depth or not

        autofmaxpcorr='off':     :Does not calculate fmaxpcorr and ftailcorrection based on water depth
        
        autofmaxpcorr='on':     :Calculate fmaxpcorr and ftailcorrection based on water depth

    Notes:
        Code calculate a maximum frequency that a pressure attenuation factor should be applied up to that.

**fminpcorr**
    It defines minimum frequency that automated calculated fmaxpcorr can have if autofmaxpcorr='on' in (Hz)

        fminpcorr=0.15;     :Minimum frequency that automated calculated fmaxpcorr can have if autofmaxpcorr='on' in (Hz)

    Notes:
        If autofmaxpcorr='on', then fmaxpcorr will be checked to be larger or equal to fminpcorr.

**fmaxpcorr**
    It defines maximum frequency for applying pressure attenuation factor in (Hz)

        fmaxpcorr=0.55;     :Maximum frequency for applying pressure attenuation factor in (Hz)

    Notes:
        Pressure attenuation factor is not applied on frequency larger than fmaxpcorr.

**mincutoff**
    It defines if to cut off the spectrum below fmin, i.e. where f<fmin, or not

        mincutoff='off';     : Does not cut off spectrum below fmin
    
    mincutoff='on';     : Cuts off spectrum below fmin

**fmin**
    It defines minimum frequency to cut off the lower part of spectrum in (Hz)

        fmin=0.04;     :Minimum frequency to cut off the lower part of spectrum in (Hz)

    Notes:
        If mincutoff='on', then results with frequency f<fmin will be removed from analysis.

        It is a simple high pass filter.

**maxcutoff**
    It defines if to cut off the spectrum beyond fmax, i.e. where f>fmax, or not

        maxcutoff='off';     : Does not cut off spectrum beyond fmax
        
        maxcutoff='on';     : Cut off spectrum beyond fmax

**fmax**
    It defines maximum frequency to cut off the upper part of spectrum in (Hz)

        fmax=1;     :Maximum frequency to cut off the upper part of spectrum in (Hz)

    Notes:
        If maxcutoff='on', then results with frequency f>fmax will be removed from analysis.

        It is a simple low pass filter.

**tailcorrection**
    It defines if to apply diagnostic tail correction or not

        tailcorrection='off';     :Does not apply diagnostic tail
        
        tailcorrection='jonswap';     :Applies JONSWAP Spectrum tail
        
        tailcorrection='tma';     :Applies TMA Spectrum tail

    Notes:
        For tailcorrection='tma', input data should be water depth.

**ftailcorrection**
    It defines frequency that diagnostic tail applies after that in (Hz)

        ftailcorrection=0.9;     :Frequency that diagnostic tail applies after that in (Hz)

    Notes:
        ftailcorrection is typically set at 2.5fm where fm=1/Tm01.

**tailpower**
    It defines power that a diagnostic tail will be applied based on that

        tailpower=-5;     :Power that a diagnostic tail will be applied based on that 

    Notes:
        Diagnostic tail will be proportional with (f^tailpower).

        tailpower=-3 for shallow water, tailpower=-5 for deep water.

**dispout**
    It defines if to plot spectrum or not

        dispout='off';     :Does not plot
        
        dispout='on';     :Plot


Required Parameters for Spectral Analysis
-----------------------------------------

All parameters mentioned in a previous section might be required for the spectral analysis (depending on which module is on or off). In other words, if AnalysisMethod='spectral'; then all mentioned parameters above might be required. If a parameter is not required, it is ignored by OCEANLYZ if defined.

Required Parameters for Zero-Crossing Method
--------------------------------------------

Not all parameters mentioned in previous section are required for the zero-crossing method. If AnalysisMethod= 'zerocross'; then only following parameters are required. All other parameters, if defined, are ignored by Oceanlyz.

.. code:: MATLAB

    InputFileName='waterdepthsample.mat';
    InputFileFolder=pwd;
    SaveOutput='on'; 
    OutputFileFolder=pwd;
    AnalysisMethod='spectral';
    WaveParameterCalc='on';
    burst=1;
    duration=1024;
    fs=1;
    heightfrombed=0.0;
    pressureattenuation='off'; 
    dispout='off';


Default Values for Input, Output, and Calculation Parameters
------------------------------------------------------------

Default values are set as follow:

.. code:: MATLAB

    InputFileName='waterdepthsample.mat';
    InputFileFolder=pwd;
    SaveOutput='on'; 
    OutputFileFolder=pwd;
    AnalysisMethod='spectral';
    WaveParameterCalc='on';
    burst=1;
    duration=1024;
    fs=1;
    heightfrombed=0.0;
    nfft=2^10;
    seaswellCalc='off';
    fminswell=0.1;
    fmaxswell=0.25;
    pressureattenuation='off'; 
    autofmaxpcorr='off';
    fminpcorr=0.15;
    fmaxpcorr=0.55;
    mincutoff='off';
    fmin=0.05;
    maxcutoff='off';
    fmax=fs/2;
    tailcorrection='off'; 
    ftailcorrection=0.9;
    tailpower=-5; 
    dispout='off';


Run OCEANLYZ
------------

To run OCEANLYZ follow these steps:


* Open MATLAB or GNU Octave.
* Change a current folder (current directory) to a folder that contains OCEANLYZ toolbox inside MATLAB or GNU Octave. For example, open “C:\oceanlyz” directory.
* Run a file named “RunOceanlyz.m” in MATLAB or GNU Octave to start calculations. 


Outputs
-------

Output(s) of the wave properties are reported based on the selected parameters as a structure array named "wave". Field(s) in the structure array "wave" can be called by using ".". For example, an output a peak period is "wave.Tp", an output for zero-moment wave height is "wave.Hm0", and an output for a water surface elevation power spectral density is "wave.Syy".

In general, output(s) for each time step (each burst) is reported in one row. For example, if an input file contains 5 bursts of data, then outputs has 5 rows, each row contains output for one burst. For this example, wave.Tp(1,1) or wave.Syy(1,:) are outputs for the first burst. Similarly, wave.Tp(5,1) or wave.Syy(5,:) are outputs for the fifth burst.

If SaveOutput='on', then the output(s) is saved in a file named "wave.mat" as a structure array in a folder defined by OutputFileFolder.


Notes
-----

Note1: 
    If data are collected in continuous mode you can choose burst and duration as follow:

    Duration is equal to a period of time that you want data averaged over that. For example, if you need wave properties reported every 15 min, then the duration would be 15*60 second

    Burst is equal to the total length of the time series divided by the duration. Burst should be a rounded number. So, if the total length of the time series divided by the duration leads to a decimal number, then data should be shortened to avoid that.

Note2: 
    In a calculation, NFFT value that is set in “oceanlyzinput.m” file will be used. However, a user can set NFFT to be calculated automatically. This should be done inside each function. In that case, NFFT will be set equal to the smallest power of two that is larger than or equal to the absolute value of the total number of data points in each burst. This should be done manually inside each function.

Note3: 
    Welch spectrum is used to calculate a power spectral density. In all spectral calculation, a default window function with a default overlap window between segments is used. If any other values are required, it should be changed manually inside each function.

Note4: 
    If autofmaxpcorr='on', then the package calculates fmaxpcorr and ftailcorrection based on water depth and a sensor height from seabed (refer to Applying Pressure Response Factor section). A maximum value for calculated fmaxpcorr and ftailcorrection will be limited to the ones user set in “oceanlyzinput.m” file.  

