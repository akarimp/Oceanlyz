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

    [Eta]=PcorFFTFun(input,10,1024,2^10,1.07,0.05,0.04,0.8,'all','off','on');

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

This function can be used as a standalone command in Matlab/GNU Octave command line or it can be embedded in Matalb/GNU Octave script file (.m file) as:

.. code:: MATLAB

    [Eta,ftailcorrection]=PcorFFTFun(input,fs,duration,nfft,h,heightfrombed,fminpcorr,fmaxpcorr,ftailcorrection,pressureattenuation,autofmaxpcorr,dispout);

Example for using a provided sample input file:

.. code:: MATLAB

    [Eta]=PcorFFTFun(input,10,1024,2^10,1.07,0.05,0.04,0.8,'all','off','on');

In case of using a pressure attenuation correction function, choosing a proper upper limit for applying a correction is essential. If the upper limit is chosen unreasonably high, it will lead to a wrong over-estimation of the results. The under-estimation also can happen, if the upper limit is chosen unreasonably low. The waves that are large enough that can be sensed by a sensor should be included in attenuation correction. Note that pressure from small waves with high frequency can be damped in the water column and therefore may not reach a sensor depth. In that case, these small waves should not be included in attenuation correction. Wave height, wave frequency, water depth, height of a sensor above a seabed all play roles on if a wave effect reaches down to a sensor depth or not. Because of that, a deployment situation and wave properties should be used to define the highest frequency that a sensor senses its effect. Pressure correction should not be applied beyond that point. (refer to Applying Pressure Response Factor section)
