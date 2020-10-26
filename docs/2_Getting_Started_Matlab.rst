Getting Started (MATLAB Version)
================================

In order to use MATLAB version of OCEANLYZ toolbox, first, one of the MATLAB or GNU Octave programming language along with required packages should be installed (Refer to required packages for MATLAB/GNU Octave). 


Installation
------------

To use MATLAB version of OCEANLYZ toolbox:

* Install MATLAB or GNU Octave
* Download OCEANLYZ:

    | GitHub: https://github.com/akarimp/oceanlyz/releases/download/2.0/oceanlyz_2_0.zip 
    | CNET: https://download.cnet.com/Oceanlyz/3000-2054_4-75833686.html

* Unzip OCEANLYZ in any location you choose such as “C:\\”

One way to access OCEANLYZ is to copy OCEANLYZ files and its sub-folders in your desire working directory and then use it there.
Another option is to add OCEANLYZ folder to MATLAB path. By doing that, you always have access to OCEANLYZ from any working directory.
For example, if OCEANLYZ files are in “C:\\oceanlyz” folder then it can be added to path as:

.. code:: MATLAB

    OceanlyzPath=genpath('C:\oceanlyz'); %Generating path for OCEANLYZ folder and its sub-folders
    addpath(OceanlyzPath);

To remove OCEANLYZ from the path use:

.. code:: MATLAB

    rmpath(OceanlyzPath);


Operating System
----------------

This code can be run on Windows, Mac and Linux. However, make sure any given path is compatible with a running operating system. In particular, “\\” is used in Windows path, while “/” is used in Mac or Linux path. For example, if a path is “C:\\” on Windows machine, it would be “C:/” on Mac or Linux.


Required Programing Language
----------------------------

The MATLAB version of this toolbox can be run by using MATLAB (https://www.mathworks.com) or GNU Octave (https://www.gnu.org/software/octave). 


Required Package for MATLAB
---------------------------

MATLAB users need to install MATLAB Signal Processing Toolbox (https://www.mathworks.com/products/signal.html) for running the OCEANLYZ spectral analysis. It gives OCEANLYZ access to MATLAB Welch's power spectral density calculation. However, MATLAB Signal Processing Toolbox it is not required for zero-crossing analysis. 


Required Package for GNU Octave
-------------------------------

GNU Octave users need to install/load GNU Octave Signal package (https://octave.sourceforge.io/signal/index.html) for running the OCEANLYZ spectral analysis. It gives OCEANLYZ access to GNU Octave Welch's power spectral density calculation. However, GNU Octave Signal package it is not required for zero-crossing analysis.

GNU Octave comes with Signal package but it needs to loaded every time GNU Octave starts. The Signal package can be loaded inside GNU Octave by using a following command in a command window (This should be done every time GNU Octave is opened):


.. code:: octave
    
    >> pkg load signal


If GNU Octave Signal Package is not already installed, it should be first installed from Octave Forge (https://octave.sourceforge.io), and then get loaded by using the following commands in a command window:

.. code:: octave

    >> pkg install -forge signal
    >> pkg load signal


Quick Start
-----------

* Open MATLAB or GNU Octave
* Change a current folder (working directory) to a folder that contains OCEANLYZ files, for example “C:\\oceanlyz”, in MATLAB or GNU Octave.
* Create OCEANLYZ object such as “ocn=oceanlyz” in MATLAB or GNU Octave and set/modify its properties based on the dataset and required analysis.
* Run a method as “ocn.runoceanlyz()” in MATLAB or GNU Octave to start calculations.

Download Previous Version
-------------------------

Download previous MATLAB version of OCEANLYZ toolbox

* Ver 1.5: https://github.com/akarimp/oceanlyz/releases/download/1.5/oceanlyz_1_5.zip
* Ver 1.4: https://github.com/akarimp/oceanlyz/releases/download/1.5/oceanlyz_1_4.zip
