%.. ++++++++++++++++++++++++++++++++YA LATIF++++++++++++++++++++++++++++++++++
%.. +                                                                        +
%.. + Oceanlyz                                                               +
%.. + Ocean Wave Analyzing Toolbox                                           +
%.. + Ver 1.5                                                                +
%.. +                                                                        +
%.. + Developed by: Arash Karimpour                                          +
%.. + Contact     : www.arashkarimpour.com                                   +
%.. + Developed/Updated (yyyy-mm-dd): 2020-07-01                             +
%.. +                                                                        +
%.. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
%
%oceanlyzinput
%=============
%
%DESCRIPTION
%-----------
%
%Oceanlyz input file, containing input values and parameters
%
%.. LICENSE & DISCLAIMER
%.. -------------------- 
%.. Copyright (c) 2020 Arash Karimpour
%..
%.. http://www.arashkarimpour.com
%..
%.. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
%.. IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
%.. FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
%.. AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
%.. LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
%.. OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
%.. SOFTWARE.
%
%==========================================================================

%CODE

%INPUT FILE----------------------------------------------------------------
%Defines name and location of the input data file

InputFileName='waterdepthsample.mat';
%                                 :Enter name of the file contains water depth or surface elevation (Eta) time series
%                                 :Data should be in a single column vector file without any text, each burst of data should follow the previous burst
%                                 :Most file formats such as '.mat', '.txt', '.csv' can be imported

InputFileFolder='C:\oceanlyz\Sample';
%                                 :Enter a location of the file contains water depth or surface elevation (Eta) time series
%                                 :For Linux or Mac, use '/' instead of '\'

%SAVE FILE----------------------------------------------------------------
%Defines if to save output(s) and a location to be saved

SaveOutput='on'; 
%                                 :Defines if to save output(s) or not ('off': not save, 'on': save)

OutputFileFolder='C:\oceanlyz';
%                                 :Enter location of the output file to be saved
%                                 :For Linux or Mac, use '/' instead of '\'
%                                 :Output is a structure array
%                                 :Name of output file is 'wave.mat'
%                                 :After wave.mat is loaded in Matlab, field(s) in structure array can be called by using '.'
%                                 :Example: Output peak wave period is : "wave.Tp"

%INPUT PARAMETERS----------------------------------------------------------

%--------------------
%Defines analysis method
AnalysisMethod='spectral';
%                                 :Analysis method
%                                 :    AnalysisMethod='spectral': Use spectral analysis method / Fast Fourier Transform
%                                 :    AnalysisMethod='zerocross': Use zero-crossing method

%--------------------
%Defines if to calculate wave parameters or not
WaveParameterCalc='on';
%                                 :Defines if to calculate wave parameters or not
%                                 :    WaveParameterCalc='off': Does not calculate/report wave properties
%                                 :    Use WaveParameterCalc='off' to only report corrected water level data measured by a pressure sensor
%                                 :        If WaveParameterCalc='off', then pressureattenuation should be pressureattenuation='on' or 'all'
%                                 :        If WaveParameterCalc='off':
%                                 :            It reports corrected water level data measured by a pressure sensor 
%                                 :            by accounting for pressure attenuation (pressure loss) in depth 
%                                 :    WaveParameterCalc='on': Calculates/reports wave properties
%                                 :        If WaveParameterCalc='on' and pressureattenuation='on' or 'all':
%                                 :            It reports both waves and corrected water level data measured by a pressure sensor 

%--------------------
%Measurement properties
n_burst=5;
%                                 :Number of burst(s) in the input file
%                                 :    n_burst=total number of data points/(burst_duration*fs)
%                                 :    Example: 
%                                 :    For 12 bursts of data, which each burst has a duration of 30 minutes, and collected at sampling frequency of 10 Hz 
%                                 :    burst_duration=(30*60)
%                                 :    total number of data points=number of burst*burst_duration of each burst*sampling frequency
%                                 :    total number of data points=12*(30*60)*10
burst_duration=1024;
%                                 :Duration time that data collected in each burst in (second)
fs=10;
%                                 :Sampling frequency that data are collected at in (Hz)
heightfrombed=0.05;
%                                 :Pressure sensor height from a bed in (m)
%                                 :    Leave heightfrombed=0.0; if data is not measured by a pressure sensor or if a sensor sits on the seabed

%--------------------
%NFFT
nfft=2^10;
%                                 :NFFT for Fast Fourier Transform
%                                 :    Results will be reported for frequency range of 0 <= f <= (fs/2) with (nfft/2+1) data points
%                                 :    Example: If fs=4 Hz and nfft=1024, then output frequency has a range of 0 <= f <= 2 with 513 data points

%--------------------
%Swell values
seaswellCalc='off';
%                                 :Defines if to separate wind sea and swell waves or not
%                                 :    seaswellCalc='off': Does not separate wind sea and swell waves
%                                 :    seaswellCalc='on': Separates wind sea and swell waves
fminswell=0.1;
%                                 :Minimum frequency that swell can have (it is used for Tpswell calculation) in (Hz)
fmaxswell=0.25;
%                                 :Maximum frequency that swell can have (It is about 0.2 in Gulf of Mexico) in (Hz)

%--------------------
%Switching module on or off
%--------------------
pressureattenuation='all';
%                                 :Defines if to apply pressure attenuation factor or not 
%                                 :    Pressure attenuation factor is used to account for pressure attenuation (pressure loss) in depth
%                                 :    pressureattenuation='off': No pressure attenuation is applied
%                                 :    pressureattenuation='on': Pressure attenuation is applied without correction after fmaxpcorr
%                                 :    pressureattenuation='all': Pressure attenuation is applied with constant correction after fmaxpcorr
%                                 :        For pressureattenuation='on' or 'all', input data should be water depth
autofmaxpcorr='on';
%                                 :Defines if to calculate fmaxpcorr and ftailcorrection based on water depth or not
%                                 :    Code calculate a maximum frequency that a pressure attenuation factor should be applied up to that
%                                 :    autofmaxpcorr='off': Does not calculate fmaxpcorr and ftailcorrection based on water depth
%                                 :    autofmaxpcorr='on': Calculate fmaxpcorr and ftailcorrection based on water depth
fminpcorr=0.15;
%                                 :Minimum frequency that automated calculated fmaxpcorr can have if autofmaxpcorr='on' in (Hz)
%                                 :    If autofmaxpcorr='on', then fmaxpcorr will be checked to be larger or equal to fminpcorr
fmaxpcorr=0.55;
%                                 :Maximum frequency for applying pressure attenuation factor in (Hz)
%                                 :    Pressure attenuation factor is not applied on frequency larger than fmaxpcorr

%--------------------
mincutoff='on';
%                                 :Defines if to cut off the spectrum below fmin, i.e. where f<fmin, or not
%                                 :    mincutoff='off': Does not cut off spectrum below fmin
%                                 :    mincutoff='on': Cuts off spectrum below fmin
fmin=0.04;
%                                 :Minimum frequency to cut off the lower part of spectrum in (Hz)
%                                 :    If mincutoff='on', then results with frequency f<fmin will be removed from analysis
%                                 :    It is a simple high pass filter

%--------------------
maxcutoff='on';
%                                 :Defines if to cut off the spectrum beyond fmax, i.e. where f>fmax, or not
%                                 :    maxcutoff='off': Does not cut off spectrum beyond fmax
%                                 :    maxcutoff='on': Cut off spectrum beyond fmax
fmax=1;
%                                 :Maximum frequency to cut off the upper part of spectrum in (Hz)
%                                 :    If maxcutoff='on', then results with frequency f>fmax will be removed from analysis
%                                 :    It is a simple low pass filter

%--------------------
tailcorrection='off';
%                                 :Defines if to apply diagnostic tail correction or not 
%                                 :    tailcorrection='off': Does not apply diagnostic tail
%                                 :    tailcorrection='jonswap': Applies JONSWAP Spectrum tail
%                                 :    tailcorrection='tma': Applies TMA Spectrum tail
%                                 :        For tailcorrection='tma', input data should be water depth
ftailcorrection=0.9;
%                                 :Frequency that diagnostic tail applies after that in (Hz)
%                                 :    ftailcorrection is typically set at 2.5fm where fm=1/Tm01
tailpower=-5;
%                                 :Power that a diagnostic tail will be applied based on that 
%                                 :    Diagnostic tail will be proportional with (f^tailpower)
%                                 :    tailpower=-3 for shallow water, tailpower=-5 for deep water

%--------------------
dispout='on';
%                                 :Defines if to plot spectrum or not
%                                 :    dispout='off': Does not plot
%                                 :    dispout='on': Plot
%--------------------

%--------------------------------------------------------------------------
