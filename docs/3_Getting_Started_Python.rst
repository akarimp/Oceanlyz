Getting Started (Python)
========================

In order to use Python version of OCEANLYZ toolbox, first, Python programming language, and then, the OCEANLYZ package should be installed.


Installing
----------

To use Python version of OCEANLYZ toolbox:

* Install Python
* Install OCEANLYZ

**1) Install Python**

First, you need to install Python programming language.

* Method 1:
    Install pure Python from https://www.python.org and then use the **pip** command to install required packages
* Method 2 (Recommended):
    Install Anaconda Python distribution from https://www.anaconda.com and then use the **conda** command to install required packages

**2) Install OCEANLYZ**

After Python is installed, you need to install OCEANLYZ package.

To install OCEANLYZ via pip (https://pypi.org/project/oceanlyz) if you use pure Python:

.. code:: python

    pip install oceanlyz

To install OCEANLYZ via Anaconda cloud (https://anaconda.org/akarimp/oceanlyz) if you use Anaconda Python distribution:

.. code:: python

    conda install -c akarimp oceanlyz


Operating System
----------------

This code can be run on Microsoft Windows, Mac, and Linux. However, make sure any given path is compatible with a running operating system. In particular, "\\" is used in Windows path, while "/" is used in Mac or Linux path. For example, if a path is "C:\\" on Windows machine, it would be "C:/" on Mac or Linux.


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
* Import OCEANLYZ package by using "import oceanlyz" 
* Create OCEANLYZ object such as "ocn=oceanlyz.oceanlyz()" in Python and set/modify its properties based on the dataset and required analysis.
* Run a method as "ocn.runoceanlyz()" in Python to start calculations.
