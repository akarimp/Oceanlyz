Getting Started (MATLAB)
========================

In order to use MATLAB version of OCEANLYZ toolbox, first, one of the MATLAB or GNU Octave programming language along with required packages should be installed (Refer to required packages for MATLAB/GNU Octave). 


Installing
----------

To use MATLAB version of OCEANLYZ toolbox:

* Install MATLAB or GNU Octave

    * MATLAB: https://www.mathworks.com
    * GNU Octave: https://octave.org

* Download OCEANLYZ:

    * Version 2.0 (GitHub): https://github.com/akarimp/Oceanlyz/releases/download/2.0/oceanlyz_2_0.zip
    * Version 1.5 (CNET): https://download.cnet.com/Oceanlyz/3000-2054_4-75833686.html
    * Version 1.5 (GitHub): https://github.com/akarimp/Oceanlyz/releases/download/1.5/oceanlyz_1_5.zip
    * Version 1.4 (GitHub): https://github.com/akarimp/Oceanlyz/releases/download/1.5/oceanlyz_1_4.zip

* Unzip OCEANLYZ in any location you choose such as "C:\\"
* Add OCEANLYZ folder to MATLAB or GNU Octave path


Add OCEANLYZ folder to MATLAB or GNU Octave path
------------------------------------------------

You may access OCEANLYZ by copying OCEANLYZ files and its sub-folders to your desire working directory and then use them there.
However, a better option is to add OCEANLYZ folder to MATLAB or GNU Octave path. By doing that, you always have access to OCEANLYZ from any working directory.
Remember, you need to add OCEANLYZ to path only once.

For example, if OCEANLYZ files are in "C:\\OCEANLYZ" folder, then:

To add OCEANLYZ to MATLAB or GNU Octave path, run following commands in the Command Window:

.. code:: MATLAB

    OceanlyzPath = genpath('C:\oceanlyz'); %Generating path for OCEANLYZ folder and its sub-folders
    addpath(OceanlyzPath); %Add OCEANLYZ folder to path

To remove OCEANLYZ from MATLAB or GNU Octave path, run following commands in the Command Window:

.. code:: MATLAB

    OceanlyzPath = genpath('C:\oceanlyz'); %Generating path for OCEANLYZ folder and its sub-folders
    rmpath(OceanlyzPath); %Remove OCEANLYZ folder from path
    %restoredefaultpath; %Restore path to factory-installed state


Operating System
----------------

This code can be run on Microsoft Windows, Mac and Linux. However, make sure any given path is compatible with a running operating system. In particular, "\\" is used in Windows path, while "/" is used in Mac or Linux path. For example, if a path is "C:\\" on Windows machine, it would be "C:/" on Mac or Linux.


Required Programing Language
----------------------------

The MATLAB version of this toolbox can be run by using MATLAB (https://www.mathworks.com) or GNU Octave (https://octave.org). 


Required Package for MATLAB
---------------------------

MATLAB users need to install MATLAB Signal Processing Toolbox (https://www.mathworks.com/products/signal.html) for running the OCEANLYZ spectral analysis. It gives OCEANLYZ access to MATLAB Welch's power spectral density calculation. However, MATLAB Signal Processing Toolbox is not required for zero-crossing analysis. 


Required Package for GNU Octave
-------------------------------

GNU Octave users need to install/load GNU Octave Signal package (https://gnu-octave.github.io/packages/signal) for running the OCEANLYZ spectral analysis.
It gives OCEANLYZ access to GNU Octave Welch's power spectral density calculation. However, GNU Octave Signal package is not required for zero-crossing analysis.
The list of the GNU Octave's installed packages can be found by running the following command in the Command Window:

.. code:: octave
    
    >> pkg list

GNU Octave comes with Signal package but it needs to loaded every time GNU Octave starts. The Signal package can be loaded inside GNU Octave by running the following command in the Command Window (This should be done every time GNU Octave is opened):

.. code:: octave
    
    >> pkg load signal

If GNU Octave Signal Package is not already installed, it should be first installed from https://packages.octave.org, and then get loaded by running the following commands in the Command Window:

.. code:: octave

    >> pkg install "https://downloads.sourceforge.net/project/octave/Octave%20Forge%20Packages/Individual%20Package%20Releases/signal-1.4.5.tar.gz"
    >> pkg load signal


Quick Start
-----------

* Open MATLAB or GNU Octave
* Change a current folder (working directory) to a folder that contains OCEANLYZ files, for example "C:\\oceanlyz", in MATLAB or GNU Octave.
* Create OCEANLYZ object such as "ocn=oceanlyz" in MATLAB or GNU Octave and set/modify its properties based on the dataset and required analysis.
* Run a method as "ocn.runoceanlyz()" in MATLAB or GNU Octave to start calculations.
