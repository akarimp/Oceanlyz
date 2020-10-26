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

scientimate.WaveZerocrossingFun
===============================

.. code:: python

    Hs,Hz,Tz,Ts,H,T=scientimate.WaveZerocrossingFun(input,fs,duration,dispout)

DESCRIPTION
-----------

Calculate wave properties using Up-going zero crossing method

INPUT
-----

input=importdata('h.mat')
                                Load water depth (h)/surface elevation (Eta) data and rename it "input" in (m)
fs=10
                                Sampling frequency that data collected at in (Hz)
duration=1024
                                Duration time that data collected in input in each burst in second
dispout='on'
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

.. code:: python

    Hs,Hz,Tz,Ts,H,T=WaveZerocrossingFun(water_pressure/(1000*9.81),10,1024,'on')

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
