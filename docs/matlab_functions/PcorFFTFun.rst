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
  
PcorFFTFun
==========

.. code:: MATLAB

    [Eta,ftailcorrection]=PcorFFTFun(input,fs,duration,nfft,h,heightfrombed,fminpcorr,fmaxpcorr,ftailcorrection,pressureattenuation,autofmaxpcorr,dispout)

DESCRIPTION
-----------

Apply pressure correction factor to water depth data from pressure gauge reading using FFT

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
heightfrombed=0.0;
                                Sensor height from bed
fminpcorr=0.15;
                                Minimum frequency that automated calculated fmaxpcorr can have if autofmaxpcorr='on' in (Hz)
fmaxpcorr=0.8;
                                Maximum frequency for applying pressure attenuation factor
ftailcorrection=1;
                                Frequency that diagnostic tail apply after that (typically set at 2.5fm, fm=1/Tm01)
pressureattenuation='all';
                                Define if to apply pressure attenuation factor or not 
                                    pressureattenuation='off': No pressure attenuation applied

                                    pressureattenuation='on': Pressure attenuation applied without correction after fmaxpcorr

                                    pressureattenuation='all': Pressure attenuation applied with constant correction after fmaxpcorr
autofmaxpcorr='on';
                                Define if to calculate fmaxpcorr and ftailcorrection based on water depth or not
                                    autofmaxpcorr='off': Off

                                    autofmaxpcorr='on': On
dispout='on';
                                Define to display outputs or not ('off': not display, 'on': display)

OUTPUT
------

Eta
                                Corrected Water Surface Level Time Series (m)

EXAMPLE
-------

.. code:: MATLAB

    [Eta,ftailcorrection]=PcorFFTFun(water_pressure/(1000*9.81),10,1024,256,1.07,0.05,0.15,0.8,1,'all','on','on')

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
