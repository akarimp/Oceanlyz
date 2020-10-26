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

scientimate.WaveSpectraFun
==========================

.. code:: python

    Hm0,Tm01,Tm02,Tp,fp,f,Syy=scientimate.WaveSpectraFun(input,fs,duration,nfft,h,heightfrombed,fmin,fmax,ftailcorrection,tailpower,mincutoff,maxcutoff,tailcorrection,dispout)

DESCRIPTION
-----------

Calculate wave properties from power spectral density

INPUT
-----

input=importdata('h.mat')
                                Load water depth (h)/surface elevation (Eta) data and rename it "input" in (m)
fs=10
                                Sampling frequency that data collected at in (Hz)
duration=1024
                                Duration time that data collected in input in each burst in second
nfft=2^10
                                NFFT for Fast Fourier Transform
h=1
                                Mean water depth in (m)
heightfrombed=0.0
                                Sensor height from bed
fmin=0.04
                                Minimum frequency for cut off the lower part of spectra
fmax=1
                                Maximum frequency for cut off the upper part of spectra
ftailcorrection=1
                                Frequency that diagnostic tail apply after that (typically set at 2.5fm, fm=1/Tm01)
tailpower=-4
                                Power that diagnostic tail apply based on that (-3 for shallow water to -5 for deep water)
mincutoff='off'
                                Define if to cut off the spectra below fmin
                                    mincutoff='off': Cutoff off

                                    mincutoff='on': Cutoff on
maxcutoff='off'
                                Define if to cut off the spectra beyond fmax
                                    maxcutoff='off': Cutoff off

                                    maxcutoff='on': Cutoff on
tailcorrection='off'
                                Define if to apply diagnostic tail correction or not 
                                    tailcorrection='off': Not apply

                                    tailcorrection='jonswap': JONSWAP Spectrum tail

                                    tailcorrection='tma': TMA Spectrum tail
dispout='on'
                                Define to display outputs or not ('off': not display, 'on': display)

OUTPUT
------

Hm0
                                Zero-Moment Wave Height (m)
Tm01
                                Wave Period from m01 (second), Mean Wave Period
Tm02
                                Wave Period from m02 (second), Mean Zero Crossing Period
Tp
                                Peak Wave Period (second)
fp
                                Peak Wave Frequency (Hz)
f
                                Frequency (Hz)
Syy
                                Wave Surface Elevation Power Spectrum (m^2s)

EXAMPLE
-------

.. code:: python

    Hm0,Tm01,Tm02,Tp,fp,f,Syy=WaveSpectraFun(water_pressure/(1000*9.81),10,1024,256,1.07,0.05,0.05,5,1,-5,'on','on','off','on')

.. LICENSE & DISCLAIMER
.. -------------------- 
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
