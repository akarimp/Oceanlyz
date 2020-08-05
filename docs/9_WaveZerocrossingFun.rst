.. ++++++++++++++++++++++++++++++++YA LATIF++++++++++++++++++++++++++++++++++
.. +                                                                        +
.. + Oceanlyz                                                               +
.. + Ocean Wave Analyzing Toolbox                                           +
.. + Ver 1.5                                                                +
.. +                                                                        +
.. + Developed by: Arash Karimpour                                          +
.. + Contact     : www.arashkarimpour.com                                   +
.. + Developed/Updated (yyyy-mm-dd): 2020-07-01                             +
.. +                                                                        +
.. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

WaveZerocrossingFun
===================

.. code:: MATLAB

    [Hs,Hz,Tz,Ts,H,T]=WaveZerocrossingFun(input,fs,duration,dispout)

DESCRIPTION
-----------

Calculate wave properties using Up-going zero crossing method

INPUT
-----

input=importdata('h.mat');
                                Load water depth (h)/surface elevation (Eta) data and rename it "input" in (m)
fs=10;
                                Sampling frequency that data collected at in (Hz)
duration=1024;
                                Duration time that data collected in input in each burst in second
dispout='on';
                                Define to display outputs or not ('off': not display, 'on': display)

OUTPUT
------

Hs
                                Significant Wave Height (m)
Hz
                                Zero Crossing Mean Wave Height (m)
Tz
                                Zero Crossing Mean Wave Period (second)
Ts
                                Significant Wave Period (second)
H
                                Wave Height Data Series (m)
T
                                Wave Period Data Series (second)

EXAMPLE
-------

.. code:: MATLAB

    [Hs,Hz,Tz,Ts,H,T]=WaveZerocrossingFun(input,10,1024,'on');

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

In case that data are measured by a pressure sensor, data should be corrected for pressure attenuation. In that case, function “PcorFFTFun.m” or “PcorZerocrossingFun.m” should be called first to correct pressure (water depth) data before calculating wave properties. Results from either of those functions can be imported to this function for zero-crossing calculation of wave parameters. If provided “RunOceanlyz.m” file is used, it will do this procedure if proper input parameters are selected in “oceanlyzinput.m” file. Please read the note in “PcorFFTFun.m”.

This function can be used as a standalone command in Matlab/GNU Octave command line or it can be embedded in Matalb/GNU Octave script file (.m file) as:

.. code:: MATLAB

    [Hs,Hz,Tz,Ts,H,T]=WaveZerocrossingFun(input,fs,duration,dispout);

Example for using a provided sample input file:

.. code:: MATLAB

    [Hs,Hz,Tz,Ts,H,T]=WaveZerocrossingFun(input,10,1024,'on');
