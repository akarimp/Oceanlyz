.. YA LATIF

.. OCEANLYZ documentation master file, created by
   sphinx-quickstart on Tue Jan 18 15:57:08 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to OCEANLYZ's documentation!
====================================

OCEANLYZ, Ocean Wave Analyzing Toolbox, is a toolbox for analyzing the wave time series data collected by sensors in open body of water such as ocean, sea, and lake or in a laboratory.

This toolbox contains functions that each one is suitable for a particular purpose. Both spectral and zero-crossing methods are offered for wave analysis. This toolbox can calculate wave properties such as zero-moment wave height, significant wave height, mean wave height, peak wave period and mean period. This toolbox can correct and account for the pressure attention (pressure loss) in the water column for data collected by a pressure sensor. This toolbox can separate wind sea and swell energies and reports their properties.

:Name: OCEANLYZ
:Description: Ocean Wave Analyzing Toolbox
:Version: 2.0
:Requirements: MATLAB, or GNU Octave, or Python (3 or later)
:Developer: Arash Karimpour (http://www.arashkarimpour.com)
:Documentation: https://oceanlyz.readthedocs.io
:Tutorial Video: `YouTube Playlist <https://www.youtube.com/playlist?list=PLcrFHi9M_GZRTCshcgujlK7y5ZPim6afM>`_
:Source Code: https://github.com/akarimp/oceanlyz
:Report Issues: https://github.com/akarimp/oceanlyz/issues

User Guide
----------

**Setup and Usage**

.. toctree::
    :maxdepth: 1

    1_Introduction.rst
    2_Getting_Started_Matlab.rst
    3_Getting_Started_Python.rst

**Functions Reference**

.. toctree::
    :maxdepth: 2

    4_Functions_List.rst

.. toctree::
    :maxdepth: 1

    12_Changelog.rst

**Example**

.. toctree::
    :maxdepth: 1

    5_Example_Matlab.rst
    6_Example_Python.rst

**Prepare Data File**

.. toctree::
    :maxdepth: 1

    7_Prepare_Input_Data_File.rst
    8_Sample_Data_Files.rst

**Technical Notes**

.. toctree::
    :maxdepth: 1

    9_Correct_Pressure_Data.rst
    10_Replace_Spectrum_Tail.rst


Recommended Books
-----------------

.. list-table::
   :header-rows: 1
   :align: center

   * - .. figure:: figures/Figure_Book_Coastal.jpg
     - .. figure:: figures/Figure_Book_Python.jpg
     - .. figure:: figures/Figure_Book_Matlab.jpg

   * - | **Ocean Wave Data Analysis**
       | Introduction to Time Series Analysis, Signal Processing, and Wave Prediction.
       |
       | Order at Amazon: https://www.amazon.com/dp/0692109978
     - | **Principles of Data Science with Python**
       | Introduction to Scientific Computing, Data Analysis, and Data Visualization.
       |
       | Order at Amazon: https://www.amazon.com/dp/1735241008
     - | **Fundamentals of Data Science with MATLAB**
       | Introduction to Scientific Computing, Data Analysis, and Data Visualization.
       |
       | Order at Amazon: https://www.amazon.com/dp/1735241016

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
