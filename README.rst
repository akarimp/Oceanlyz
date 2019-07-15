.. YA LATIF

OCEANLYZ
========

OCEANLYZ, Ocean Wave Analyzing Toolbox

MATLAB / GNU Octave Toolbox

:Developer: Arash Karimpour
:Website: http://www.arashkarimpour.com
:Download: http://www.arashkarimpour.com/oceanlyz.html
:Documentation: https://oceanlyz.readthedocs.io
:Source code: https://github.com/akarimp/oceanlyz
:Version: 1.4

OCEANLYZ, Ocean Wave Analyzing Toolbox, is a toolbox for analyzing the wave time series data collected by sensors in open body of water such as ocean, sea, and lake or in a laboratory.

This toolbox contains functions that each one is suitable for a particular purpose. Both spectral and zero-crossing methods are offered for wave analysis. This toolbox can calculate wave properties such as zero-moment wave height, significant wave height, mean wave height, peak wave period and mean period. This toolbox can correct and account for the pressure attention (pressure loss) in the water column for data collected by a pressure sensor. This toolbox can separate wind sea and swell energies and reports their properties.


Download
--------

To download Oceanlyz, visit http://www.arashkarimpour.com


Installation
------------

To use this toolbox, download and unzip it in any location you choose such as “C:\\”.


Operating System
----------------

This code can be run on Windows, Mac and Linux. However, make sure any given path is compatible with a running operating system. In particular, “\\” is used in Windows path, while “/” is used in Mac or Linux path. For example, if a path is “C:\\” on Windows machine, it would be “C:/” on Mac or Linux.


Required Programing Language
----------------------------

This toolbox can be run by using MATLAB (https://www.mathworks.com) or GNU Octave (https://www.gnu.org/software/octave). 


Required Package for MATLAB
---------------------------

MATLAB users need to install MATLAB Signal Processing Toolbox for running the Oceanlyz spectral analysis. It gives Oceanlyz access to MATLAB Welch's power spectral density calculation. However, MATLAB Signal Processing Toolbox it is not required for zero-crossing analysis. 


Required Package for GNU Octave
-------------------------------

GNU Octave users need to install/load GNU Octave Signal Package for running the Oceanlyz spectral analysis. It gives Oceanlyz access to GNU Octave Welch's power spectral density calculation. However, GNU Octave Signal Package it is not required for zero-crossing analysis.

GNU Octave Signal Package can be loaded inside GNU Octave by using a following command in a command window (This should be done every time GNU Octave is opened):


.. code:: octave
    
    >> pkg load signal


If GNU Octave Signal Package is not already installed, it should be first installed from Octave Forge (octave.sourceforge.io), and then get loaded by using the following commands in a command window:

.. code:: octave

    >> pkg install -forge signal
    >> pkg load signal


Quick Start
-----------

* Open MATLAB or GNU Octave
* Change a current folder (current directory) to a folder that contains OCEANLYZ toolbox, for example “C:\\oceanlyz”, in MATLAB or GNU Octave.
* Open a file named “oceanlyzinput.m” in MATLAB or GNU Octave editor and modify it based on the properties of the collected dataset and required analysis.
* Run a file named “RunOceanlyz.m” in MATLAB or GNU Octave to start calculations.

For more information, refer to “Tutorial” section.

Recommended Book
----------------

For more details on coastal and ocean wave data analysis refer to:

Karimpour A., (2018), Ocean Wave Data Analysis: Introduction to Time Series Analysis, Signal Processing, and Wave Prediction, KDP.

Book link: https://www.amazon.com/dp/0692109978

Citation
--------

Cite this toolbox as:

Karimpour, A., & Chen, Q. (2017). Wind Wave Analysis in Depth Limited Water Using OCEANLYZ, a MATLAB toolbox. Computers & Geosciences.

License Agreement and Disclaimer
--------------------------------

Copyright (c) 2018 Arash Karimpour

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
