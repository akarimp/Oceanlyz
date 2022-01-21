class oceanlyz:
    """
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

    oceanlyz.oceanlyz (Python Version)
    ==================================

    .. code:: python

        oceanlyz_object = oceanlyz.oceanlyz()

    DESCRIPTION
    -----------

    | Calculate wave properties from water level or water pressure data
    | For OCEANLYZ Document visit https://oceanlyz.readthedocs.io

    Required Properties
    -------------------

    Following properties are required for all analysis

    data=[]
        Water level (water surface elevation, Eta), water depth, or water pressure time series
            | Data should be a single column array (column vector) without any text
            | Each burst of data should follow the previous burst without any void

    InputType='waterlevel'
        Define input data type
            InputType='waterlevel': Input data is water level or water depth in (m)
                If InputType='waterlevel' then OutputType='wave'
            InputType='pressure': Input data are water pressure measured by a pressure sensor at sensor depth in (N/m^2)
                If InputType='pressure' then OutputType='waterlevel' or OutputType='wave+waterlevel'

    OutputType='wave'
        Define output data type
            | OutputType='wave': Calculate wave properties from water level or water depth data
            | OutputType='waterlevel': Calculate water level data from water pressure data measured by a pressure sensor
            | OutputType='wave+waterlevel': Calculate waves properties and water level data from water pressure data measured by a pressure sensor

    AnalysisMethod='spectral'
        Analysis method
            | AnalysisMethod='spectral': Use spectral analysis method / Fast Fourier Transform
            | AnalysisMethod='zerocross': Use zero-crossing method

    n_burst=1
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

    burst_duration=1024
        Duration time that data collected in each burst in (second)

    fs=2
        Sampling frequency that data are collected at in (Hz)

    Required Properties for Spectral Analysis
    -----------------------------------------

    Following properties are needed only if AnalysisMethod='spectral'

    fmin=0.05
        Minimum frequency to cut off the spectrum below that, i.e. where f<fmin, in (Hz)
            | Results with frequency f<fmin will be removed from analysis
            | It should be between 0 and (fs/2)
            | It is a simple high pass filter
            | Only required if AnalysisMethod='spectral'

    fmax=1e6
        Maximum frequency to cut off the spectrum beyond that, i.e. where f>fmax, in (Hz)
            | Results with frequency f>fmax will be removed from analysis
            | It should be between 0 and (fs/2)
            | It is a simple low pass filter
            | Only required if AnalysisMethod='spectral'

    Required Properties for Pressure Data Analysis
    ----------------------------------------------

    Following properties are needed only if InputType='pressure'

    fmaxpcorrCalcMethod='auto'
        Define if to calculate fmaxpcorr and ftail or to use user defined
            | fmaxpcorrCalcMethod='user': use user defined value for fmaxpcorr
            | fmaxpcorrCalcMethod='auto': automatically define value for fmaxpcorr
            | Only required if InputType='pressure' and AnalysisMethod='spectral'

    Kpafterfmaxpcorr='constant'
        Define a pressure response factor, Kp, value for frequency larger than fmaxpcorr
            | Kpafterfmaxpcorr='one': Kp=1 for frequency larger than fmaxpcorr 
            | Kpafterfmaxpcorr='constant': Kp for f larger than fmaxpcorr stays equal to Kp at fmaxpcorr (constant)
            | Kpafterfmaxpcorr='nochange': Kp is not changed for frequency larger than fmaxpcorr (Not implemented yet)
            | Only required if InputType='pressure' and AnalysisMethod='spectral'

    fminpcorr=0.15
        Minimum frequency that automated calculated fmaxpcorr can have if fmaxpcorrCalcMethod='auto' in (Hz)
            | If fmaxpcorrCalcMethod='auto', then fmaxpcorr will be checked to be larger or equal to fminpcorr
            | It should be between 0 and (fs/2)
            | Only required if InputType='pressure' and AnalysisMethod='spectral'

    fmaxpcorr=0.55
        Maximum frequency for applying pressure attenuation factor in (Hz)
            | Pressure attenuation factor is not applied on frequency larger than fmaxpcorr
            | It should be between 0 and (fs/2)
            | Only required if InputType='pressure' and AnalysisMethod='spectral'

    heightfrombed=0.0
        Pressure sensor height from a bed in (m)
            Leave heightfrombed=0.0 if data are not measured by a pressure sensor or if a sensor sits on the seabed
            | Only required if InputType='pressure'

    Optional Properties
    -------------------

    Following properties are optional

    dispout='no'
        Define if to plot spectrum or not
            | dispout='no': Does not plot
            | dispout='yes': Plot

    Rho=1000
        Water density (kg/m^3)
            Only required if InputType='pressure'

    nfft=512
        Define number of data points in discrete Fourier transform
            | Should be 2^n
            | Results will be reported for frequency range of 0 <= f <= (fs/2) with (nfft/2+1) data points
            | Example: If fs=4 Hz and nfft=512, then output frequency has a range of 0 <= f <= 2 with 257 data points
            | Only required if AnalysisMethod='spectral'

    SeparateSeaSwell='no'
        Define if to separate wind sea and swell waves or not
            | SeparateSeaSwell='no': Does not separate wind sea and swell waves
            | SeparateSeaSwell='yes': Separates wind sea and swell waves

    fmaxswell=0.25
        Maximum frequency that swell can have (It is about 0.2 in Gulf of Mexico) in (Hz)
            | It should be between 0 and (fs/2)
            | Only required if SeparateSeaSwell='yes' and AnalysisMethod='spectral'

    fpminswell=0.1
        Minimum frequency that swell can have (it is used for Tpswell calculation) in (Hz)
            | It should be between 0 and (fs/2)
            | Only required if SeparateSeaSwell='yes' and AnalysisMethod='spectral'

    tailcorrection='off'
        Define if to replace spectrum tail with tail of empirical spectrum (diagnostic tail) or not 
            | tailcorrection='off': Does replace spectrum tail
            | tailcorrection='jonswap': Replace spectrum tail with JONSWAP Spectrum tail
            | tailcorrection='tma': Replace spectrum tail with TMA Spectrum tail

                For tailcorrection='tma', input data should be water depth

    ftailcorrection=0.9
        Frequency that spectrum tail replaced after that in (Hz)
            | ftailcorrection is typically set at ftailcorrection=(2.5*fm) where (fm=1/Tm01)
            | It should be between 0 and (fs/2)
            | Only required if SeparateSeaSwell='yes' and tailcorrection='jonswap' or tailcorrection='tma'

    tailpower=-5
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
        Calculated wave properties as a Python dictionary
            | Output is a Python dictionary
            | Name of output is 'oceanlyz_object.wave'
            | Values(s) in this dictionary can be called by using 'key'
            | Example:

                | oceanlyz_object.wave['Hm0']         : Contain zero-moment wave height
                | oceanlyz_object.wave['Tp']          : Contain peak wave period
                | oceanlyz_object.wave['Field_Names'] : Contain key (variable) names in the wave dictionary
                | oceanlyz_object.wave['Burst_Data']  : Contain data for each burst

    Examples
    --------

    .. code:: python

        #Import libraries
        import oceanlyz
        import numpy as np
        import matplotlib.pyplot as plt
        import os

        #Create OCEANLYZ object
        #del ocn #Optional
        ocn=oceanlyz.oceanlyz()
        
        #Read data
        #Assume data file is named 'waterpressure_5burst.csv' and is stored in 'C:\oceanlyz_python\Sample_Data'
        os.chdir('C:\\oceanlyz_python\\Sample_Data') #Change current path to Sample_Data folder
        water_pressure=np.genfromtxt('waterpressure_5burst.csv') #Load data
        
        #Input parameters
        ocn.data=water_pressure.copy()
        ocn.InputType='pressure'
        ocn.OutputType='wave+waterlevel'
        ocn.AnalysisMethod='spectral'
        ocn.n_burst=5
        ocn.burst_duration=1024
        ocn.fs=10
        ocn.fmin=0.05                    #Only required if ocn.AnalysisMethod='spectral'
        ocn.fmax=ocn.fs/2                #Only required if ocn.AnalysisMethod='spectral'
        ocn.fmaxpcorrCalcMethod='auto'   #Only required if ocn.InputType='pressure' and ocn.AnalysisMethod='spectral'
        ocn.Kpafterfmaxpcorr='constant'  #Only required if ocn.InputType='pressure' and ocn.AnalysisMethod='spectral'
        ocn.fminpcorr=0.15               #Only required if ocn.InputType='pressure' and ocn.AnalysisMethod='spectral'
        ocn.fmaxpcorr=0.55               #Only required if ocn.InputType='pressure' and ocn.AnalysisMethod='spectral'
        ocn.heightfrombed=0.05           #Only required if ocn.InputType='pressure' and ocn.AnalysisMethod='spectral'
        ocn.dispout='yes'               
        ocn.Rho=1024                     #Seawater density (Varies)

        #Run OCEANLYZ
        ocn.runoceanlyz()

        #Plot peak wave period (Tp)
        plt.plot(ocn.wave['Tp'])

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
    """

    #--------------------------------------------------------------------------
    #CODE
    #--------------------------------------------------------------------------
    #Import required packages
    #https://stackoverflow.com/questions/38087060/using-import-inside-class/38087292
    
    #import numpy as np
    #import warnings
    #import datetime

    #--------------------------------------------------------------------------
    #properties

    def __init__(self):
            
        #Assign default values

        #--------------------
        #Setup input and output data
        #--------------------

        #Inut data
        self.data=[]
        #                                 Water level (water surface elevation, Eta), water depth, or water pressure time series
        #                                     Data should be a single column array (column vector) without any text
        #                                     Each burst of data should follow the previous burst without any void

        #Output data
        self.wave={}
        #Calculated wave properties as a Python dictionary
        #                                 Output is a Python dictionary
        #                                 Name of output is 'oceanlyz_object.wave'
        #                                 Values(s) in this dictionary can be called by using 'key'
        #                                 Example:
        #
        #                                     oceanlyz_object.wave['Hm0']         : Contain zero-moment wave height
        #                                     oceanlyz_object.wave['Tp']          : Contain peak wave period
        #                                     oceanlyz_object.wave['Field_Names'] : Contain key (variable) names in the wave dictionary
        #                                     oceanlyz_object.wave['Burst_Data']  : Contain data for each burst

        #Define input data type
        self.InputType='waterlevel'
        #                                 Define input data type
        #                                     InputType='waterlevel': Input data is water level or water depth in (m)
        #                                         If InputType='waterlevel' then OutputType='wave'
        #                                     InputType='pressure': Input data are water pressure measured by a pressure sensor at sensor depth in (N/m^2)
        #                                         If InputType='pressure' then OutputType='waterlevel' or OutputType='wave+waterlevel'

        #Define output data type
        self.OutputType='wave'
        #                                 Define output data type
        #                                     OutputType='wave': Calculate wave properties from water level or water depth data
        #                                     OutputType='waterlevel': Calculate water level data from water pressure data measured by a pressure sensor
        #                                     OutputType='wave+waterlevel': Calculate waves properties and water level data from water pressure data measured by a pressure sensor

        #--------------------
        #Setup analysis method
        #--------------------

        #Define analysis method
        self.AnalysisMethod='spectral'
        #                                 Analysis method
        #                                     AnalysisMethod='spectral': Use spectral analysis method / Fast Fourier Transform
        #                                     AnalysisMethod='zerocross': Use zero-crossing method

        #--------------------
        #Setup measurement properties of input data
        #--------------------
        
        #Number of burst(s)
        self.n_burst=1
        #                                 Number of burst(s) in the input file
        #                                     n_burst = (total number of data points)/(burst_duration*fs)
        #                                     Example: 
        #                                         Assume data are collected for 6 hours at a sampling frequency of fs=10 Hz
        #                                         If data are analyzed at intervals of 30 minutes then there are 12 bursts (6 hours/30 minutes=12 bursts)
        #                                         For 12 bursts of data, which each burst has a duration of 30 minutes, and collected at sampling frequency of fs=10 Hz 
        #                                         burst_duration=(30 min * 60) = 1800 seconds
        #                                         total number of data points=(number of burst)*(duration of each burst)*(sampling frequency)
        #                                         total number of data points=(n_burst)*(burst_duration)*(fs)
        #                                         total number of data points=12 * 1800 * 10
        
        #Duration of each burst
        self.burst_duration=1024
        #                                 Duration time that data collected in each burst in (second)
        
        #Sampling frequency
        self.fs=2
        #                                 Sampling frequency that data are collected at in (Hz)

        #--------------------
        #Frequency setup if spectral analysis is used
        #--------------------
        
        #Minimum frequency used in spectral analysis
        self.fmin=0.05
        #                                 Minimum frequency to cut off the spectrum below that, i.e. where f<fmin, in (Hz)
        #                                     Results with frequency f<fmin will be removed from analysis
        #                                     It should be between 0 and (fs/2)
        #                                     It is a simple high pass filter
        #                                     Only required if AnalysisMethod='spectral'

        #Maximum frequency used in spectral analysis
        self.fmax=1e6
        #                                 Maximum frequency to cut off the spectrum beyond that, i.e. where f>fmax, in (Hz)
        #                                     Results with frequency f>fmax will be removed from analysis
        #                                     It should be between 0 and (fs/2)
        #                                     It is a simple low pass filter
        #                                     Only required if AnalysisMethod='spectral'

        #--------------------
        #Calculation setup if input is pressure
        #--------------------
        
        #fmaxpcorr calculation method
        self.fmaxpcorrCalcMethod='auto'
        #                                 Define if to calculate fmaxpcorr and ftail or to use user defined
        #                                     fmaxpcorrCalcMethod='user': use user defined value for fmaxpcorr
        #                                     fmaxpcorrCalcMethod='auto': automatically define value for fmaxpcorr
        #                                     Only required if InputType='pressure' and AnalysisMethod='spectral'
        
        #Pressure response factor for kp>fmaxpcorr
        self.Kpafterfmaxpcorr='constant'
        #                                 Define a pressure response factor, Kp, value for frequency larger than fmaxpcorr
        #                                     Kpafterfmaxpcorr='one': Kp=1 for frequency larger than fmaxpcorr 
        #                                     Kpafterfmaxpcorr='constant': Kp for f larger than fmaxpcorr stays equal to Kp at fmaxpcorr (constant)
        #                                     Kpafterfmaxpcorr='nochange': Kp is not changed for frequency larger than fmaxpcorr (Not implemented yet)
        #                                     Only required if InputType='pressure' and AnalysisMethod='spectral'

        #Minimume value of fmaxpcorr
        self.fminpcorr=0.15
        #                                 Minimum frequency that automated calculated fmaxpcorr can have if fmaxpcorrCalcMethod='auto' in (Hz)
        #                                     If fmaxpcorrCalcMethod='auto', then fmaxpcorr will be checked to be larger or equal to fminpcorr
        #                                     It should be between 0 and (fs/2)
        #                                     Only required if InputType='pressure' and AnalysisMethod='spectral'
        
        #Maximum frequency to apply a pressure response
        self.fmaxpcorr=0.55
        #                                 Maximum frequency for applying pressure attenuation factor in (Hz)
        #                                     Pressure attenuation factor is not applied on frequency larger than fmaxpcorr
        #                                     It should be between 0 and (fs/2)
        #                                     Only required if InputType='pressure' and AnalysisMethod='spectral'
        
        #Pressure sensor height from water bed
        self.heightfrombed=0.0
        #                                 Pressure sensor height from a bed in (m)
        #                                     Leave heightfrombed=0.0 if data are not measured by a pressure sensor or if a sensor sits on the seabed
        #                                      Only required if InputType='pressure'

        #--------------------
        #Display setup
        #--------------------

        #Display results
        self.dispout='no'
        #                                 Define if to plot spectrum or not
        #                                     dispout='no': Does not plot
        #                                     dispout='yes': Plot

        #--------------------
        #Setup NFFT and Rho
        #--------------------

        self.Rho=1000
        #                                 Water density (kg/m^3)
        #                                     Only required if InputType='pressure'
    
        self.nfft=512
        #                                 Define number of data points in discrete Fourier transform
        #                                     Should be 2^n
        #                                     Results will be reported for frequency range of 0 <= f <= (fs/2) with (nfft/2+1) data points
        #                                     Example: If fs=4 Hz and nfft=512, then output frequency has a range of 0 <= f <= 2 with 257 data points
        #                                     Only required if AnalysisMethod='spectral'
    
        #--------------------
        #Calculation setup for sea and swell separation
        #--------------------
    
        #Sea and swell separation
        self.SeparateSeaSwell='no'
        #                                 Define if to separate wind sea and swell waves or not
        #                                     SeparateSeaSwell='no': Does not separate wind sea and swell waves
        #                                     SeparateSeaSwell='yes': Separates wind sea and swell waves

        #maximum swell frequency
        self.fmaxswell=0.25
        #                                 Maximum frequency that swell can have (It is about 0.2 in Gulf of Mexico) in (Hz)
        #                                     It should be between 0 and (fs/2)
        #                                     Only required if SeparateSeaSwell='yes' and AnalysisMethod='spectral'

        #Minimum swell frequency
        self.fpminswell=0.1
        #                                 Minimum frequency that swell can have (it is used for Tpswell calculation) in (Hz)
        #                                     It should be between 0 and (fs/2)
        #                                     Only required if SeparateSeaSwell='yes' and AnalysisMethod='spectral'

        #--------------------
        #Diagnostic tail setup if spectral analysis is used
        #--------------------
        
        #Diagnostic tail
        self.tailcorrection='off'
        #                                 Define if to replace spectrum tail with tail of empirical spectrum (diagnostic tail) or not 
        #                                     tailcorrection='off': Does replace spectrum tail
        #                                     tailcorrection='jonswap': Replace spectrum tail with JONSWAP Spectrum tail
        #                                     tailcorrection='tma': Replace spectrum tail with TMA Spectrum tail
        #
        #                                         For tailcorrection='tma', input data should be water depth
    
        self.ftailcorrection=0.9
        #                                 Frequency that spectrum tail replaced after that in (Hz)
        #                                     ftailcorrection is typically set at ftailcorrection=(2.5*fm) where (fm=1/Tm01)
        #                                     It should be between 0 and (fs/2)
        #                                     Only required if SeparateSeaSwell='yes' and tailcorrection='jonswap' or tailcorrection='tma'
    
        self.tailpower=-5
        #                                 Power that a replaced tail (diagnostic tail)
        #                                     Replaced tail (diagnostic tail) will be proportional to (f^tailpower)
        #                                     Recommendation: use tailpower=-3 for shallow water and tailpower=-5 for deep water
        #                                     Only required if SeparateSeaSwell='yes' and tailcorrection='jonswap' or tailcorrection='tma'

        #--------------------
        #Default values
        #--------------------

        #Default calculation module
        self.module=1

        #Default values
        self.mincutoff='on'
        self.maxcutoff='on'

    #--------------------------------------------------------------------------
    #methods

    #==========================================================================
    def oceanlyzmodule(self):
        #
        #DESCRIPTION
        #-----------
        #
        #Define calculation module
        #
        #OUTPUT
        #------
        #Calculation modul
        #
        #--------------------------------------------------------------------------
        print('--------------------------------------------------')
        print('Parameters (only required ones used)')
        
        #--------------------
        print('--------------------------------------------------')
        print('InputType           : ', self.InputType)
        print('OutputType          : ', self.OutputType)

        #--------------------
        print('-------------------------------')
        print('AnalysisMethod      : ', self.AnalysisMethod)
        
        #--------------------
        print('-------------------------------')
        print('n_burst             : ', self.n_burst)
        print('burst_duration      : ', self.burst_duration)
        print('fs                  : ', self.fs)
        
        #--------------------
        print('-------------------------------')
        print('fmin                : ', self.fmin)
        print('fmax                : ', self.fmax)
        
        #--------------------
        print('-------------------------------')
        print('fmaxpcorrCalcMethod : ', self.fmaxpcorrCalcMethod)
        print('Kpafterfmaxpcorr    : ', self.Kpafterfmaxpcorr)
        print('fminpcorr           : ', self.fminpcorr)
        print('fmaxpcorr           : ', self.fmaxpcorr)
        print('heightfrombed       : ', self.heightfrombed)
        
        #--------------------
        print('-------------------------------')
        print('dispout             : ', self.dispout)

        #--------------------
        print('-------------------------------')
        print('Rho                 : ', self.Rho)
        print('nfft                : ', self.nfft)

        #--------------------
        print('-------------------------------')
        print('SeparateSeaSwell    : ', self.SeparateSeaSwell)
        print('fpminswell          : ', self.fpminswell)
        print('fmaxswell           : ', self.fmaxswell)
        
        #--------------------
        print('-------------------------------')
        print('tailcorrection      : ', self.tailcorrection)
        print('ftailcorrection     : ', self.ftailcorrection)
        print('tailpower           : ', self.tailpower)
        
        #--------------------
        
        #--------------------------------------------------------------------------
        #Define a module number based on the input parameters
        
        # module=1:
        #    Description       : Calculate wave parameters
        #    Calculation Method: spectral analysis
        #    Input Data        : water depth or surface elevation data
        #    Output            : wave parameters
        #
        # module=2:
        #    Description       : Calculate wave parameters
        #    Calculation Method: zero-crossing
        #    Input Data        : water depth or surface elevation data
        #    Output            : wave parameters
        #
        # module=3:
        #    Description       : Calculate water level data from water pressure data
        #                        It accounts for pressure attenuation in depth
        #    Calculation Method: spectral analysis (Fast Fourier Transform)
        #    Input Data        : water pressure data measured by a pressure sensor
        #    Output            : water level
        #
        # module=4:
        #    Description       : Calculate water level data from water pressure data
        #                        It accounts for pressure attenuation in depth
        #    Calculation Method: zero-crossing (linear wave theory)
        #    Input Data        : water pressure data measured by a pressure sensor
        #    Output            : water level
        #
        # module=5:
        #    Description       : Separate wind sea and swell waves and calculate wave parameters
        #    Calculation Method: spectral analysis
        #    Input Data        : water depth or surface elevation data
        #    Output            : wave parameters
        #
        # module=6:
        #    Description       : Calculate water level data from water pressure data and calculate wave parameters
        #                        It accounts for pressure attenuation in depth
        #    Calculation Method: spectral analysis (Fast Fourier Transform)
        #    Input Data        : water pressure data measured by a pressure sensor
        #    Output            : wave parameters, water level
        #
        # module=7:
        #    Description       : Calculate water level data from water pressure data and calculate wave parameters
        #                        It accounts for pressure attenuation in depth
        #    Calculation Method: zero-crossing (linear wave theory)
        #    Input Data        : water pressure data measured by a pressure sensor
        #    Output            : wave parameters, water level
        #
        # module=8:
        #    Description       : Calculate water level data from water pressure data, separate wind sea and swell waves, and calculate wave parameters
        #                        It accounts for pressure attenuation in depth
        #    Calculation Method: spectral analysis (Fast Fourier Transform)
        #    Input Data        : water pressure data measured by a pressure sensor
        #    Output            : wave parameters, water level
        
        print('--------------------------------------------------')
        
        #Default value
        #module=1
        
        #Check input values
        if self.InputType=='waterlevel':
            if ((self.OutputType=='waterlevel') or (self.OutputType=='wave+waterleve')):
                self.OutputType='wave'
                print('OutputType is set to "wave"')
                print('--------------------------------------------------')


        if self.InputType=='pressure':
            if self.OutputType=='wave':
                self.OutputType='wave+waterlevel'
                print('OutputType is set to "wave+waterlevel"')
                print('--------------------------------------------------')


        if self.SeparateSeaSwell=='yes':
            if self.AnalysisMethod=='zerocross':
                self.AnalysisMethod='spectral'
                print('AnalysisMethod is set to "spectral"')
                print('--------------------------------------------------')

        
        #Setting calculation method
        #Module 1
        if self.InputType=='waterlevel':
            if self.OutputType=='wave':
                if self.AnalysisMethod=='spectral':
                    if self.SeparateSeaSwell=='no':
                        module=1
                        print('Calculation Method: module=1')
                        print('Description       : Calculate wave parameters')
                        print('Calculation Method: spectral analysis')
                        print('Input Data        : water depth or surface elevation data')
                        print('Output            : wave parameters')


        #Module 2
        if self.InputType=='waterlevel':
            if self.OutputType=='wave':
                if self.AnalysisMethod=='zerocross':
                    if self.SeparateSeaSwell=='no':
                        module=2
                        print('Calculation Method: module=2')
                        print('Description       : Calculate wave parameters')
                        print('Calculation Method: zero-crossing')
                        print('Input Data        : water depth or surface elevation data')
                        print('Output            : wave parameters')


        #Module 3
        if self.InputType=='pressure':
            if self.OutputType=='waterlevel':
                if self.AnalysisMethod=='spectral':
                    if self.SeparateSeaSwell=='no':
                        module=3
                        print('Calculation Method: module=3')
                        print('Description       : Calculate water level data from water pressure data')
                        print('                    It accounts for pressure attenuation in depth')
                        print('Calculation Method: spectral analysis (Fast Fourier Transform)')
                        print('Input Data        : water pressure data measured by a pressure sensor')
                        print('Output            : water level')


        #Module 4
        if self.InputType=='pressure':
            if self.OutputType=='waterlevel':
                if self.AnalysisMethod=='zerocross':
                    if self.SeparateSeaSwell=='no':
                        module=4
                        print('Calculation Method: module=4')
                        print('Description       : Calculate water level data from water pressure data')
                        print('                    It accounts for pressure attenuation in depth')
                        print('Calculation Method: zero-crossing (linear wave theory)')
                        print('Input Data        : water pressure data measured by a pressure sensor')
                        print('Output            : water level')


        #Module 5
        if self.InputType=='waterlevel':
            if self.OutputType=='wave':
                if self.AnalysisMethod=='spectral':
                    if self.SeparateSeaSwell=='yes':
                        module=5
                        print('Calculation Method: module=5')
                        print('Description       : Separate wind sea and swell waves and calculate wave parameters')
                        print('Calculation Method: spectral analysis')
                        print('Input Data        : water depth or surface elevation data')
                        print('Output            : wave parameters')


        #Module 6
        if self.InputType=='pressure':
            if self.OutputType=='wave+waterlevel':
                if self.AnalysisMethod=='spectral':
                    if self.SeparateSeaSwell=='no':
                        module=6
                        print('Calculation Method: module=6')
                        print('Description       : Calculate water level data from water pressure data and calculate wave parameters')
                        print('                    It accounts for pressure attenuation in depth')
                        print('Calculation Method: spectral analysis (Fast Fourier Transform)')
                        print('Input Data        : water pressure data measured by a pressure sensor')
                        print('Output            : wave parameters, water level')


        #Module 7
        if self.InputType=='pressure':
            if self.OutputType=='wave+waterlevel':
                if self.AnalysisMethod=='zerocross':
                    if self.SeparateSeaSwell=='no':
                        module=7
                        print('Calculation Method: module=7')
                        print('Description       : Calculate water level data from water pressure data and calculate wave parameters')
                        print('                    It accounts for pressure attenuation in depth')
                        print('Calculation Method: zero-crossing (linear wave theory)')
                        print('Input Data        : water pressure data measured by a pressure sensor')
                        print('Output            : wave parameters, water level')


        #Module 8
        if self.InputType=='pressure':
            if self.OutputType=='wave+waterlevel':
                if self.AnalysisMethod=='spectral':
                    if self.SeparateSeaSwell=='yes':
                        module=8
                        print('Calculation Method: module=8')
                        print('Description       : Calculate water level data from water pressure data, separate wind sea and swell waves, and calculate wave parameters')
                        print('                    It accounts for pressure attenuation in depth')
                        print('Calculation Method: spectral analysis (Fast Fourier Transform)')
                        print('Input Data        : water pressure data measured by a pressure sensor')
                        print('Output            : wave parameters, water level')


        print('--------------------------------------------------')
        
        return module

        #--------------------------------------------------------------------------


    #==========================================================================
    def oceanlyzecalcwave(self):
        #
        #DESCRIPTION
        #-----------
        #
        #Calculate wave properties
        #
        #OUTPUT
        #------
        #Output the wave properties depending on the selected module as a Python dictionary such as:
        #
        #wave['Tp']
        #                                Peak wave period in (Second)
        #wave['Hm0']
        #                                Zero-moment wave height in (m)
        #
        #Calculated wave properties as a Python dictionary
        #    Output is a Python dictionary
        #    Name of output is 'wave'
        #    Values(s) in this dictionary can be called by using 'key'
        #    Example:
        #
        #        wave['Hm0']         : Contain zero-moment wave height
        #        wave['Tp']          : Contain peak wave period
        #        wave['Field_Names'] : Contain key (variable) names in the wave dictionary
        #        wave['Burst_Data']  : Contain data for each burst
        #
        #--------------------------------------------------------------------------
        #Load data
        
        #Import required packages
        #https://stackoverflow.com/questions/38087060/using-import-inside-class/38087292
        
        #import scientimate as sm
        import numpy as np
        import os
        import warnings

        #currentpath=pwd
        #cd(InputFileFolder)
        d=(self.data)
        
        #Check if inputs are column vectors
        #if isrow(d)==1:
        #    d=d'
        
        #Check data for NaN
        if np.sum(np.isnan(d))!=0:
            #error('Input file contains NaN value(s), Oceanlyz will be terminated.')
            warnings.warn('Input file contains NaN value(s).')
            warnings.warn('NaN value(s) are replaced by linearly interpolated value(s).')
            warnings.warn('Oceanlyz continues with modified data.')
            
            #Replacing NaN values
            Indx=np.linspace(0,len(d)-1,len(d))
            d=np.interp(Indx,Indx(np.isnan(d)==0),d(np.isnan(d)==0))

        
        #Check data for Inf
        if np.sum(np.isinf(d))!=0:
            #error('Input file contains Inf value(s), Oceanlyz will be terminated.')
            warnings.warn('Input file contains Inf value(s).')
            warnings.warn('Inf value(s) are replaced by linearly interpolated value(s).')
            warnings.warn('Oceanlyz continues with modified data.')
            
            #Replacing Inf values
            Indx=np.linspace(0,len(d)-1,len(d))
            d=np.interp(Indx,Indx(np.isinf(d)==0),d(np.isinf(d)==0))

        
        #Check data for zero values
        if np.sum(d==0)!=0:
            warnings.warn('Input file contains Zero value(s), Oceanlyz continues with current data.')

        
        #--------------------------------------------------------------------------
        
        #Calculate number of sample in 1 burst
        n_sample=self.fs*self.burst_duration #Number of sample in 1 burst
        
        #Make sure n_burst and n_sample are int
        #self.n_burst = int(self.n_burst)
        #n_sample = int(n_sample)

        #CALLING-FUNCTION----------------------------------------------------------
        #Call calculation functions

        if self.InputType=='pressure':
            d=d/(self.Rho*9.81)

        if ((self.InputType=='pressure') and (self.fmaxpcorrCalcMethod=='auto')):
            autofmaxpcorr='on'
        elif ((self.InputType=='pressure') and (self.fmaxpcorrCalcMethod=='user')):
            autofmaxpcorr='off'

        
        if self.InputType=='waterlevel':
            pressureattenuation='off'
        elif ((self.InputType=='pressure') and (self.Kpafterfmaxpcorr=='constant')):
            pressureattenuation='all'
        elif ((self.InputType=='pressure') and (self.Kpafterfmaxpcorr=='one')):
            pressureattenuation='on'


        if self.dispout=='yes':
            dispout='on'
        elif self.dispout=='no':
            dispout='off'


        #Import functions
        #OceanlyzFolder=os.getcwd() #Current (OCEANLYZ) path
        #os.chdir('.\\Functions') #Change current path to Functions folder
        from .PcorFFTFun import PcorFFTFun
        from .PcorZerocrossingFun import PcorZerocrossingFun
        from .SeaSwellFun import SeaSwellFun
        from .WaveSpectraFun import WaveSpectraFun
        from .WaveZerocrossingFun import WaveZerocrossingFun
        #os.chdir(OceanlyzFolder) #Change current path to OCEANLYZ folder

        #Initialize array
        ini_arr=np.zeros(self.n_burst) #Initialize array
        ini_arr_f_Syy=np.zeros((self.n_burst,int(self.nfft/2+1))) #Initialize array to store spectrum data
        ini_arr_Eta=np.zeros((self.n_burst,n_sample)) #Initialize array to store surface elevation data
        ini_arr_burst_data=np.zeros((self.n_burst,n_sample)) #Initialize array to store burst data
        if self.module==1:
            wave={'Hm0':ini_arr.copy(), 'Tp':ini_arr.copy(), 'fp':ini_arr.copy(), 'f':ini_arr_f_Syy.copy(), 'Syy':ini_arr_f_Syy.copy(), 'Burst_Data':ini_arr_burst_data.copy()} #Initialize dictionary

        elif self.module==2:
            wave={'Hs':ini_arr.copy(), 'Hz':ini_arr.copy(), 'Tz':ini_arr.copy(), 'Ts':ini_arr.copy(), 'Burst_Data':ini_arr_burst_data.copy()} #Initialize dictionary

        elif self.module==3:
            wave={'Eta':ini_arr_Eta.copy(), 'Burst_Data':ini_arr_burst_data.copy()} #Initialize dictionary

        elif self.module==4:
            wave={'Eta':ini_arr_Eta.copy(), 'Burst_Data':ini_arr_burst_data.copy()} #Initialize dictionary

        elif self.module==5:
            wave={'Hm0':ini_arr.copy(), 'Hm0sea':ini_arr.copy(), 'Hm0swell':ini_arr.copy(), 'Tp':ini_arr.copy(), 'Tpsea':ini_arr.copy(), 'Tpswell':ini_arr.copy(), 'fp':ini_arr.copy(), 'fseparation':ini_arr.copy(), 'f':ini_arr_f_Syy.copy(), 'Syy':ini_arr_f_Syy.copy(), 'Burst_Data':ini_arr_burst_data.copy()} #Initialize dictionary

        elif self.module==6:
            wave={'Eta':ini_arr_Eta.copy(), 'Hm0':ini_arr.copy(), 'Tp':ini_arr.copy(), 'fp':ini_arr.copy(), 'f':ini_arr_f_Syy.copy(), 'Syy':ini_arr_f_Syy.copy(), 'Burst_Data':ini_arr_burst_data.copy()} #Initialize dictionary

        elif self.module==7:
            wave={'Eta':ini_arr_Eta.copy(), 'Hs':ini_arr.copy(), 'Hz':ini_arr.copy(), 'Tz':ini_arr.copy(), 'Ts':ini_arr.copy(), 'Burst_Data':ini_arr_burst_data.copy()} #Initialize dictionary

        elif self.module==8:
            wave={'Eta':ini_arr_Eta.copy(), 'Hm0':ini_arr.copy(), 'Hm0sea':ini_arr.copy(), 'Hm0swell':ini_arr.copy(), 'Tp':ini_arr.copy(), 'Tpsea':ini_arr.copy(), 'Tpswell':ini_arr.copy(), 'fp':ini_arr.copy(), 'fseparation':ini_arr.copy(), 'f':ini_arr_f_Syy.copy(), 'Syy':ini_arr_f_Syy.copy(), 'Burst_Data':ini_arr_burst_data.copy()} #Initialize dictionary


        #Calculation functions
        for i in range(0,self.n_burst,1):
            
            if self.dispout=='yes':
                Step='Burst = '+str(i+1)
                print('--------------------------------------------------')
                print(Step)
                #if ((self.module==1) or (self.module==5) or (self.module==6) or (self.module==8)):
                #    hold on
        
            #Load burst data
            j1=i*n_sample
            j2=(i+1)*n_sample
            input_data=d[j1:j2]
            
            #Calculate mean water depth
            if self.InputType=='waterlevel':
                h=np.mean(input_data) #Calculating mean water depth from water depth data
            elif self.InputType=='pressure':
                h=np.mean(input_data)+self.heightfrombed #Calculating mean water depth from pressure data

            if h<=0:
                warnings.warn('Mean water depth is Zero or negative, Oceanlyz continues with mean water depth=0.001 m.')
                h=0.001

            
            #Call function
            if self.module==1:
                wave['Hm0'][i],_,_,wave['Tp'][i],wave['fp'][i],wave['f'][i,:],wave['Syy'][i,:]=WaveSpectraFun(input_data,self.fs,self.burst_duration,self.nfft,h,self.heightfrombed,self.fmin,self.fmax,self.ftailcorrection,self.tailpower,self.mincutoff,self.maxcutoff,self.tailcorrection,dispout)
                wave['Field_Names'] = ['Hm0, Tp, fp, f, Syy, Field_Names, Burst_Data']
        
            elif self.module==2:
                wave['Hs'][i],wave['Hz'][i],wave['Tz'][i],wave['Ts'][i],_,_=WaveZerocrossingFun(input_data,self.fs,self.burst_duration,'off')
                wave['Field_Names'] = ['Hs, Hz, Tz, Ts,  Field_Names, Burst_Data']
            
            elif self.module==3:
                wave['Eta'][i,:],_=PcorFFTFun(input_data,self.fs,self.burst_duration,self.nfft,h,self.heightfrombed,self.fminpcorr,self.fmaxpcorr,self.ftailcorrection,pressureattenuation,autofmaxpcorr,'off')
                wave['Field_Names'] = ['Eta, Field_Names, Burst_Data']
        
            elif self.module==4:
                wave['Eta'][i,:]=PcorZerocrossingFun(input_data,self.fs,self.burst_duration,h,self.heightfrombed,'off')
                wave['Field_Names'] = ['Eta, Field_Names, Burst_Data']
            
            elif self.module==5:
                wave['Hm0'][i],wave['Hm0sea'][i],wave['Hm0swell'][i],wave['Tp'][i],wave['Tpsea'][i],wave['Tpswell'][i],wave['fp'][i],wave['fseparation'][i],wave['f'][i,:],wave['Syy'][i,:]=SeaSwellFun(input_data,self.fs,self.burst_duration,self.nfft,h,self.fmin,self.fmax,self.ftailcorrection,self.tailpower,self.fpminswell,self.fmaxswell,self.mincutoff,self.maxcutoff,self.tailcorrection,dispout)
                wave['Field_Names'] = ['Hm0, Hm0sea, Hm0swell, Tp, Tpsea, Tpswell, fp, fseparation, f, Syy, Field_Names, Burst_Data']
        
            elif self.module==6:
                wave['Eta'][i,:],ftailcorrection=PcorFFTFun(input_data,self.fs,self.burst_duration,self.nfft,h,self.heightfrombed,self.fminpcorr,self.fmaxpcorr,self.ftailcorrection,pressureattenuation,autofmaxpcorr,'off') 
                wave['Hm0'][i],_,_,wave['Tp'][i],wave['fp'][i],wave['f'][i,:],wave['Syy'][i,:]=WaveSpectraFun((wave['Eta'][i,:]),self.fs,self.burst_duration,self.nfft,h,self.heightfrombed,self.fmin,self.fmax,self.ftailcorrection,self.tailpower,self.mincutoff,self.maxcutoff,self.tailcorrection,dispout)
                wave['Field_Names'] = ['Eta, Hm0, Tp, fp, f, Syy, Field_Names, Burst_Data']
        
            elif self.module==7:
                wave['Eta'][i,:]=PcorZerocrossingFun(input_data,self.fs,self.burst_duration,h,self.heightfrombed,'off')
                wave['Hs'][i],wave['Hz'][i],wave['Tz'][i],wave['Ts'][i],_,_=WaveZerocrossingFun((wave['Eta'][i,:]),self.fs,self.burst_duration,'off')
                wave['Field_Names'] = ['Eta, Hs, Hz, Tz, Ts, Field_Names, Burst_Data']
        
            elif self.module==8:
                wave['Eta'][i,:],ftailcorrection=PcorFFTFun(input_data,self.fs,self.burst_duration,self.nfft,h,self.heightfrombed,self.fminpcorr,self.fmaxpcorr,self.ftailcorrection,pressureattenuation,autofmaxpcorr,'off')
                wave['Hm0'][i],wave['Hm0sea'][i],wave['Hm0swell'][i],wave['Tp'][i],wave['Tpsea'][i],wave['Tpswell'][i],wave['fp'][i],wave['fseparation'][i],wave['f'][i,:],wave['Syy'][i,:]=SeaSwellFun((wave['Eta'][i,:]),self.fs,self.burst_duration,self.nfft,h,self.fmin,self.fmax,self.ftailcorrection,self.tailpower,self.fpminswell,self.fmaxswell,self.mincutoff,self.maxcutoff,self.tailcorrection,dispout)
                wave['Field_Names'] = ['Eta, Hm0, Hm0sea, Hm0swell, Tp, Tpsea, Tpswell, fp, fseparation, f, Syy, Field_Names, Burst_Data']
            
            
            #self.dispout=='yes':
            #    wb=waitbar(i/self.n_burst)
            #    waitbar(i/self.n_burst,wb,sprintf('Percentage = #0.2f',i/self.n_burst*100))
            #else:
            #    fprintf('#14s   #g  #s   #g \n','burst:',i,'out of',self.n_burst)

            if self.dispout=='no':
                print('\n burst {} out of {}'.format(i+1,self.n_burst))
        
            wave['Burst_Data'][i,:]=input_data.copy() #Save input burst data

        return wave
        

    #==========================================================================
    def runoceanlyz(self):
        #--------------------------------------------------------------------------
        #Import required packages
        #https://stackoverflow.com/questions/38087060/using-import-inside-class/38087292
        
        import datetime
        import warnings
        #import os
        #import sys

        #Print

        CurrentDate=datetime.datetime.now().year
        print('--------------------------------------------------')
        print('OCEANLYZ Ver 2.0')
        print('www.ArashKarimpour.com')
        print('Copyright (C) 2012 -',CurrentDate,' Arash Karimpour')
        #print('--------------------------------------------------')

        #--------------------------------------------------------------------------
        #Turn off warning

        warnings.filterwarnings('ignore')

        #--------------------------------------------------------------------------
        #Addinng the OCEANLYZ folder and its subfolders to the search path

        #OceanlyzFolder=os.getcwd() #Current (OCEANLYZ) path
        #OceanlyzPath=os.path.dirname(OceanlyzFolder) #Generating path for OCEANLYZ folder and its subfolders
        #sys.path.append(OceanlyzPath)

        #FUNCTION------------------------------------------------------------------
        #Calling main calculating function
        #https://stackoverflow.com/questions/34453826/calling-method-to-another-method-in-python

        self.module=self.oceanlyzmodule()

        #--------------------------------------------------------------------------
        #Calculate wave properties

        print('Calculating wave properties')

        self.wave=self.oceanlyzecalcwave()


        #Output fields
        print('--------------------------------------------------')
        print('Output is a Python dictionary named "obj.wave"')
        print('Values(s) in a dictionary "wave" can be called by using "key"')
        print('Example: Output for a peak wave period is : "obj.wave["Tp"]"')
        print('Key names may be obtained from obj.wave.keys() command')
        print('Also, obj.wave["Field_Names"] contains key names in the wave dictionary')
        print('Output key (field) names are')
        for key, value in self.wave.items():
            print (key)
        print('--------------------------------------------------')
        print('Calculation finished')
        print('--------------------------------------------------')
        
        #--------------------------------------------------------------------------
        #Turn on warning

        warnings.resetwarnings()

        #--------------------------------------------------------------------------

#--------------------------------------------------------------------------
