.. YA LATIF

OCEANLYZ
========

OCEANLYZ, Ocean Wave Analyzing Toolbox, is a toolbox for analyzing the wave time series data collected by sensors in open body of water such as ocean, sea, and lake or in a laboratory.

OCEANLYZ GUI is a graphical user interface for the OCEANLYZ toolbox.

This toolbox provides spectral and zero-crossing wave analysis. It can calculate wave properties such as zero-moment wave height, significant wave height, mean wave height, peak wave period and mean period. This toolbox can correct and account for the pressure attention (pressure loss) in the water column for data collected by a pressure sensor. This toolbox can separate wind sea and swell energies and reports their properties.

:Name: OCEANLYZ
:Description: Ocean Wave Analyzing Toolbox
:Version: 2.0 (GUI 1.2)
:Requirements: MATLAB or GNU Octave | Python (3 or later) | GUI Version (Microsoft Windows 10 (64-bit))
:Developer: Arash Karimpour (http://www.arashkarimpour.com)
:Documentation: https://oceanlyz.readthedocs.io
:Tutorial Video: `YouTube Playlist <https://www.youtube.com/playlist?list=PLcrFHi9M_GZRTCshcgujlK7y5ZPim6afM>`_
:Source Code: https://github.com/akarimp/Oceanlyz
:Report Issues: https://github.com/akarimp/Oceanlyz/issues

GUI Version
===========

Installing (GUI Version)
------------------------

To use stand-alone GUI version of OCEANLYZ (Microsoft Windows (64-bit)):

* Download OCEANLYZ GUI setup file:

    * Version 1.2 (GitHub): https://github.com/akarimp/Oceanlyz/releases/download/2.0/oceanlyz_gui_1.2_win_x64_setup.exe

* Run setup file and follow setup wizard to install OCEANLYZ GUI
* Start OCEANLYZ GUI
* For documentation, use Help menu in OCEANLYZ GUI

MATLAB Version
==============

Installing (MATLAB)
-------------------

To use MATLAB version of OCEANLYZ toolbox:

* Install MATLAB or GNU Octave

    * MATLAB: https://www.mathworks.com
    * GNU Octave: https://octave.org

* Download OCEANLYZ:

    * Version 2.0 (GitHub): https://github.com/akarimp/Oceanlyz/releases/download/2.0/oceanlyz_2_0.zip
    * Version 1.5 (CNET): https://download.cnet.com/Oceanlyz/3000-2054_4-75833686.html
    * Version 1.5 (GitHub): https://github.com/akarimp/Oceanlyz/releases/download/1.5/oceanlyz_1_5.zip
    * Version 1.4 (GitHub): https://github.com/akarimp/Oceanlyz/releases/download/1.5/oceanlyz_1_4.zip

* Unzip OCEANLYZ in any location you choose such as “C:\\”

Required Package for MATLAB
---------------------------

MATLAB users need to install MATLAB Signal Processing Toolbox (https://www.mathworks.com/products/signal.html) for running the OCEANLYZ spectral analysis. It gives OCEANLYZ access to MATLAB Welch's power spectral density calculation. However, MATLAB Signal Processing Toolbox is not required for zero-crossing analysis. 

Required Package for GNU Octave
-------------------------------

GNU Octave users need to install/load GNU Octave Signal package (https://gnu-octave.github.io/packages/signal) for running the OCEANLYZ spectral analysis.
It gives OCEANLYZ access to GNU Octave Welch's power spectral density calculation. However, GNU Octave Signal package is not required for zero-crossing analysis.
The list of installed packages can be found by using a following command in a command window:

.. code:: octave
    
    >> pkg list

GNU Octave comes with Signal package but it needs to loaded every time GNU Octave starts. The Signal package can be loaded inside GNU Octave by using a following command in a command window (This should be done every time GNU Octave is opened):

.. code:: octave
    
    >> pkg load signal


If GNU Octave Signal Package is not already installed, it should be first installed from https://packages.octave.org, and then get loaded by using the following commands in the command window:

.. code:: octave

    >> pkg install "https://downloads.sourceforge.net/project/octave/Octave%20Forge%20Packages/Individual%20Package%20Releases/signal-1.4.5.tar.gz"
    >> pkg load signal

Quick Start (MATLAB)
--------------------

* Open MATLAB or GNU Octave
* Change a current folder (current directory) to a folder that contains OCEANLYZ toolbox, for example “C:\\oceanlyz”, in MATLAB or GNU Octave.
* Open a file named “oceanlyzinput.m” in MATLAB or GNU Octave editor and modify it based on the properties of the collected dataset and required analysis.
* Run a file named “RunOceanlyz.m” in MATLAB or GNU Octave to start calculations.

Python Version
==============

Installing (Python)
-------------------

To use Python version of OCEANLYZ toolbox:

* Install Python
* Install OCEANLYZ

**1) Install Python**

First, we need to install Python programming language.

* Method 1:
    Install pure Python from https://www.python.org and then use the **pip** command to install required packages
* Method 2 (Recommended):
    Install Anaconda Python distribution from https://www.anaconda.com and then use the **conda** command to install required packages

**2) Install OCEANLYZ**

After Python is installed, we need to install OCEANLYZ package.

To install OCEANLYZ via pip (https://pypi.org/project/oceanlyz):

.. code:: python

    pip install oceanlyz

To install OCEANLYZ via Anaconda cloud (https://anaconda.org/akarimp/oceanlyz):

.. code:: python

    conda install -c akarimp oceanlyz

Required Package for Python
---------------------------

Following packages are required:

* NumPy (https://numpy.org)
* SciPy (https://www.scipy.org)
* Matplotlib (https://matplotlib.org)

Quick Start (Python)
--------------------

* Open Python
* Import OCEANLYZ package by using "import oceanlyz" 
* Create OCEANLYZ object such as “ocn=oceanlyz.oceanlyz()” in Python and set/modify its properties based on the dataset and required analysis.
* Run a method as “ocn.runoceanlyz()” in Python to start calculations.

About
=====

Operating System
----------------

OCEANLYZ code can be run on Microsoft Windows, Mac, and Linux. However, make sure any given path is compatible with a running operating system. In particular, “\\” is used in Windows path, while “/” is used in Mac or Linux path. For example, if a path is “C:\\” on Windows machine, it would be “C:/” on Mac or Linux.

OCEANLYZ GUI can be run on Microsoft Windows (64-bit) machine.

Required Programming Language
-----------------------------

OCEANLYZ toolbox can be run by using MATLAB (https://www.mathworks.com), GNU Octave (https://octave.org), or Python (https://www.python.org). 

Citation
--------

Cite OCEANLYZ as:

Karimpour, A., & Chen, Q. (2017). Wind Wave Analysis in Depth Limited Water Using OCEANLYZ, a MATLAB toolbox. Computers & Geosciences.

Link: https://www.sciencedirect.com/science/article/pii/S0098300417306489

Recommended Books
-----------------

.. list-table::
   :header-rows: 1
   :align: center

   * - .. figure:: figures/Figure_Book_Coastal.jpg
     - .. figure:: figures/Figure_Book_Matlab.jpg
     - .. figure:: figures/Figure_Book_Python.jpg

   * - | **Ocean Wave Data Analysis**
       | Introduction to Time Series Analysis, Signal Processing, and Wave Prediction.
       |
       | Order at Amazon: https://www.amazon.com/dp/0692109978
       |
       | Read Online: https://github.com/akarimp/Ocean-Wave-Data-Analysis
     - | **Fundamentals of Data Science with MATLAB**
       | Introduction to Scientific Computing, Data Analysis, and Data Visualization.
       |
       | Order at Amazon: https://www.amazon.com/dp/1735241016
       |
       | Read Online: https://github.com/akarimp/Fundamentals-of-Data-Science-with-MATLAB
     - | **Principles of Data Science with Python**
       | Introduction to Scientific Computing, Data Analysis, and Data Visualization.
       |
       | Order at Amazon: https://www.amazon.com/dp/1735241008
       |
       | Read Online: https://github.com/akarimp/Principles-of-Data-Science-with-Python

Recommended Application
-----------------------

.. list-table::
   :header-rows: 1
   :align: center

   * - .. figure:: figures/Figure_Oceanlyz_Logo.jpg
     - .. figure:: figures/Figure_ScientiMate_Logo.jpg
     - .. figure:: figures/Figure_AsanPlot_Screenshot.jpg
            :width: 1777 px
            :height: 1002 px
            :scale: 20 %

   * - | **OCEANLYZ**
       | Ocean Wave Analyzing Toolbox
       |
       | Download: https://github.com/akarimp/Oceanlyz
     - | **ScientiMate**
       | Coastal and Ocean Data Analysis Library
       |
       | Download: https://github.com/akarimp/ScientiMate
     - | **AsanPlot**
       | Data cleaning and plotting software
       |
       | Download: https://github.com/akarimp/AsanPlot

License Agreement and Disclaimer
--------------------------------

OCEANLYZ: Ocean Wave Analyzing Toolbox

Copyright (c) 2023 Arash Karimpour

All rights reserved

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
