Introduction
============

OCEANLYZ, Ocean Wave Analyzing Toolbox, is a toolbox for analyzing the wave time series data collected by sensors in open body of water such as ocean, sea, and lake or in a laboratory.

OCEANLYZ GUI is a graphical user interface for the OCEANLYZ toolbox.

This toolbox provides spectral and zero-crossing wave analysis. It can calculate wave properties such as zero-moment wave height, significant wave height, mean wave height, peak wave period and mean period. This toolbox can correct and account for the pressure attention (pressure loss) in the water column for data collected by a pressure sensor. This toolbox can separate wind sea and swell energies and reports their properties.

Selected applications for OCEANLYZ toolbox
------------------------------------------

* Calculate wave properties from field/lab measured data.
* Use spectral analysis and zero-crossing method for wave analyzing.
* Partition wave spectra and separate wind-sea and swell data. 
* Correct pressure data that read by a pressure sensor to account for pressure attenuation in water depth.
* replace spectrum tail with tail of empirical spectrum (diagnostic tail), (MATLAB and Python Versions).

Selected parameters that can be calculated with OCEANLYZ toolbox
----------------------------------------------------------------

**Wave Height and Spectrum**

* Zero-Moment Wave Height
* Sea/Swell Wave Height 
* Significant Wave Height
* Mean Wave Height 
* Wave Power Spectral Density

**Wave Period**

* Peak Wave Frequency 
* Peak Wave Period 
* Peak Sea/Swell Period 
* Mean Wave Period
* Significant Wave Period

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

   * - .. figure:: figures/Figure_AsanPlot_Screenshot.jpg
            :width: 1777 px
            :height: 1002 px
            :scale: 20 %

   * - | **AsanPlot**
       | Data cleaning and plotting software.
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
