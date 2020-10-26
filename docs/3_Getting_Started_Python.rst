Getting Started (Python Version)
================================

The Python version of OCEANLYZ toolbox is part of ScintiMate package (https://scientimate.readthedocs.io).

In order to use Python version of OCEANLYZ toolbox, first, Python programming language, and then, the ScientiMate package should be installed.


Installation
------------

To use Python version of OCEANLYZ toolbox:

* Install Python
* Install ScientiMate (Python version of OCEANLYZ toolbox is part of ScintiMate package)

**1) Install Python**

First, we need to install Python programming language.

* Method 1:
    Install pure Python from https://www.python.org and then use the **pip** command to install required packages
* Method 2 (Recommended):
    Install Anaconda Python distribution from https://www.anaconda.com and then use the **conda** command to install required packages

**2) Install ScientiMate**

After Python is installed, we need to install ScientiMate package.

To install ScientiMate via pip (https://pypi.org/project/scientimate):

.. code:: python

    pip install scientimate

To install ScientiMate via Anaconda cloud (https://anaconda.org/akarimp/scientimate):

.. code:: python

     conda install -c akarimp scientimate


Operating System
----------------

This code can be run on Windows, Mac, and Linux. However, make sure any given path is compatible with a running operating system. In particular, “\\” is used in Windows path, while “/” is used in Mac or Linux path. For example, if a path is “C:\\” on Windows machine, it would be “C:/” on Mac or Linux.


Required Programing Language
----------------------------

The Python version of this toolbox can be run by using Python 3 or later (https://www.python.org or https://www.anaconda.com).


Required Package for Python
---------------------------

Following packages are required:

* NumPy (https://numpy.org)
* SciPy (https://www.scipy.org)
* Matplotlib (https://matplotlib.org)


Quick Start
-----------

* Open Python
* Import ScientiMate package by using "import scientimate as sm" 
* Create OCEANLYZ object such as “ocn=sm.oceanlyz()” in Python and set/modify its properties based on the dataset and required analysis.
* Run a method as “ocn.runoceanlyz()” in Python to start calculations.
