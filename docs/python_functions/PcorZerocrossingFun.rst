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

scientimate.PcorZerocrossingFun
===============================

.. code:: python

    Eta=scientimate.PcorZerocrossingFun(input,fs,duration,h,heightfrombed,dispout)

DESCRIPTION
-----------

Apply pressure correction factor to water depth data from pressure gauge reading using up-going zerocrossing method

INPUT
-----

input=importdata('h.mat')
                                Load water depth (h)/surface elevation (Eta) data and rename it "input" in (m)
fs=10
                                Sampling frequency that data collected at in (Hz)
duration=1024
                                Duration time that data collected in input in each burst in second
h=1
                                Mean water level (m)
heightfrombed=0.0
                                Sensor height from bed
dispout='on'
                                Define to display outputs or not ('off': not display, 'on': display)

OUTPUT
------

Eta
                                Corrected Water Surface Level Time Series in (m)

EXAMPLE
-------

.. code:: python

    Eta=PcorZerocrossingFun(input,10,1024,1.07,0.05,'on')

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
