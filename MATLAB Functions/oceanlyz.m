classdef oceanlyz < handle
%{
.. ++++++++++++++++++++++++++++++++YA LATIF++++++++++++++++++++++++++++++++++
.. +                                                                        +
.. + Oceanlyz                                                               +
.. + Ocean Wave Analyzing Toolbox                                           +
.. + Ver 2.0                                                                +
.. +                                                                        +
.. + Developed by: Arash Karimpour                                          +
.. + Contact     : www.arashkarimpour.com                                   +
.. + Developed/Updated (yyyy-mm-dd): 2020-08-01                             +
.. +                                                                        +
.. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

oceanlyz (MATLAB Version)
=========================

.. code:: MATLAB

    oceanlyz_object = oceanlyz

DESCRIPTION
-----------

| Calculate wave properties from water level or water pressure data
| For OCEANLYZ Document visit https://oceanlyz.readthedocs.io

Required Properties
-------------------

Following properties are required for all analysis

data=[];
    Water level (water surface elevation, Eta), water depth, or water pressure time series
        | Data should be a single column array (column vector) without any text
        | Each burst of data should follow the previous burst without any void

InputType='waterlevel';
    Define input data type
        InputType='waterlevel': Input data is water level or water depth in (m)
            If InputType='waterlevel' then OutputType='wave'
        InputType='pressure': Input data are water pressure measured by a pressure sensor at sensor depth in (N/m^2)
            If InputType='pressure' then OutputType='waterlevel' or OutputType='wave+waterlevel'

OutputType='wave';
    Define output data type
        | OutputType='wave': Calculate wave properties from water level or water depth data
        | OutputType='waterlevel': Calculate water level data from water pressure data measured by a pressure sensor
        | OutputType='wave+waterlevel': Calculate waves properties and water level data from water pressure data measured by a pressure sensor

AnalysisMethod='spectral';
    Analysis method
        | AnalysisMethod='spectral': Use spectral analysis method / Fast Fourier Transform
        | AnalysisMethod='zerocross': Use zero-crossing method

n_burst=1;
    Number of burst(s) in the input file
        | n_burst = (total number of data points)/(burst_duration*fs)
        | Example:

            | Assume data are collected for 6 hours at a sampling frequency of fs=10 Hz
            | If data are analyzed at intervals of 30 minutes then there are 12 bursts (6 hours/30 minutes=12 bursts)
            | For 12 bursts of data, which each burst has a duration of 30 minutes, and collected at sampling frequency of fs=10 Hz 
            | burst_duration=(30 min * 60) = 1800 seconds
            | total number of data points=(number of burst)*(duration of each burst)*(sampling frequency)
            | total number of data points=(n_burst)*(burst_duration)*(fs)
            | total number of data points=12 * 1800 * 10

burst_duration=1024;
    Duration time that data collected in each burst in (second)

fs=2;
    Sampling frequency that data are collected at in (Hz)

Required Properties for Spectral Analysis
-----------------------------------------

Following properties are needed only if AnalysisMethod='spectral'

fmin=0.05;
    Minimum frequency to cut off the spectrum below that, i.e. where f<fmin, in (Hz)
        | Results with frequency f<fmin will be removed from analysis
        | It should be between 0 and (fs/2)
        | It is a simple high pass filter
        | Only required if AnalysisMethod='spectral'

fmax=1e6;
    Maximum frequency to cut off the spectrum beyond that, i.e. where f>fmax, in (Hz)
        | Results with frequency f>fmax will be removed from analysis
        | It should be between 0 and (fs/2)
        | It is a simple low pass filter
        | Only required if AnalysisMethod='spectral'

Required Properties for Pressure Data Analysis
----------------------------------------------

Following properties are needed only if InputType='pressure'

fmaxpcorrCalcMethod='auto';
    Define if to calculate fmaxpcorr and ftail or to use user defined
        | fmaxpcorrCalcMethod='user': use user defined value for fmaxpcorr
        | fmaxpcorrCalcMethod='auto': automatically define value for fmaxpcorr
        | Only required if InputType='pressure' and AnalysisMethod='spectral'

Kpafterfmaxpcorr='constant';
    Define a pressure response factor, Kp, value for frequency larger than fmaxpcorr
        | Kpafterfmaxpcorr='one': Kp=1 for frequency larger than fmaxpcorr 
        | Kpafterfmaxpcorr='constant': Kp for f larger than fmaxpcorr stays equal to Kp at fmaxpcorr (constant)
        | Kpafterfmaxpcorr='nochange': Kp is not changed for frequency larger than fmaxpcorr (Not implemented yet)
        | Only required if InputType='pressure' and AnalysisMethod='spectral'

fminpcorr=0.15;
     Minimum frequency that automated calculated fmaxpcorr can have if fmaxpcorrCalcMethod='auto' in (Hz)
        | If fmaxpcorrCalcMethod='auto', then fmaxpcorr will be checked to be larger or equal to fminpcorr
        | It should be between 0 and (fs/2)
        | Only required if InputType='pressure' and AnalysisMethod='spectral'

fmaxpcorr=0.55;
    Maximum frequency for applying pressure attenuation factor in (Hz)
        | Pressure attenuation factor is not applied on frequency larger than fmaxpcorr
        | It should be between 0 and (fs/2)
        | Only required if InputType='pressure' and AnalysisMethod='spectral'

heightfrombed=0.0;
    Pressure sensor height from a bed in (m)
        Leave heightfrombed=0.0 if data are not measured by a pressure sensor or if a sensor sits on the seabed
        | Only required if InputType='pressure'

Optional Properties
-------------------

Following properties are optional

dispout='no';
    Define if to plot spectrum or not
        | dispout='no': Does not plot
        | dispout='yes': Plot

Rho=1000;
    Water density (kg/m^3)
        Only required if InputType='pressure'

nfft=512;
    Define number of data points in discrete Fourier transform
        | Should be 2^n
        | Results will be reported for frequency range of 0 <= f <= (fs/2) with (nfft/2+1) data points
        | Example: If fs=4 Hz and nfft=512, then output frequency has a range of 0 <= f <= 2 with 257 data points
        | Only required if AnalysisMethod='spectral'

SeparateSeaSwell='no';
    Define if to separate wind sea and swell waves or not
        | SeparateSeaSwell='no': Does not separate wind sea and swell waves
        | SeparateSeaSwell='yes': Separates wind sea and swell waves

fmaxswell=0.25;
    Maximum frequency that swell can have (It is about 0.2 in Gulf of Mexico) in (Hz)
        | It should be between 0 and (fs/2)
        | Only required if SeparateSeaSwell='yes' and AnalysisMethod='spectral'

fpminswell=0.1;
    Minimum frequency that swell can have (it is used for Tpswell calculation) in (Hz)
        | It should be between 0 and (fs/2)
        | Only required if SeparateSeaSwell='yes' and AnalysisMethod='spectral'

tailcorrection='off';
    Define if to replace spectrum tail with tail of empirical spectrum (diagnostic tail) or not 
        | tailcorrection='off': Does replace spectrum tail
        | tailcorrection='jonswap': Replace spectrum tail with JONSWAP Spectrum tail
        | tailcorrection='tma': Replace spectrum tail with TMA Spectrum tail

            For tailcorrection='tma', input data should be water depth

ftailcorrection=0.9;
    Frequency that spectrum tail replaced after that in (Hz)
        | ftailcorrection is typically set at ftailcorrection=(2.5*fm) where (fm=1/Tm01)
        | It should be between 0 and (fs/2)
        | Only required if SeparateSeaSwell='yes' and tailcorrection='jonswap' or tailcorrection='tma'

tailpower=-5;
    Power that a replaced tail (diagnostic tail)
        | Replaced tail (diagnostic tail) will be proportional to (f^tailpower)
        | Recommendation: use tailpower=-3 for shallow water and tailpower=-5 for deep water
        | Only required if SeparateSeaSwell='yes' and tailcorrection='jonswap' or tailcorrection='tma'

Methods
-------

oceanlyz_object.runoceanlyz()
    Run oceanlyz and calculate wave properties

Outputs
-------

oceanlyz_object.wave
    Calculated wave properties as a structure array
        | Output is a structure array
        | Name of output is 'oceanlyz_object.wave'
        | Field(s) in this structure array can be called by using '.'
        | Example:

            | oceanlyz_object.wave.Hm0         : Contain zero-moment wave height
            | oceanlyz_object.wave.Tp          : Contain peak wave period
            | oceanlyz_object.wave.Field_Names : Contain field (variable) names in the wave array
            | oceanlyz_object.wave.Burst_Data  : Contain data for each burst

Examples
--------

.. code:: MATLAB

    %Change current working directory to OCEANLYZ folder
    %Assume OCEANLYZ files are in 'C:\oceanlyz_matlab' folder
    cd('C:\oceanlyz_matlab')

    %Create OCEANLYZ object
    %clear ocn %Optional
    ocn=oceanlyz;
    
    %Read data
    %Assume data file is named 'waterpressure_5burst.csv' and is stored in 'C:\oceanlyz_matlab\Sample_Data'
    current_folder=pwd;                  %Current (OCEANLYZ) path
    cd('C:\oceanlyz_matlab\Sample_Data') %Change current path to Sample_Data folder
    water_pressure=importdata('waterpressure_5burst.csv'); %Load data
    cd(current_folder)                   %Change current path to OCEANLYZ folder
    
    %Input parameters
    ocn.data=water_pressure;
    ocn.InputType='pressure';
    ocn.OutputType='wave+waterlevel';
    ocn.AnalysisMethod='spectral';
    ocn.n_burst=5;
    ocn.burst_duration=1024;
    ocn.fs=10;
    ocn.fmin=0.05;                    %Only required if ocn.AnalysisMethod='spectral'
    ocn.fmax=ocn.fs/2;                %Only required if ocn.AnalysisMethod='spectral'
    ocn.fmaxpcorrCalcMethod='auto';   %Only required if ocn.InputType='pressure' and ocn.AnalysisMethod='spectral'
    ocn.Kpafterfmaxpcorr='constant';  %Only required if ocn.InputType='pressure' and ocn.AnalysisMethod='spectral'
    ocn.fminpcorr=0.15;               %Only required if ocn.InputType='pressure' and ocn.AnalysisMethod='spectral'
    ocn.fmaxpcorr=0.55;               %Only required if ocn.InputType='pressure' and ocn.AnalysisMethod='spectral'
    ocn.heightfrombed=0.05;           %Only required if ocn.InputType='pressure' and ocn.AnalysisMethod='spectral'
    ocn.dispout='yes';
    ocn.Rho=1024;                     %Seawater density (Varies)

    %Run OCEANLYZ
    ocn.runoceanlyz()

    %Plot peak wave period (Tp)
    plot(ocn.wave.Tp(1,:))

References
----------

Karimpour, A., & Chen, Q. (2017).
Wind wave analysis in depth limited water using OCEANLYZ, A MATLAB toolbox.
Computers & Geosciences, 106, 181-189.

.. License & Disclaimer
.. --------------------
..
.. Copyright (c) 2020 Arash Karimpour
..
.. http://www.arashkarimpour.com
..
.. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
.. IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
.. FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
.. AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
.. LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
.. OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
.. SOFTWARE.
%}

%--------------------------------------------------------------------------
%CODE
%--------------------------------------------------------------------------
    properties
        
        %Assign default values

        %--------------------
        %Setup input and output data
        %--------------------

        %Inut data
        data=[];
        %                                 Water level (water surface elevation, Eta), water depth, or water pressure time series
        %                                     Data should be a single column array (column vector) without any text
        %                                     Each burst of data should follow the previous burst without any void

        %Output data
        wave=[];
        %Calculated wave properties as a structure array
        %                                 Output is a structure array
        %                                 Name of output is 'oceanlyz_object.wave'
        %                                 Field(s) in this structure array can be called by using '.'
        %                                 Example:
        %
        %                                     oceanlyz_object.wave.Hm0         : Contain zero-moment wave height
        %                                     oceanlyz_object.wave.Tp          : Contain peak wave period
        %                                     oceanlyz_object.wave.Field_Names : Contain field (variable) names in the wave array
        %                                     oceanlyz_object.wave.Burst_Data  : Contain data for each burst

        %Define input data type
        InputType='waterlevel';
        %                                 Define input data type
        %                                     InputType='waterlevel': Input data is water level or water depth in (m)
        %                                         If InputType='waterlevel' then OutputType='wave'
        %                                     InputType='pressure': Input data are water pressure measured by a pressure sensor at sensor depth in (N/m^2)
        %                                         If InputType='pressure' then OutputType='waterlevel' or OutputType='wave+waterlevel'

        %Define output data type
        OutputType='wave';
        %                                 Define output data type
        %                                     OutputType='wave': Calculate wave properties from water level or water depth data
        %                                     OutputType='waterlevel': Calculate water level data from water pressure data measured by a pressure sensor
        %                                     OutputType='wave+waterlevel': Calculate waves properties and water level data from water pressure data measured by a pressure sensor

        %--------------------
        %Setup analysis method
        %--------------------

        %Define analysis method
        AnalysisMethod='spectral';
        %                                 Analysis method
        %                                     AnalysisMethod='spectral': Use spectral analysis method / Fast Fourier Transform
        %                                     AnalysisMethod='zerocross': Use zero-crossing method

        %--------------------
        %Setup measurement properties of input data
        %--------------------
        
        %Number of burst(s)
        n_burst=1;
        %                                 Number of burst(s) in the input file
        %                                     n_burst = (total number of data points)/(burst_duration*fs)
        %                                     Example: 
        %                                         Assume data are collected for 6 hours at a sampling frequency of fs=10 Hz
        %                                         If data are analyzed at intervals of 30 minutes then there are 12 bursts (6 hours/30 minutes=12 bursts)
        %                                         For 12 bursts of data, which each burst has a duration of 30 minutes, and collected at sampling frequency of fs=10 Hz 
        %                                         burst_duration=(30 min * 60) = 1800 seconds
        %                                         total number of data points=(number of burst)*(duration of each burst)*(sampling frequency)
        %                                         total number of data points=(n_burst)*(burst_duration)*(fs)
        %                                         total number of data points=12 * 1800 * 10
        
        %Duration of each burst
        burst_duration=1024;
        %                                 Duration time that data collected in each burst in (second)
        
        %Sampling frequency
        fs=2;
        %                                 Sampling frequency that data are collected at in (Hz)

        %--------------------
        %Frequency setup if spectral analysis is used
        %--------------------
        
        %Minimum frequency used in spectral analysis
        fmin=0.05;
        %                                 Minimum frequency to cut off the spectrum below that, i.e. where f<fmin, in (Hz)
        %                                     Results with frequency f<fmin will be removed from analysis
        %                                     It should be between 0 and (fs/2)
        %                                     It is a simple high pass filter
        %                                     Only required if AnalysisMethod='spectral'

        %Maximum frequency used in spectral analysis
        fmax=1e6;
        %                                 Maximum frequency to cut off the spectrum beyond that, i.e. where f>fmax, in (Hz)
        %                                     Results with frequency f>fmax will be removed from analysis
        %                                     It should be between 0 and (fs/2)
        %                                     It is a simple low pass filter
        %                                     Only required if AnalysisMethod='spectral'

        %--------------------
        %Calculation setup if input is pressure
        %--------------------
        
        %fmaxpcorr calculation method
        fmaxpcorrCalcMethod='auto';
        %                                 Define if to calculate fmaxpcorr and ftail or to use user defined
        %                                     fmaxpcorrCalcMethod='user': use user defined value for fmaxpcorr
        %                                     fmaxpcorrCalcMethod='auto': automatically define value for fmaxpcorr
        %                                     Only required if InputType='pressure' and AnalysisMethod='spectral'
        
        %Pressure response factor for kp>fmaxpcorr
        Kpafterfmaxpcorr='constant';
        %                                 Define a pressure response factor, Kp, value for frequency larger than fmaxpcorr
        %                                     Kpafterfmaxpcorr='one': Kp=1 for frequency larger than fmaxpcorr 
        %                                     Kpafterfmaxpcorr='constant': Kp for f larger than fmaxpcorr stays equal to Kp at fmaxpcorr (constant)
        %                                     Kpafterfmaxpcorr='nochange': Kp is not changed for frequency larger than fmaxpcorr (Not implemented yet)
        %                                     Only required if InputType='pressure' and AnalysisMethod='spectral'

        %Minimume value of fmaxpcorr
        fminpcorr=0.15;
        %                                 Minimum frequency that automated calculated fmaxpcorr can have if fmaxpcorrCalcMethod='auto' in (Hz)
        %                                     If fmaxpcorrCalcMethod='auto', then fmaxpcorr will be checked to be larger or equal to fminpcorr
        %                                     It should be between 0 and (fs/2)
        %                                     Only required if InputType='pressure' and AnalysisMethod='spectral'
        
        %Maximum frequency to apply a pressure response
        fmaxpcorr=0.55;
        %                                 Maximum frequency for applying pressure attenuation factor in (Hz)
        %                                     Pressure attenuation factor is not applied on frequency larger than fmaxpcorr
        %                                     It should be between 0 and (fs/2)
        %                                     Only required if InputType='pressure' and AnalysisMethod='spectral'
        
        %Pressure sensor height from water bed
        heightfrombed=0.0;
        %                                 Pressure sensor height from a bed in (m)
        %                                     Leave heightfrombed=0.0 if data are not measured by a pressure sensor or if a sensor sits on the seabed
        %                                     Only required if InputType='pressure'

        %--------------------
        %Display setup
        %--------------------

        %Display results
        dispout='no';
        %                                 Define if to plot spectrum or not
        %                                     dispout='no': Does not plot
        %                                     dispout='yes': Plot

        %--------------------
        %Setup NFFT and Rho
        %--------------------

        Rho=1000;
        %                                 Water density (kg/m^3)
        %                                     Only required if InputType='pressure'
    
        nfft=512;
        %                                 Define number of data points in discrete Fourier transform
        %                                     Should be 2^n
        %                                     Results will be reported for frequency range of 0 <= f <= (fs/2) with (nfft/2+1) data points
        %                                     Example: If fs=4 Hz and nfft=512, then output frequency has a range of 0 <= f <= 2 with 257 data points
        %                                     Only required if AnalysisMethod='spectral'
    
        %--------------------
        %Calculation setup for sea and swell separation
        %--------------------
    
        %Sea and swell separation
        SeparateSeaSwell='no';
        %                                 Define if to separate wind sea and swell waves or not
        %                                     SeparateSeaSwell='no': Does not separate wind sea and swell waves
        %                                     SeparateSeaSwell='yes': Separates wind sea and swell waves

        %maximum swell frequency
        fmaxswell=0.25;
        %                                 Maximum frequency that swell can have (It is about 0.2 in Gulf of Mexico) in (Hz)
        %                                     It should be between 0 and (fs/2)
        %                                     Only required if SeparateSeaSwell='yes' and AnalysisMethod='spectral'

        %Minimum swell frequency
        fpminswell=0.1;
        %                                 Minimum frequency that swell can have (it is used for Tpswell calculation) in (Hz)
        %                                     It should be between 0 and (fs/2)
        %                                     Only required if SeparateSeaSwell='yes' and AnalysisMethod='spectral'

        %--------------------
        %Diagnostic tail setup if spectral analysis is used
        %--------------------
        
        %Diagnostic tail
        tailcorrection='off';
        %                                 Define if to replace spectrum tail with tail of empirical spectrum (diagnostic tail) or not 
        %                                     tailcorrection='off': Does replace spectrum tail
        %                                     tailcorrection='jonswap': Replace spectrum tail with JONSWAP Spectrum tail
        %                                     tailcorrection='tma': Replace spectrum tail with TMA Spectrum tail
        %
        %                                         For tailcorrection='tma', input data should be water depth
    
        ftailcorrection=0.9;
        %                                 Frequency that spectrum tail replaced after that in (Hz)
        %                                     ftailcorrection is typically set at ftailcorrection=(2.5*fm) where (fm=1/Tm01)
        %                                     It should be between 0 and (fs/2)
        %                                     Only required if SeparateSeaSwell='yes' and tailcorrection='jonswap' or tailcorrection='tma'
    
        tailpower=-5;
        %                                 Power that a replaced tail (diagnostic tail)
        %                                     Replaced tail (diagnostic tail) will be proportional to (f^tailpower)
        %                                     Recommendation: use tailpower=-3 for shallow water and tailpower=-5 for deep water
        %                                     Only required if SeparateSeaSwell='yes' and tailcorrection='jonswap' or tailcorrection='tma'
   
        %--------------------
        %Default values
        %--------------------

        %Default calculation module
        module=1;

        %Default values
        mincutoff='on';
        maxcutoff='on';
        
    end

%--------------------------------------------------------------------------
    methods

        %==========================================================================
        function [module]=oceanlyzmodule(obj)
            %
            %DESCRIPTION
            %-----------
            %
            %Define calculation module
            %
            %OUTPUT
            %------
            %Calculation modul
            %
            %--------------------------------------------------------------------------
            disp('--------------------------------------------------')
            disp('Parameters (only required ones used)')
            
            %--------------------
            disp('--------------------------------------------------')
            disp(['InputType           : ', obj.InputType])
            disp(['OutputType          : ', obj.OutputType])

            %--------------------
            disp('-------------------------------')
            disp(['AnalysisMethod      : ', obj.AnalysisMethod])
            
            %--------------------
            disp('-------------------------------')
            disp(['n_burst             : ', num2str(obj.n_burst)])
            disp(['burst_duration      : ', num2str(obj.burst_duration)])
            disp(['fs                  : ', num2str(obj.fs)])
            
            %--------------------
            disp('-------------------------------')
            disp(['fmin                : ', num2str(obj.fmin)])
            disp(['fmax                : ', num2str(obj.fmax)])
            
            %--------------------
            disp('-------------------------------')
            disp(['fmaxpcorrCalcMethod : ', obj.fmaxpcorrCalcMethod])
            disp(['Kpafterfmaxpcorr    : ', obj.Kpafterfmaxpcorr])
            disp(['fminpcorr           : ', num2str(obj.fminpcorr)])
            disp(['fmaxpcorr           : ', num2str(obj.fmaxpcorr)])
            disp(['heightfrombed       : ', num2str(obj.heightfrombed)])
            
            %--------------------
            disp('-------------------------------')
            disp(['dispout             : ', obj.dispout])

            %--------------------
            disp('-------------------------------')
            disp(['Rho                 : ', num2str(obj.Rho)])
            disp(['nfft                : ', num2str(obj.nfft)])

            %--------------------
            disp('-------------------------------')
            disp(['SeparateSeaSwell    : ', obj.SeparateSeaSwell])
            disp(['fpminswell          : ', num2str(obj.fpminswell)])
            disp(['fmaxswell           : ', num2str(obj.fmaxswell)])
            
            %--------------------
            disp('-------------------------------')
            disp(['tailcorrection      : ', obj.tailcorrection])
            disp(['ftailcorrection     : ', num2str(obj.ftailcorrection)])
            disp(['tailpower           : ', num2str(obj.tailpower)])
            
            %--------------------
            
            %--------------------------------------------------------------------------
            %Define a module number based on the input parameters
            
            % module=1:
            %    Description       : Calculate wave parameters
            %    Calculation Method: spectral analysis
            %    Input Data        : water depth or surface elevation data
            %    Output            : wave parameters
            %
            % module=2:
            %    Description       : Calculate wave parameters
            %    Calculation Method: zero-crossing
            %    Input Data        : water depth or surface elevation data
            %    Output            : wave parameters
            %
            % module=3:
            %    Description       : Calculate water level data from water pressure data
            %                        It accounts for pressure attenuation in depth
            %    Calculation Method: spectral analysis (Fast Fourier Transform)
            %    Input Data        : water pressure data measured by a pressure sensor
            %    Output            : water level
            %
            % module=4:
            %    Description       : Calculate water level data from water pressure data
            %                        It accounts for pressure attenuation in depth
            %    Calculation Method: zero-crossing (linear wave theory)
            %    Input Data        : water pressure data measured by a pressure sensor
            %    Output            : water level
            %
            % module=5:
            %    Description       : Separate wind sea and swell waves and calculate wave parameters
            %    Calculation Method: spectral analysis
            %    Input Data        : water depth or surface elevation data
            %    Output            : wave parameters
            %
            % module=6:
            %    Description       : Calculate water level data from water pressure data and calculate wave parameters
            %                        It accounts for pressure attenuation in depth
            %    Calculation Method: spectral analysis (Fast Fourier Transform)
            %    Input Data        : water pressure data measured by a pressure sensor
            %    Output            : wave parameters, water level
            %
            % module=7:
            %    Description       : Calculate water level data from water pressure data and calculate wave parameters
            %                        It accounts for pressure attenuation in depth
            %    Calculation Method: zero-crossing (linear wave theory)
            %    Input Data        : water pressure data measured by a pressure sensor
            %    Output            : wave parameters, water level
            %
            % module=8:
            %    Description       : Calculate water level data from water pressure data, separate wind sea and swell waves, and calculate wave parameters
            %                        It accounts for pressure attenuation in depth
            %    Calculation Method: spectral analysis (Fast Fourier Transform)
            %    Input Data        : water pressure data measured by a pressure sensor
            %    Output            : wave parameters, water level
            
            disp('--------------------------------------------------')
            
            %Default value
            %module=1;
            
            %Check input values
            if strcmp(obj.InputType,'waterlevel')==1
                if (strcmp(obj.OutputType,'waterlevel')==1 | strcmp(obj.OutputType,'wave+waterleve')==1)
                    obj.OutputType='wave';
                    disp('OutputType is set to "wave"')
                    disp('--------------------------------------------------')
                end
            end

            if strcmp(obj.InputType,'pressure')==1
                if strcmp(obj.OutputType,'wave')==1
                    obj.OutputType='wave+waterlevel';
                    disp('OutputType is set to "wave+waterlevel"')
                    disp('--------------------------------------------------')
                end
            end
            
            if strcmp(obj.SeparateSeaSwell,'yes')==1
                if strcmp(obj.AnalysisMethod,'zerocross')==1
                    obj.AnalysisMethod='spectral';
                    disp('AnalysisMethod is set to "spectral"')
                    disp('--------------------------------------------------')
                end
            end

            %Setting calculation method
            %Module 1
            if strcmp(obj.InputType,'waterlevel')==1
                if strcmp(obj.OutputType,'wave')==1
                    if strcmp(obj.AnalysisMethod,'spectral')==1
                        if strcmp(obj.SeparateSeaSwell,'no')==1
                            module=1;
                            disp('Calculation Method: module=1')
                            disp('Description       : Calculate wave parameters')
                            disp('Calculation Method: spectral analysis')
                            disp('Input Data        : water depth or surface elevation data')
                            disp('Output            : wave parameters')
                        end
                    end
                end
            end

            %Module 2
            if strcmp(obj.InputType,'waterlevel')==1
                if strcmp(obj.OutputType,'wave')==1
                    if strcmp(obj.AnalysisMethod,'zerocross')==1
                        if strcmp(obj.SeparateSeaSwell,'no')==1
                            module=2;
                            disp('Calculation Method: module=2')
                            disp('Description       : Calculate wave parameters')
                            disp('Calculation Method: zero-crossing')
                            disp('Input Data        : water depth or surface elevation data')
                            disp('Output            : wave parameters')
                        end
                    end
                end
            end

            %Module 3
            if strcmp(obj.InputType,'pressure')==1
                if strcmp(obj.OutputType,'waterlevel')==1
                    if strcmp(obj.AnalysisMethod,'spectral')==1
                        if strcmp(obj.SeparateSeaSwell,'no')==1
                            module=3;
                            disp('Calculation Method: module=3')
                            disp('Description       : Calculate water level data from water pressure data')
                            disp('                    It accounts for pressure attenuation in depth')
                            disp('Calculation Method: spectral analysis (Fast Fourier Transform)')
                            disp('Input Data        : water pressure data measured by a pressure sensor')
                            disp('Output            : water level')
                        end
                    end
                end
            end

            %Module 4
            if strcmp(obj.InputType,'pressure')==1
                if strcmp(obj.OutputType,'waterlevel')==1
                    if strcmp(obj.AnalysisMethod,'zerocross')==1
                        if strcmp(obj.SeparateSeaSwell,'no')==1
                            module=4;
                            disp('Calculation Method: module=4')
                            disp('Description       : Calculate water level data from water pressure data')
                            disp('                    It accounts for pressure attenuation in depth')
                            disp('Calculation Method: zero-crossing (linear wave theory)')
                            disp('Input Data        : water pressure data measured by a pressure sensor')
                            disp('Output            : water level')
                        end
                    end
                end
            end

            %Module 5
            if strcmp(obj.InputType,'waterlevel')==1
                if strcmp(obj.OutputType,'wave')==1
                    if strcmp(obj.AnalysisMethod,'spectral')==1
                        if strcmp(obj.SeparateSeaSwell,'yes')==1
                            module=5;
                            disp('Calculation Method: module=5')
                            disp('Description       : Separate wind sea and swell waves and calculate wave parameters')
                            disp('Calculation Method: spectral analysis')
                            disp('Input Data        : water depth or surface elevation data')
                            disp('Output            : wave parameters')
                        end
                    end
                end
            end

            %Module 6
            if strcmp(obj.InputType,'pressure')==1
                if strcmp(obj.OutputType,'wave+waterlevel')==1
                    if strcmp(obj.AnalysisMethod,'spectral')==1
                        if strcmp(obj.SeparateSeaSwell,'no')==1
                            module=6;
                            disp('Calculation Method: module=6')
                            disp('Description       : Calculate water level data from water pressure data and calculate wave parameters')
                            disp('                    It accounts for pressure attenuation in depth')
                            disp('Calculation Method: spectral analysis (Fast Fourier Transform)')
                            disp('Input Data        : water pressure data measured by a pressure sensor')
                            disp('Output            : wave parameters, water level')
                        end
                    end
                end
            end

            %Module 7
            if strcmp(obj.InputType,'pressure')==1
                if strcmp(obj.OutputType,'wave+waterlevel')==1
                    if strcmp(obj.AnalysisMethod,'zerocross')==1
                        if strcmp(obj.SeparateSeaSwell,'no')==1
                            module=7;
                            disp('Calculation Method: module=7')
                            disp('Description       : Calculate water level data from water pressure data and calculate wave parameters')
                            disp('                    It accounts for pressure attenuation in depth')
                            disp('Calculation Method: zero-crossing (linear wave theory)')
                            disp('Input Data        : water pressure data measured by a pressure sensor')
                            disp('Output            : wave parameters, water level')
                        end
                    end
                end
            end

            %Module 8
            if strcmp(obj.InputType,'pressure')==1
                if strcmp(obj.OutputType,'wave+waterlevel')==1
                    if strcmp(obj.AnalysisMethod,'spectral')==1
                        if strcmp(obj.SeparateSeaSwell,'yes')==1
                            module=8;
                            disp('Calculation Method: module=8')
                            disp('Description       : Calculate water level data from water pressure data, separate wind sea and swell waves, and calculate wave parameters')
                            disp('                    It accounts for pressure attenuation in depth')
                            disp('Calculation Method: spectral analysis (Fast Fourier Transform)')
                            disp('Input Data        : water pressure data measured by a pressure sensor')
                            disp('Output            : wave parameters, water level')
                        end
                    end
                end
            end


            %{
            if strcmp(obj.AnalysisMethod,'spectral')==1
                if strcmp(obj.OutputType,'wave')==1
                    if strcmp(obj.SeparateSeaSwell,'no')==1
                        if strcmp(obj.InputType,'waterlevel')==1
                            module=1;
                            disp('module=1 : Calculates wave parameters using a spectral analysis method')
                            disp('Input Data: water depth or surface elevation data')
                            disp('Output    : wave parameters')
                        elseif strcmp(obj.InputType,'pressure')==1
                            module=6;
                            disp('module=6 : Correctes water level data measured by a pressure sensor, using a spectral analysis method')
                            disp('Calculates wave parameters using a spectral analysis method')
                            disp('It accounts for pressure attenuation in depth')
                            disp('Input Data: water depth data measured by a pressure sensor')
                            disp('Output    : wave parameters, corrected water level')
                        end
                    elseif strcmp(obj.SeparateSeaSwell,'yes')==1
                        if strcmp(obj.InputType,'waterlevel')==1
                            module=5;
                            disp('module=5 : Separates wind sea and swell waves')
                            disp('Calculates wave parameters using a spectral analysis method')
                            disp('Input Data: water depth or surface elevation data')
                            disp('Output    : wave parameters')
                        elseif strcmp(obj.InputType,'pressure')==1
                            module=8;
                            disp('module=8 : Correctes wave pressure data using a spectral analysis method (Fast Fourier Transform)')
                            disp('Separates wind sea and swell waves')
                            disp('Calculates wave parameters using a spectral analysis method')
                            disp('It accounts for pressure attenuation in depth')
                            disp('Input Data: water depth data measured by a pressure sensor')
                            disp('Output    : wave parameters, corrected water level')
                        end
                    end
                elseif strcmp(obj.OutputType,'waterlevel')==1
                    if strcmp(obj.InputType,'pressure')==1
                        module=3;
                        disp('module=3 : Correctes water wevel data measured by a pressure sensor, using a spectral analysis method')
                        disp('It accounts for pressure attenuation in depth')
                        disp('Input Data: water depth data measured by a pressure sensor')
                        disp('Output    : corrected water level')
                    end
                end
            elseif strcmp(obj.AnalysisMethod,'zerocross')==1
                if strcmp(obj.OutputType,'wave')==1
                    if strcmp(obj.InputType,'waterlevel')==1
                        module=2;
                        disp('module=2 : Calculates wave parameters using a zero-crossing method')
                        disp('Input Data: water depth or surface elevation data')
                        disp('Output    : wave parameters')
                    elseif strcmp(obj.InputType,'pressure')==1
                        module=7;
                        disp('module=7 : Correctes water level data measured by a pressure sensor, using the linear wave theory')
                        disp('Calculates wave parameters using a zero-crossing method')
                        disp('It accounts for pressure attenuation in depth')
                        disp('Input Data: water depth data measured by a pressure sensor')
                        disp('Output    : wave parameters, corrected water level')
                    end
                elseif strcmp(obj.OutputType,'waterlevel')==1
                    if strcmp(obj.InputType,'pressure')==1
                        module=4;
                        disp('module=4 : Correctes water level data measured by a pressure sensor, using the linear wave theory')
                        disp('It accounts for pressure attenuation in depth')
                        disp('Input Data: water depth data measured by a pressure sensor')
                        disp('Output    : corrected water level')
                    end
                end
            end
            %}

            disp('--------------------------------------------------')
            
            %--------------------------------------------------------------------------
            
        end


        %==========================================================================
        function [wave]=oceanlyzecalcwave(obj)
            %
            %DESCRIPTION
            %-----------
            %
            %Calculate wave properties
            %
            %OUTPUT
            %------
            %Output the wave properties depending on the selected module as a structure array such as:
            %
            %wave.Tp
            %                                Peak wave period in (Second)
            %wave.Hm0
            %                                Zero-moment wave height in (m)
            %
            %Calculated wave properties as a structure array
            %    Output is a structure array
            %    Name of output is 'oceanlyz_object.wave'
            %    Field(s) in this structure array can be called by using '.'
            %    Example:
            %
            %        wave.Hm0         : Contain zero-moment wave height
            %        wave.Tp          : Contain peak wave period
            %        wave.Field_Names : Contain field (variable) names in the wave array
            %        wave.Burst_Data  : Contain data for each burst
            %
            %--------------------------------------------------------------------------
            %Load data
            
            %currentpath=pwd;
            %cd(InputFileFolder);
            d=(obj.data);
            
            %Check if inputs are column vectors
            if isrow(d)==1
                d=d';
            end
            
            %Check data for NaN
            if sum(isnan(d))~=0
                %error('Input file contains NaN value(s), Oceanlyz will be terminated.');
                warning('Input file contains NaN value(s).');
                warning('NaN value(s) are replaced by linearly interpolated value(s).');
                warning('Oceanlyz continues with modified data.');
                
                %Replacing NaN values
                Indx(:,1)=linspace(1,length(d(:,1)),length(d(:,1)));
                d=interp1(Indx(isnan(d)==0),d(isnan(d)==0),Indx);
            end
            
            %Check data for Inf
            if sum(isinf(d))~=0
                %error('Input file contains Inf value(s), Oceanlyz will be terminated.');
                warning('Input file contains Inf value(s).');
                warning('Inf value(s) are replaced by linearly interpolated value(s).');
                warning('Oceanlyz continues with modified data.');
                
                %Replacing Inf values
                Indx(:,1)=linspace(1,length(d(:,1)),length(d(:,1)));
                d=interp1(Indx(isinf(d)==0),d(isinf(d)==0),Indx);
            end
            
            %Check data for zero values
            if sum(d==0)~=0
                warning('Input file contains Zero value(s), Oceanlyz continues with current data.');
            end
            
            %--------------------------------------------------------------------------
            
            %Calculate number of sample in 1 burst
            n_sample=obj.fs*obj.burst_duration; %Number of sample in 1 burst
            
            %Make sure n_burst and n_sample are int
            %obj.n_burst = fix(obj.n_burst)
            %n_sample = fix(n_sample)

            %CALLING-FUNCTION----------------------------------------------------------
            %Call calculation functions

            if strcmp(obj.InputType,'pressure')==1
                d=d./(obj.Rho*9.81);
            end
            
            if strcmp(obj.InputType,'pressure')==1 & strcmp(obj.fmaxpcorrCalcMethod,'auto')==1
                autofmaxpcorr='on';
            elseif strcmp(obj.InputType,'pressure')==1 & strcmp(obj.fmaxpcorrCalcMethod,'user')==1
                autofmaxpcorr='off';
            end
           
            if strcmp(obj.InputType,'waterlevel')==1
                pressureattenuation='off';
            elseif strcmp(obj.InputType,'pressure')==1 & strcmp(obj.Kpafterfmaxpcorr,'constant')==1
                pressureattenuation='all';
            elseif strcmp(obj.InputType,'pressure')==1 & strcmp(obj.Kpafterfmaxpcorr,'one')==1
                pressureattenuation='on';
            end

            if strcmp(obj.dispout,'yes')==1
                dispout='on';
            elseif strcmp(obj.dispout,'no')==1
                dispout='off';
            end

            %Calculation functions
            for i=1:obj.n_burst
                
                if strcmp(obj.dispout,'yes')==1
                    Step=['Burst = ',num2str(i)];
                    disp('--------------------------------------------------')
                    disp(Step)
                    if obj.module==1 | obj.module==5 | obj.module==6 | obj.module==8
                        hold on
                    end
                end
            
                %Load burst data
                j1=(i-1)*n_sample+1;
                j2=i*n_sample;
                input_data=d(j1:j2,1);
                
                %Calculate mean water depth
                if strcmp(obj.InputType,'waterlevel')==1
                    h=mean(input_data(:,1)); %Calculating mean water depth from water depth data
                elseif strcmp(obj.InputType,'pressure')==1
                    h=mean(input_data(:,1))+obj.heightfrombed; %Calculating mean water depth from pressure data
                end

                if h<=0
                    warning('Mean water depth is Zero or negative, Oceanlyz continues with mean water depth=0.001 m.');
                    h=0.001;
                end
                
                %Call function
                if obj.module==1
                    [wave.Hm0(i,1),~,~,wave.Tp(i,1),wave.fp(i,1),wave.f(i,:),wave.Syy(i,:)]=WaveSpectraFun(input_data,obj.fs,obj.burst_duration,obj.nfft,h,obj.heightfrombed,obj.fmin,obj.fmax,obj.ftailcorrection,obj.tailpower,obj.mincutoff,obj.maxcutoff,obj.tailcorrection,dispout);
                    %[wave.Hm0(i,1), wave.fp(i,1), wave.Tp(i,1), ~, ~, wave.f(i,:), wave.Syy(i,:), ~] = wavefromsurfaceelevpsd(input_data, obj.fs, obj.fmin, obj.fmax, [], [], [], obj.dispout);
                    wave.Field_Names = ['Hm0, Tp, fp, f, Syy, Field_Names, Burst_Data'];
            
                elseif obj.module==2
                    [wave.Hs(i,1),wave.Hz(i,1),wave.Tz(i,1),wave.Ts(i,1),~,~]=WaveZerocrossingFun(input_data,obj.fs,obj.burst_duration,'off');
                    %[wave.Hs(i,1), wave.Ts(i,1), wave.Hz(i,1), wave.Tz(i,1), ~, ~, ~] = wavefromsurfaceelevzcross(input_data, obj.fs, 'no');
                    wave.Field_Names = ['Hs, Hz, Tz, Ts, Field_Names, Burst_Data'];
                
                elseif obj.module==3
                    [wave.Eta(i,:),~]=PcorFFTFun(input_data,obj.fs,obj.burst_duration,obj.nfft,h,obj.heightfrombed,obj.fminpcorr,obj.fmaxpcorr,obj.ftailcorrection,pressureattenuation,autofmaxpcorr,'off');
                    %[wave.Eta(i,:), ~] = pressure2surfaceelevfft(input_data, obj.fs, obj.burst_duration, h, obj.heightfrombed, obj.fmaxpcorr, obj.fminpcorr, obj.fmin, obj.fmax, obj.fmaxpcorrCalcMethod, obj.Kpafterfmaxpcorr, 'beji', 1000, 'no');
                    wave.Field_Names = ['Eta, Field_Names, Burst_Data'];
            
                elseif obj.module==4
                    [wave.Eta(i,:)]=PcorZerocrossingFun(input_data,obj.fs,obj.burst_duration,h,obj.heightfrombed,'off');
                    %[wave.Eta(i,:), ~] = pressure2surfaceelevzcross(input_data, obj.fs, h, obj.heightfrombed, 0.15, 'beji', 1000, 'no');
                    wave.Field_Names = ['Eta, Field_Names, Burst_Data'];
                
                elseif obj.module==5
                    [wave.Hm0(i,1),wave.Hm0sea(i,1),wave.Hm0swell(i,1),wave.Tp(i,1),wave.Tpsea(i,1),wave.Tpswell(i,1),wave.fp(i,1),wave.fseparation(i,1),wave.f(i,:),wave.Syy(i,:)]=SeaSwellFun(input_data,obj.fs,obj.burst_duration,obj.nfft,h,obj.fmin,obj.fmax,obj.ftailcorrection,obj.tailpower,obj.fpminswell,obj.fmaxswell,obj.mincutoff,obj.maxcutoff,obj.tailcorrection,dispout);
                    %[~, ~, ~, ~, ~, wave.f(i,:), wave.Syy(i,:), ~] = wavefromsurfaceelevpsd(input_data, obj.fs, obj.fmin, obj.fmax, [], [], [], 'no');
                    %[wave.fseparation(i,1), wave.Hm0(i,1), wave.Hm0sea(i,1), wave.Hm0swell(i,1), wave.Tp(i,1), wave.Tpsea(i,1), wave.Tpswell(i,1), ~, ~, ~, wave.fp(i,1), ~, ~] = seaswell1d((wave.f(i,:)).', (wave.Syy(i,:)).', 'hwang', 0.5, obj.fmaxswell, obj.fpminswell, 10, obj.dispout);
                    wave.Field_Names = ['Hm0, Hm0sea, Hm0swell, Tp, Tpsea, Tpswell, fp, fseparation, f, Syy, Field_Names, Burst_Data'];
            
                elseif obj.module==6
                    [wave.Eta(i,:),ftailcorrection]=PcorFFTFun(input_data,obj.fs,obj.burst_duration,obj.nfft,h,obj.heightfrombed,obj.fminpcorr,obj.fmaxpcorr,obj.ftailcorrection,pressureattenuation,autofmaxpcorr,'off'); 
                    [wave.Hm0(i,1),~,~,wave.Tp(i,1),wave.fp(i,1),wave.f(i,:),wave.Syy(i,:)]=WaveSpectraFun((wave.Eta(i,:))',obj.fs,obj.burst_duration,obj.nfft,h,obj.heightfrombed,obj.fmin,obj.fmax,obj.ftailcorrection,obj.tailpower,obj.mincutoff,obj.maxcutoff,obj.tailcorrection,dispout);
                    %[wave.Hm0(i,1), wave.fp(i,1), wave.Tp(i,1), ~, ~, wave.f(i,:), wave.Syy(i,:), ~, ~] = wavefrompressurepsd(input_data, obj.fs, h, obj.heightfrombed, obj.fmaxpcorr, obj.fminpcorr, obj.fmin, obj.fmax, obj.fmaxpcorrCalcMethod, obj.Kpafterfmaxpcorr, 'beji', 1000, [], [], [], obj.dispout);
                    wave.Field_Names = ['Eta, Hm0, Tp, fp, f, Syy, Field_Names, Burst_Data'];
            
                elseif obj.module==7
                    [wave.Eta(i,:)]=PcorZerocrossingFun(input_data,obj.fs,obj.burst_duration,h,obj.heightfrombed,'off');
                    [wave.Hs(i,1),wave.Hz(i,1),wave.Tz(i,1),wave.Ts(i,1),~,~]=WaveZerocrossingFun((wave.Eta(i,:))',obj.fs,obj.burst_duration,'off');
                    %[wave.Eta(i,:), ~] = pressure2surfaceelevzcross(input_data, obj.fs, h, obj.heightfrombed, 0.15, 'beji', 1000, 'no');
                    %[wave.Hs(i,1), wave.Ts(i,1), wave.Hz(i,1), wave.Tz(i,1), ~, ~, ~] = wavefromsurfaceelevzcross((wave.Eta(i,:)).', obj.fs, 'no');
                    %[wave.Hs(i,1), wave.Ts(i,1), wave.Hz(i,1), wave.Tz(i,1), ~, ~, ~, wave.Eta(i,:), ~] = wavefrompressurezcross(input_data, obj.fs, h, obj.heightfrombed, 0.15, 'beji', 1000, 'no');
                    wave.Field_Names = ['Eta, Hs, Hz, Tz, Ts, Field_Names, Burst_Data'];
            
                elseif obj.module==8
                    [wave.Eta(i,:),ftailcorrection]=PcorFFTFun(input_data,obj.fs,obj.burst_duration,obj.nfft,h,obj.heightfrombed,obj.fminpcorr,obj.fmaxpcorr,obj.ftailcorrection,pressureattenuation,autofmaxpcorr,'off');
                    [wave.Hm0(i,1),wave.Hm0sea(i,1),wave.Hm0swell(i,1),wave.Tp(i,1),wave.Tpsea(i,1),wave.Tpswell(i,1),wave.fp(i,1),wave.fseparation(i,1),wave.f(i,:),wave.Syy(i,:)]=SeaSwellFun((wave.Eta(i,:))',obj.fs,obj.burst_duration,obj.nfft,h,obj.fmin,obj.fmax,obj.ftailcorrection,obj.tailpower,obj.fpminswell,obj.fmaxswell,obj.mincutoff,obj.maxcutoff,obj.tailcorrection,dispout);
                    %[~, ~, ~, ~, ~, wave.f(i,:), wave.Syy(i,:), ~, ~] = wavefrompressurepsd(input_data, obj.fs, h, obj.heightfrombed, obj.fmaxpcorr, obj.fminpcorr, obj.fmin, obj.fmax, obj.fmaxpcorrCalcMethod, obj.Kpafterfmaxpcorr, 'beji', 1000, [], [], [], 'no');
                    %[wave.fseparation(i,1), wave.Hm0(i,1), wave.Hm0sea(i,1), wave.Hm0swell(i,1), wave.Tp(i,1), wave.Tpsea(i,1), wave.Tpswell(i,1), ~, ~, ~, wave.fp(i,1), ~, ~] = seaswell1d((wave.f(i,:)).', (wave.Syy(i,:)).', 'hwang', 0.5, obj.fmaxswell, obj.fpminswell, 10, obj.dispout);
                    wave.Field_Names = ['Eta, Hm0, Hm0sea, Hm0swell, Tp, Tpsea, Tpswell, fp, fseparation, f, Syy, Field_Names, Burst_Data'];
                
                end
                
                %if strcmp(obj.dispout,'yes')==1
                %    wb=waitbar(i/obj.n_burst);
                %    waitbar(i/obj.n_burst,wb,sprintf('Percentage = %0.2f',i/obj.n_burst*100))
                %else
                %    fprintf('%14s   %g  %s   %g \n','burst:',i,'out of',obj.n_burst);
                %end
                if strcmp(obj.dispout,'no')==1
                    fprintf('%14s   %g  %s   %g \n','burst:',i,'out of',obj.n_burst);
                end
            
                wave.Burst_Data(i,:)=input_data; %Save input burst data
            
            end
            
        end


        %==========================================================================
        function runoceanlyz(obj)
            %--------------------------------------------------------------------------
            %Print

            CurrentDate=clock;
            %clc;
            disp('--------------------------------------------------')
            disp('OCEANLYZ Ver 2.0')
            disp('www.ArashKarimpour.com')
            disp(['Copyright (C) 2012-',num2str(CurrentDate(1)),' Arash Karimpour'])
            %disp('Copyright (C) 2018 Arash Karimpour')
            %disp('--------------------------------------------------')

            %--------------------------------------------------------------------------
            %Turn off warning

            warning('off');

            %--------------------------------------------------------------------------
            %Addinng the OCEANLYZ folder and its subfolders to the search path

            OceanlyzFolder=pwd; %Current (OCEANLYZ) path
            OceanlyzPath=genpath(OceanlyzFolder); %Generating path for OCEANLYZ folder and its subfolders
            addpath(OceanlyzPath);

            %FUNCTION------------------------------------------------------------------
            %Calling main calculating function
            %https://www.mathworks.com/help/matlab/matlab_oop/create-a-simple-class.html
            %https://www.mathworks.com/help/matlab/matlab_oop/specifying-methods-and-functions.html
            %https://www.mathworks.com/help/matlab/matlab_oop/method-invocation.html
            %https://www.mathworks.com/matlabcentral/answers/395472-how-to-call-a-method-from-a-class-called-a-within-another-method-from-a

            [obj.module]=obj.oceanlyzmodule();

            %--------------------------------------------------------------------------
            %Calculate wave properties

            disp('Calculating wave properties')

            %pkg load signal; % for Octave GNU User, it loads Signal Package 

            [obj.wave]=obj.oceanlyzecalcwave();


            %Output fields
            disp('--------------------------------------------------')
            disp('Output array is a structure array named "obj.wave"')
            disp('Field(s) in a structure array "wave" can be called by using "."')
            disp('Example: Output for a peak wave period is : "obj.wave.Tp"')
            disp('Field names may be obtained from fieldnames(obj.wave) command')
            disp('Also, obj.wave.Field_Names contains field names in the wave array')
            disp('Output field names are')
            fieldnames(obj.wave)
            disp('--------------------------------------------------')
            disp('Calculation finished')
            disp('--------------------------------------------------')
            
            %--------------------------------------------------------------------------
            %Removing OCEANLYZ floder and its subfolders from the search path

            rmpath(OceanlyzPath);

            %--------------------------------------------------------------------------
            %Turn on warning

            warning('on');

            %--------------------------------------------------------------------------

        end
    end
%--------------------------------------------------------------------------
end
