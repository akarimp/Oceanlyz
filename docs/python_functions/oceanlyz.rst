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

Following properties are required for all abalysis

data=[]
    Water level (water surface elevation, Eta), water depth, or water pressure time series
        | Data should be a single column array (column vector) without any text
        | Each burst of data should follow the previous burst without any void

InputType='waterlevel'
    Define input data type
        InputType='waterlevel': Input data is water level or water depth in (m)
            If InputType='waterlevel' then OutputType='wave'
        InputType='pressure': Input data are water pressure measured by a pressure sensor in (N/m^2)
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
        | Kpafterfmaxpcorr='nochange': Kp is not changed for frequency larger than fmaxpcorr 
        | Kpafterfmaxpcorr='one': Kp=1 for frequency larger than fmaxpcorr 
        | Kpafterfmaxpcorr='constant': Kp for f larger than fmaxpcorr stays equal to Kp at fmaxpcorr (constant)
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
