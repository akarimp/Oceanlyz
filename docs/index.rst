.. YA LATIF

.. OCEANLYZ documentation master file, created by
   sphinx-quickstart on Wed Aug  2 15:40:03 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to OCEANLYZ's documentation!
====================================

OCEANLYZ, Ocean Wave Analyzing Toolbox, is a toolbox for analyzing the wave time series data collected by sensors in open body of water such as ocean, sea, and lake or in a laboratory.

OCEANLYZ GUI is a graphical user interface for the OCEANLYZ toolbox.

This toolbox provides spectral and zero-crossing wave analysis. It can calculate wave properties such as zero-moment wave height, significant wave height, mean wave height, peak wave period and mean period. This toolbox can correct and account for the pressure attention (pressure loss) in the water column for data collected by a pressure sensor. This toolbox can separate wind sea and swell energies and reports their properties.

:Name: OCEANLYZ
:Description: Ocean Wave Analyzing Toolbox
:Version: 2.0 (GUI 1.2)
:Requirements: MATLAB or GNU Octave | Python (3 or later) | GUI Version (Microsoft Windows 10 (64-bit))
:Developer: Arash Karimpour | http://www.arashkarimpour.com
:Documentation: https://oceanlyz.readthedocs.io
:Tutorial Video: `YouTube Playlist <https://www.youtube.com/playlist?list=PLcrFHi9M_GZRTCshcgujlK7y5ZPim6afM>`_
:Source Code: https://github.com/akarimp/Oceanlyz
:Report Issues: https://github.com/akarimp/Oceanlyz/issues

User Guide
----------

**Installing**

.. toctree::
    :maxdepth: 1

    1_Introduction.rst
    2_Getting_Started_Matlab.rst
    3_Getting_Started_Python.rst
    4_Getting_Started_GUI.rst

**Prepare Data File**

.. toctree::
    :maxdepth: 1

    5_Prepare_Input_Data_File_Matlab_Python.rst
    6_Prepare_Input_Data_File_GUI.rst
    7_Sample_Data_Files.rst

**Tutorials (MATLAB and Python)**

.. toctree::
    :maxdepth: 1

    8_Tutorial_Matlab.rst
    9_Tutorial_Python.rst

**Tutorials (GUI Version)**

.. toctree::
    :maxdepth: 1

    10_OCEANLYZ_GUI_Interface.rst
    11_Load_Data_Tab.rst
    12_Preprocess_Data_Tab.rst
    13_Analyze_Data_Tab.rst
    14_TimeSeries_Results_Tab.rst
    15_Spectrum_Results_Tab.rst
    16_Save_Open_Export_Results.rst

**Functions Reference**

.. toctree::
    :maxdepth: 2

    17_Functions_List.rst

.. toctree::
    :maxdepth: 1

    18_Changelog_Matlab_Python.rst
    19_Changelog_GUI.rst


**Technical Notes**

.. toctree::
    :maxdepth: 1

    20_Correct_Pressure_Data.rst
    21_Replace_Spectrum_Tail.rst


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


Recommended Applications
------------------------

.. list-table::
   :header-rows: 1
   :align: center

   * - .. figure:: figures/Figure_Oceanlyz_Logo.png
     - .. figure:: figures/Figure_ScientiMate_Logo.png
     - .. figure:: figures/Figure_AsanPlot_Screenshot.jpg

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


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
