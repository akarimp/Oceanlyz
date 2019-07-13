.. ++++++++++++++++++++++++++++++++YA LATIF++++++++++++++++++++++++++++++++++
.. +                                                                        +
.. + Oceanlyz                                                               +
.. + Ocean Wave Analyzing Toolbox                                           +
.. + Ver 1.4                                                                +
.. +                                                                        +
.. + Developed by: Arash Karimpour                                          +
.. + Contact     : www.arashkarimpour.com                                   +
.. + Developed/Updated (yyyy-mm-dd): 2019-07-01                             +
.. +                                                                        +
.. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

SeaSwellFun
===========

.. code:: MATLAB

    [Hm0,Hm0sea,Hm0swell,Tp,Tpsea,Tpswell,fp,fseparation,f,Syy]=SeaSwellFun(input,fs,duration,nfft,h,fmin,fmax,ftailcorrection,tailpower,fminswell,fmaxswell,mincutoff,maxcutoff,tailcorrection,dispout)

DESCRIPTION
-----------

Separate sea wave from swell wave

INPUT
-----

input=importdata('h.mat');
                                Load water depth (h)/surface elevation (Eta) data and rename it "input" in (m)
fs=10;
                                Sampling frequency that data collected at in (Hz)
duration=1024;
                                Duration time that data collected in input in each burst in second
nfft=2^10;
                                NFFT for Fast Fourier Transform
h=1;
                                Mean water depth in (m)
fmin=0.04;
                                Minimum frequency for cut off the lower part of spectra
fmax=1;
                                Maximum frequency for cut off the upper part of spectra
ftailcorrection=1;
                                Frequency that diagnostic tail apply after that (typically set at 2.5fm, fm=1/Tm01)
tailpower=-4;
                                Power that diagnostic tail apply based on that (-3 for shallow water to -5 for deep water)
fminswell=0.1;
                                Minimum frequency that is used for Tpswell calculation
fmaxswell=0.25;
                                Maximum frequency that swell can have, It is about 0.2 in Gulf of Mexico
mincutoff='off';
                                Define if to cut off the spectra below fmin
                                    mincutoff='off': Cutoff off

                                    mincutoff='on': Cutoff on
maxcutoff='off';
                                Define if to cut off the spectra beyond fmax
                                    maxcutoff='off': Cutoff off

                                    maxcutoff='on': Cutoff on
tailcorrection='off';
                                Define if to apply diagnostic tail correction or not 
                                    tailcorrection='off': Not apply

                                    tailcorrection='jonswap': JONSWAP Spectrum tail

                                    tailcorrection='tma': TMA Spectrum tail
dispout='on';
                                Define to display outputs or not ('off': not display, 'on': display)

OUTPUT
------

Hm0
                                Zero-Moment Wave Height (m)
Hm0sea
                                Sea Zero-Moment Wave Height (m)
Hm0swell
                                Swell Zero-Moment Wave Height (m)
Tp
                                Peak wave period (second)
Tpsea
                                Peak Sea period (second)
Tpswell
                                Peak Swell Period (second)
fp
                                Peak Wave Frequency (Hz)
f
                                Frequency (Hz)
fseparation
                                Sea and Swell Separation Frequency (Hz)
Syy
                                Wave Surface Elevation Power Spectrum (m^2s)

EXAMPLE
-------

.. code:: MATLAB

    [Hm0,Hm0sea,Hm0swell,Tp,Tpswell,fp,fseparation,f,Syy]= SeaSwellFun(input,10,1024,2^10,1.07,0.05,2,0.9,-4,0.1,0.25,'on','on','off','on');

.. LICENSE & DISCLAIMER
.. -------------------- 
.. Copyright (c) 2018 Arash Karimpour
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

NOTES
-----

In case that data are measured by a pressure sensor, data should be corrected for pressure attenuation. In that case, function “PcorFFTFun.m” or “PcorZerocrossingFun.m” should be called first to correct pressure (water depth) data before calculating wave properties. Results from either of those functions can be imported to this function for spectral analysis of wave parameters. If provided “RunOceanlyz.m” file is used, it will do this procedure if proper input parameters are selected in “oceanlyzinput.m” file. Please read the note in “PcorFFTFun.m”.

This function can be used as a standalone command in Matlab/GNU Octave command line or it can be embedded in Matalb/GNU Octave script file (.m file) as:

.. code:: MATLAB

    [Hm0,Hm0sea,Hm0swell,Tp,Tpsea,Tpswell,fp,fseparation,f,Syy]=SeaSwellFun(input,fs,duration,nfft,h,fmin,fmax,ftailcorrection,tailpower,fminswell,fmaxswell,mincutoff,maxcutoff,tailcorrection,dispout);

Example for using a provided sample input file:

.. code:: MATLAB

    [Hm0,Hm0sea,Hm0swell,Tp,Tpswell,fp,fseparation,f,Syy]= SeaSwellFun(input,10,1024,2^10,1.07,0.05,2,0.9,-4,0.1,0.25,'on','on','off','on');
