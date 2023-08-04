#GUI for OCEANLYZ (originally developed by wxGlade 1.0.2, http://wxglade.sourceforge.net)
"""
.. ++++++++++++++++++++++++++++++++YA LATIF++++++++++++++++++++++++++++++++++
.. +                                                                        +
.. + Oceanlyz GUI                                                           +
.. + Ocean Wave Analyzing Toolbox                                           +
.. + Ver 1.2                                                                +
.. +                                                                        +
.. + Developed by: Arash Karimpour                                          +
.. + Contact     : www.arashkarimpour.com                                   +
.. + Developed/Updated (yyyy-mm-dd): 2023-08-01                             +
.. +                                                                        +
.. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

oceanlyz_gui (Python Version)
=============================

.. code:: python

    oceanlyz_gui

DESCRIPTION
-----------

| GUI for OCEANLYZ
| Calculate wave properties from water level or water pressure data
| For OCEANLYZ Document visit https://oceanlyz.readthedocs.io

Required Properties
-------------------

Following properties are required for all abalysis

data=[]
    Water level (water surface elevation, Eta), water depth, or water pressure time series
        | Data should be a single column array (column vector) without any text
        | Each burst of data should follow the previous burst without any void

InputType='waterlevel'
    Define input data type
        InputType='waterlevel': Input data is water level or water depth in (m)
            If InputType='waterlevel' then OutputType='wave'
        InputType='pressure': Input data are water pressure measured by a pressure sensor in (N/m^2)
            If InputType='pressure' then OutputType='waterlevel' or OutputType='wave+waterlevel'

OutputType='wave'
    Defines output data type
        | OutputType='wave': Calculate wave properties from water level or water depth data
        | OutputType='waterlevel': Calculate water level data from water pressure data measured by a pressure sensor
        | OutputType='wave+waterlevel': Calculate waves properties and water level data from water pressure data measured by a pressure sensor

AnalysisMethod='spectral'
    Analysis method
        | AnalysisMethod='spectral': Use spectral analysis method / Fast Fourier Transform
        | AnalysisMethod='zerocross': Use zero-crossing method

n_burst=1
    Number of burst(s) in the input file
        | n_burst = (total number of data points)/(burst_duration*fs)
        | Example:

            | Assume data are collected for 6 hours at a sampling frequency of fs=10 Hz
            | If data are analyzed at intervals of 30 minutes then there are 12 bursts (6 hours/30 minutes=12 bursts)
            | For 12 bursts of data, which each burst has a duration of 30 minutes, and collected at sampling frequency of fs=10 Hz 
            | burst_duration=(30 min * 60) = 1800 seconds
            | total number of data points=(number of burst)*(duration of each burst)*(sampling frequency)
            | total number of data points=(n_burst)*(burst_duration)*(fs)
            | total number of data points=12 * 1800 * 10

burst_duration=1024
    Duration time that data collected in each burst in (second)

fs=2
    Sampling frequency that data are collected at in (Hz)

Required Properties for Spectral Analysis
-----------------------------------------

Following properties are needed only if AnalysisMethod='spectral'


fmin=0.05
    Minimum frequency to cut off the spectrum below that, i.e. where f<fmin, in (Hz)
        | Results with frequency f<fmin will be removed from analysis
        | It should be between 0 and (fs/2)
        | It is a simple high pass filter
        | Only required if AnalysisMethod='spectral'

fmax=1e6
    Maximum frequency to cut off the spectrum beyond that, i.e. where f>fmax, in (Hz)
        | Results with frequency f>fmax will be removed from analysis
        | It should be between 0 and (fs/2)
        | It is a simple low pass filter
        | Only required if AnalysisMethod='spectral'

Required Properties for Pressure Data Analysis
----------------------------------------------

Following properties are needed only if InputType='pressure'

fmaxpcorrCalcMethod='auto'
    Define if to calculate fmaxpcorr and ftail or to use user defined
        | fmaxpcorrCalcMethod='user': use user defined value for fmaxpcorr
        | fmaxpcorrCalcMethod='auto': automatically define value for fmaxpcorr
        | Only required if InputType='pressure' and AnalysisMethod='spectral'

Kpafterfmaxpcorr='constant'
    Define a pressure response factor, Kp, value for frequency larger than fmaxpcorr
        | Kpafterfmaxpcorr='one': Kp=1 for frequency larger than fmaxpcorr 
        | Kpafterfmaxpcorr='constant': Kp for f larger than fmaxpcorr stays equal to Kp at fmaxpcorr (constant)
        | Kpafterfmaxpcorr='nochange': Kp is not changed for frequency larger than fmaxpcorr (Not implemented yet)
        | Only required if InputType='pressure' and AnalysisMethod='spectral'

fminpcorr=0.15
    Minimum frequency that automated calculated fmaxpcorr can have if fmaxpcorrCalcMethod='auto' in (Hz)
        | If fmaxpcorrCalcMethod='auto', then fmaxpcorr will be checked to be larger or equal to fminpcorr
        | It should be between 0 and (fs/2)
        | Only required if InputType='pressure' and AnalysisMethod='spectral'

fmaxpcorr=0.55
    Maximum frequency for applying pressure attenuation factor in (Hz)
        | Pressure attenuation factor is not applied on frequency larger than fmaxpcorr
        | It should be between 0 and (fs/2)
        | Only required if InputType='pressure' and AnalysisMethod='spectral'

heightfrombed=0.0
    Pressure sensor height from a bed in (m)
        Leave heightfrombed=0.0 if data are not measured by a pressure sensor or if a sensor sits on the seabed
        | Only required if InputType='pressure'

Optional Properties
-------------------

Following properties are optional

dispout='no'
    Define if to plot spectrum or not
        | dispout='no': Does not plot
        | dispout='yes': Plot

Rho=1000
    Water density (kg/m^3)
        Only required if InputType='pressure'

nfft=512
    Define number of data points in discrete Fourier transform
        | Should be 2^n
        | Results will be reported for frequency range of 0 <= f <= (fs/2) with (nfft/2+1) data points
        | Example: If fs=4 Hz and nfft=512, then output frequency has a range of 0 <= f <= 2 with 257 data points
        | Only required if AnalysisMethod='spectral'

SeparateSeaSwell='no'
    Define if to separate wind sea and swell waves or not
        | SeparateSeaSwell='yes': Does not separate wind sea and swell waves
        | SeparateSeaSwell='no': Separates wind sea and swell waves

fmaxswell=0.25
    Maximum frequency that swell can have (It is about 0.2 in Gulf of Mexico) in (Hz)
        | It should be between 0 and (fs/2)
        | Only required if SeparateSeaSwell='yes' and AnalysisMethod='spectral'

fpminswell=0.1
    Minimum frequency that swell can have (it is used for Tpswell calculation) in (Hz)
        | It should be between 0 and (fs/2)
        | Only required if SeparateSeaSwell='yes' and AnalysisMethod='spectral'

Methods
-------

oceanlyz_object.runoceanlyz()
    Run oceanlyz and calculate wave properties

Outputs
-------

oceanlyz_object.wave
    Calculated wave properties as a Python dictionary
        | Output is a Python dictionary
        | Name of output is 'oceanlyz_object.wave'
        | Values(s) in this dictionary can be called by using 'key'
        | Example:

            | oceanlyz_object.wave['Hm0']         : Contain zero-moment wave height
            | oceanlyz_object.wave['Tp']          : Contain peak wave period
            | oceanlyz_object.wave['Field_Names'] : Contain key (variable) names in the wave dictionary
            | oceanlyz_object.wave['Burst_Data']  : Contain data for each burst

Examples
--------

.. code:: python

    #Import libraries
    import oceanlyz
    import numpy as np
    import matplotlib.pyplot as plt
    import os

    #Create OCEANLYZ object
    #del ocn #Optional
    ocn=oceanlyz.oceanlyz()
    
    #Read data
    #Assume data file is named 'waterpressure_5burst.csv' and is stored in 'C:\oceanlyz_python\Sample_Data'
    os.chdir('C:\\oceanlyz_python\\Sample_Data') #Change current path to Sample_Data folder
    water_pressure=np.genfromtxt('waterpressure_5burst.csv') #Load data
    
    #Input parameters
    ocn.data=water_pressure.copy()
    ocn.InputType='pressure'
    ocn.OutputType='wave+waterlevel'
    ocn.AnalysisMethod='spectral'
    ocn.n_burst=5
    ocn.burst_duration=1024
    ocn.fs=10
    ocn.fmin=0.05                    #Only required if ocn.AnalysisMethod='spectral'
    ocn.fmax=ocn.fs/2                #Only required if ocn.AnalysisMethod='spectral'
    ocn.fmaxpcorrCalcMethod='auto'   #Only required if ocn.InputType='pressure' and ocn.AnalysisMethod='spectral'
    ocn.Kpafterfmaxpcorr='constant'  #Only required if ocn.InputType='pressure' and ocn.AnalysisMethod='spectral'
    ocn.fminpcorr=0.15               #Only required if ocn.InputType='pressure' and ocn.AnalysisMethod='spectral'
    ocn.fmaxpcorr=0.55               #Only required if ocn.InputType='pressure' and ocn.AnalysisMethod='spectral'
    ocn.heightfrombed=0.05           #Only required if ocn.InputType='pressure' and ocn.AnalysisMethod='spectral'
    ocn.dispout='yes'               
    ocn.Rho=1024                     #Seawater density (Varies)

    #Run OCEANLYZ
    ocn.runoceanlyz()

    #Plot peak wave period (Tp)
    plt.plot(ocn.wave['Tp'])

References
----------

Karimpour, A., & Chen, Q. (2017).
Wind wave analysis in depth limited water using OCEANLYZ, A MATLAB toolbox.
Computers & Geosciences, 106, 181-189.

Karimpour, A. (2020). ScientiMate, Earth-Science Data Analysis Library.

wxPython Demo Code and Gallery
https://extras.wxpython.org/wxPython4/extras/
https://docs.wxpython.org/gallery.html
https://wxpython.org/Phoenix/docs/html/gallery.html
https://docs.wxwidgets.org/trunk/page_screenshots.html
https://wxpython.org/pages/downloads/
https://wxpython.org/Phoenix/docs/html/grid_overview.html

wxPython instructions:
https://realpython.com/python-gui-with-wxpython/
https://zetcode.com/wxpython/
https://www.tutorialspoint.com/wxpython/index.htm
http://wxglade.sourceforge.net/docs/index.html
https://www.blog.pythonlibrary.org/2010/06/26/the-dialogs-of-wxpython-part-1-of-2/
https://www.blog.pythonlibrary.org/2010/07/10/the-dialogs-of-wxpython-part-2-of-2/

List of widget toolkits
https://en.wikipedia.org/wiki/List_of_widget_toolkits
https://en.wikipedia.org/wiki/Graphical_user_interface_builder
https://en.wikipedia.org/wiki/Rapid_application_development
https://wiki.python.org/moin/GuiProgramming
http://wxglade.sourceforge.net/
https://github.com/wxFormBuilder/wxFormBuilder

.. License & Disclaimer
.. --------------------
..
.. Copyright (c) 2023 Arash Karimpour
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
"""

#--------------------------------------------------------------------------
#CODE
#--------------------------------------------------------------------------
#Import required packages
import os
import sys
import datetime
import hashlib
import base64
import pickle
import copy
import webbrowser
import wx
import wx.grid
import wx.adv
import wx.lib.wordwrap
#import wx.lib.intctrl
import oceanlyz
import scientimate as sm 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg, NavigationToolbar2WxAgg

#--------------------------------------------------------------------------
#Create OCEANLYZ object
ocn = oceanlyz.oceanlyz()

#--------------------------------------------------------------------------
#Global variables
class Global_Variable():
    #properties
    def __init__(self):
        self.oceanlyz_gui_ver = '1.2'
        self.oceanlyz_ver = '2.0'
        self.data = []
        self.data_original = []
        self.data_modified = []
        self.wave = []
        self.wave_timeseries = []
        self.wave_spectrum = []
        self.wave_waterlevel = []
        self.wave_timeseries_header = []
        self.wave_spectrum_header = []
        self.wave_waterlevel_header = []
        self.oceanlyz_dir_abspath = []
        self.CommercialKeyValid = False

GlobalVar = Global_Variable()

#--------------------------------------------------------------------------
#Get application absolute path

#https://note.nkmk.me/en/python-script-file-path/
#https://stackoverflow.com/questions/404744/determining-application-path-in-a-python-exe-generated-by-pyinstaller
#https://stackoverflow.com/questions/2292703/how-can-i-get-the-executables-current-directory-in-py2exe
#Determine if application is a python script file or frozen exe file
if getattr(sys, 'frozen', False):
    GlobalVar.oceanlyz_dir_abspath = os.path.dirname(sys.executable) #Get path of executable PyInstaller
else:
    GlobalVar.oceanlyz_dir_abspath = os.path.dirname(os.path.abspath(__file__))


#GlobalVar.oceanlyz_dir_abspath = os.path.dirname(os.path.abspath(__file__))
#GlobalVar.oceanlyz_dir_abspath = pathlib.Path(__file__).reslove().parent

#--------------------------------------------------------------------------
#Save load configuration
class Save_Load_Config():
    #properties
    def __init__(self):
        self.InputType = []
        self.InputType_Selection = []
        self.OutputType = []
        self.OutputType_Selection = []
        self.AnalysisMethod = []
        self.AnalysisMethod_Selection = []
        self.n_burst = []
        self.burst_duration = []
        self.fs = []
        self.fmin = []
        self.fmax = []
        self.fmaxpcorrCalcMethod = []
        self.fmaxpcorrCalcMethod_Selection = []
        self.Kpafterfmaxpcorr = []
        self.Kpafterfmaxpcorr_Selection = []
        self.fminpcorr = []
        self.fmaxpcorr = []
        self.heightfrombed = []
        self.Rho = []
        self.nfft = []
        self.nfft_Selection = []
        self.SeparateSeaSwell = []
        self.SeparateSeaSwell_Selection = []
        self.fmaxswell = []
        self.fpminswell = []

#SaveLoadConfig = Save_Load_Config()

#--------------------------------------------------------------------------
#Validate license functions

#--------------------------------------------------------------------------
#Functions to classes

#Reset GlobalVar
def ResetGlobalVar():
    GlobalVar.oceanlyz_gui_ver = '1.2'
    GlobalVar.oceanlyz_ver = '2.0'
    GlobalVar.data = []
    GlobalVar.data_original = []
    GlobalVar.data_modified = []
    GlobalVar.wave = []
    GlobalVar.wave_timeseries = []
    GlobalVar.wave_spectrum = []
    GlobalVar.wave_waterlevel = []
    GlobalVar.wave_timeseries_header = []
    GlobalVar.wave_spectrum_header = []
    GlobalVar.wave_waterlevel_header = []
    GlobalVar.oceanlyz_dir_abspath = []

#Reset OCEANLYZ
def ResetOCEANLYZ():
    ocn.data=[]
    ocn.InputType='waterlevel'
    ocn.OutputType='wave'
    ocn.AnalysisMethod='spectral'
    ocn.n_burst=1
    ocn.burst_duration=1024
    ocn.fs=2
    ocn.fmin=0.05
    ocn.fmax=1e6
    ocn.fmaxpcorrCalcMethod='auto'
    ocn.Kpafterfmaxpcorr='constant'
    ocn.fminpcorr=0.15
    ocn.fmaxpcorr=0.55
    ocn.heightfrombed=0.0
    ocn.dispout='no'
    ocn.Rho=1000
    ocn.nfft=512
    ocn.SeparateSeaSwell='no'
    ocn.fmaxswell=0.25
    ocn.fpminswell=0.1
    ocn.tailcorrection='off'
    ocn.ftailcorrection=0.9
    ocn.tailpower=-5
    ocn.wave={}

#--------------------------------------------------------------------------
#Functions to reset and update GUI

#Reset (reload) Tab1 to its initial configuration
def ResetTab1():
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab1.Delimiter_combo_box_tab1.SetSelection(0)
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab1.FirstRowtoRead_combo_box_tab1.SetSelection(0)
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab1.FirstColumntoRead_combo_box_tab1.SetSelection(0)
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab1.FilePath_text_tab1.SetValue('')
    #grid_height = 1000
    #grid_width = 1
    #for row in range(grid_height): #Columns
    #    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab1.SpreadSheet_grid_tab1.SetCellValue(row,0,'')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab1.SpreadSheet_grid_tab1.ClearGrid()
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab1.axes_tab1.cla()
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab1.axes_tab1.set_ylabel('Data')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab1.PlotCanvas_tab1.draw() #Redraw plot

#Reset (reload) Tab2 to its initial configuration
def ResetTab2():
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab2.interpMethod.SetSelection(0)
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab2.ChangetoNaN_text_tab2.SetValue('0.0')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab2.what2replace.SetValue('0.0')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab2.WindowSize.SetSelection(1)
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab2.zscore_threshold.SetSelection(1)
    #grid_height = 1000
    #grid_width = 1
    #for row in range(grid_height): #Columns
    #    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab2.SpreadSheet_grid_tab2.SetCellValue(row,0,'')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab2.SpreadSheet_grid_tab2.ClearGrid()
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab2.axes_tab2.cla()
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab2.axes_tab2.set_ylabel('Data')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab2.PlotCanvas_tab2.draw() #Redraw plot

#Reset (reload) Tab3 to its initial configuration
def ResetTab3():
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.InputType.SetSelection(0)
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.OutputType.SetSelection(0)
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.AnalysisMethod.SetSelection(0)
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.n_burst.SetValue('')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.burst_duration.SetValue('')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.fs.SetValue('')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.fmin.SetValue('0.05')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.fmax.SetValue('1000000')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.fmaxpcorrCalcMethod.SetSelection(1)
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.Kpafterfmaxpcorr.SetSelection(1)
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.fminpcorr.SetValue('0.15')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.fmaxpcorr.SetValue('0.55')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.heightfrombed.SetValue('0.0')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.Rho.SetValue('1000')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.nfft.SetSelection(1)
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.SeparateSeaSwell.SetSelection(1)
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.fmaxswell.SetValue('0.25')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.fpminswell.SetValue('0.1')

#Reset (reload) Tab4 to its initial configuration
def ResetTab4():
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab4.TimeSeriesValue_combo_box_tab4.Set(['None'])
    #grid_height = 1000
    #grid_width = 1
    #for row in range(grid_height): #Columns
    #    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab4.SpreadSheet_grid_tab4.SetCellValue(row,0,'')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab4.SpreadSheet_grid_tab4.ClearGrid()
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab4.axes_tab4.cla()
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab4.axes_tab4.set_ylabel('Data')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab4.PlotCanvas_tab4.draw() #Redraw plot

#Reset (reload) Tab5 to its initial configuration
def ResetTab5():
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab5.BurstNumber_spin_ctrl_tab5.SetRange(1,100)
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab5.BurstNumber_spin_ctrl_tab5.SetValue('1')
    #grid_height = 1000
    #grid_width = 2
    #for row in range(grid_height): #Columns
    #    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab5.SpreadSheet_grid_tab5.SetCellValue(row,0,'')
    #    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab5.SpreadSheet_grid_tab5.SetCellValue(row,1,'')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab5.SpreadSheet_grid_tab5.ClearGrid()
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab5.axes_tab5.cla()
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab5.axes_tab5.set_xlabel('f (Hz)')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab5.axes_tab5.set_ylabel('Syy (m^2/Hz)')
    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab5.PlotCanvas_tab5.draw() #Redraw plot

#Update timeseries variables to be plotted
def SetTimeseriesVariablestoPlot(ocn, wave_timeseries_names, wave_spectrum_names, wave_waterlevel_names):
    if ocn.module==1 or ocn.module==2 or ocn.module==5 or ocn.module==6 or ocn.module==7 or ocn.module==8:
        #app.MainFrame.MainPanel.MainNotebook.Notebook_Tab4.TimeSeriesValue_combo_box_tab4.Clear()
        #for item in wave_timeseries_names:
        #    app.MainFrame.MainPanel.MainNotebook.Notebook_Tab4.TimeSeriesValue_combo_box_tab4.Append(item)
        
        app.MainFrame.MainPanel.MainNotebook.Notebook_Tab4.TimeSeriesValue_combo_box_tab4.Set(wave_timeseries_names)
        #app.MainFrame.MainPanel.MainNotebook.Notebook_Tab4.TimeSeriesValue_combo_box_tab4.SetSelection(0)
    else:
        app.MainFrame.MainPanel.MainNotebook.Notebook_Tab4.TimeSeriesValue_combo_box_tab4.Set(['None'])

#Update spectrum range to be plotted
def SetSpectrumRangetoPlot(ocn):
    if ocn.module==1 or ocn.module==5 or ocn.module==6 or ocn.module==8:
        app.MainFrame.MainPanel.MainNotebook.Notebook_Tab5.BurstNumber_spin_ctrl_tab5.SetMax(ocn.n_burst)
    else:
        app.MainFrame.MainPanel.MainNotebook.Notebook_Tab5.BurstNumber_spin_ctrl_tab5.SetMax(1)

#--------------------------------------------------------------------------
#wxpython
class MyNotebook_Tab1(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyNotebook_Tab1.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)

        Tab1_vbox = wx.BoxSizer(wx.VERTICAL)

        Tab1_vbox_hbox1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Load water level/depth/pressure timeseries from CSV/TXT/ASCII file"), wx.HORIZONTAL)
        Tab1_vbox.Add(Tab1_vbox_hbox1, 0, wx.ALL | wx.EXPAND, 5)

        Delimiter_label_tab1 = wx.StaticText(self, wx.ID_ANY, "Delimiter")
        Tab1_vbox_hbox1.Add(Delimiter_label_tab1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.Delimiter_combo_box_tab1 = wx.ComboBox(self, wx.ID_ANY, choices=["Comma", "Space", "Tab"], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.Delimiter_combo_box_tab1.SetSelection(0)
        Tab1_vbox_hbox1.Add(self.Delimiter_combo_box_tab1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        static_line_1_tab1 = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
        Tab1_vbox_hbox1.Add(static_line_1_tab1, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        FirstRowtoRead_label_tab1 = wx.StaticText(self, wx.ID_ANY, "First row to read")
        Tab1_vbox_hbox1.Add(FirstRowtoRead_label_tab1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.FirstRowtoRead_combo_box_tab1 = wx.ComboBox(self, wx.ID_ANY, choices=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.FirstRowtoRead_combo_box_tab1.SetSelection(0)
        Tab1_vbox_hbox1.Add(self.FirstRowtoRead_combo_box_tab1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        FirstColumntoRead_label_tab1 = wx.StaticText(self, wx.ID_ANY, "First column to read")
        Tab1_vbox_hbox1.Add(FirstColumntoRead_label_tab1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.FirstColumntoRead_combo_box_tab1 = wx.ComboBox(self, wx.ID_ANY, choices=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.FirstColumntoRead_combo_box_tab1.SetSelection(0)
        Tab1_vbox_hbox1.Add(self.FirstColumntoRead_combo_box_tab1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        static_line_2_tab1 = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
        Tab1_vbox_hbox1.Add(static_line_2_tab1, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        FilePath_label_tab1 = wx.StaticText(self, wx.ID_ANY, "File Path")
        Tab1_vbox_hbox1.Add(FilePath_label_tab1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.FilePath_text_tab1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY | wx.TE_RICH)
        Tab1_vbox_hbox1.Add(self.FilePath_text_tab1, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.LoadData_button_tab1 = wx.Button(self, wx.ID_ANY, "Load Data")
        self.LoadData_button_tab1.SetToolTip("Load water level/depth/pressure timeseries from CSV/TXT/ASCII file")
        Tab1_vbox_hbox1.Add(self.LoadData_button_tab1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Tab1_vbox_hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        Tab1_vbox.Add(Tab1_vbox_hbox2, 1, wx.ALL | wx.EXPAND, 5)

        #Set up spreadsheet
        grid_height = 1000
        grid_width = 1
        self.SpreadSheet_grid_tab1 = wx.grid.Grid(self, wx.ID_ANY, size=(1, 1))
        self.SpreadSheet_grid_tab1.CreateGrid(grid_height, grid_width)
        self.SpreadSheet_grid_tab1.EnableEditing(0)
        self.SpreadSheet_grid_tab1.SetColLabelValue(0, "Data")
        Tab1_vbox_hbox2.Add(self.SpreadSheet_grid_tab1, 1, wx.ALL | wx.EXPAND, 0)

        Tab1_vbox_hbox2_vbox1 = wx.BoxSizer(wx.VERTICAL)
        Tab1_vbox_hbox2.Add(Tab1_vbox_hbox2_vbox1, 4, wx.ALL | wx.EXPAND, 5)

        #Set up plot and its toolbar
        self.fig_tab1=mpl.figure.Figure(figsize=(6.4, 6.4/2), dpi=100)
        self.axes_tab1 = self.fig_tab1.add_subplot(111)
        #self.axes_tab1.set_xlabel('Time')
        self.axes_tab1.set_ylabel('Data')
        #self.axes_tab1.set_title('Input Data')
        self.PlotCanvas_tab1 = FigureCanvasWxAgg(self, -1, self.fig_tab1)
        self.PlotCanvas_tab1.Fit()
        PlotToolbar_tab1 = NavigationToolbar2WxAgg(self.PlotCanvas_tab1)
        PlotToolbar_tab1.Realize()
        PlotToolbar_tab1.update() #Update the axes menu on the toolbar

        Tab1_vbox_hbox2_vbox1.Add(PlotToolbar_tab1, 0, wx.ALL | wx.EXPAND, 5)
        Tab1_vbox_hbox2_vbox1.Add(self.PlotCanvas_tab1, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(Tab1_vbox)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.OnLoadData_tab1, self.LoadData_button_tab1)
        # end wxGlade

    def OnLoadData_tab1(self, event):  # wxGlade: MyNotebook_Tab1.<event_handler>
        #print("Event handler 'OnLoadData_tab1' not implemented!")
        #event.Skip()

        #Load data file
        wildcard = 'CSV and TXT files (*.csv;*.txt)|*.csv;*.txt|ASCII files (*.*)|*.*'
        with wx.FileDialog(self, "Load Data", wildcard=wildcard,
                        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     #User pressed Cancel

            #Get file information
            FilePath = fileDialog.GetPath()
            DirName = fileDialog.GetDirectory()
            FileName = fileDialog.GetFilename()
            FileRoot, FileExtension = os.path.splitext(FilePath)

            #Reset GlobalVar
            ResetGlobalVar()

            #Reset (reload) Tab1 to its initial configuration
            #ResetTab1()
            #self.Delimiter_combo_box_tab1.SetSelection(0)
            #self.FirstRowtoRead_combo_box_tab1.SetSelection(0)
            #self.FirstColumntoRead_combo_box_tab1.SetSelection(0)
            self.FilePath_text_tab1.SetValue('')
            self.SpreadSheet_grid_tab1.ClearGrid()
            self.axes_tab1.cla()
            self.axes_tab1.set_ylabel('Data')
            self.PlotCanvas_tab1.draw() #Redraw plot

            #Reset (reload) Tab2 to its initial configuration
            ResetTab2()

            #Reset (reload) Tab3 to its initial configuration
            ResetTab3()

            #Reset (reload) Tab4 to its initial configuration
            ResetTab4()

            #Reset (reload) Tab5 to its initial configuration
            ResetTab5()

            #Set delimiter
            if self.Delimiter_combo_box_tab1.GetValue()=="Comma":
                delimiter=','
            elif self.Delimiter_combo_box_tab1.GetValue()=="Space":
                delimiter=None
            elif self.Delimiter_combo_box_tab1.GetValue()=="Tab":
                delimiter=None
            else:
                delimiter=None
    
            #Set first row to read (number of headerlines to skip)
            num_headerlines_to_skip = int(self.FirstRowtoRead_combo_box_tab1.GetValue())-1

            try:

                #Load data
                GlobalVar.data = np.genfromtxt(FilePath, delimiter=delimiter, skip_header=num_headerlines_to_skip)

                #Display file path
                self.FilePath_text_tab1.SetValue(FilePath)

            except:
                #pass
                #wx.LogError("Cannot open file '%s'." % FilePath)

                #Message dialog
                MsgDialog=wx.MessageDialog(None, message='Data cannot be loaded', caption='Error', style=wx.OK | wx.CENTRE)
                MsgDialog.ShowModal()
                return

        #Set column to read
        if self.FirstColumntoRead_combo_box_tab1.GetValue()!='1':
            first_col_index = int(self.FirstColumntoRead_combo_box_tab1.GetValue())-1
            if GlobalVar.data.ndim>1 and first_col_index<GlobalVar.data.shape[1]:
                GlobalVar.data=GlobalVar.data[:,first_col_index:]

        #Reshape data to a single column
        if GlobalVar.data.ndim>1:
            #GlobalVar.data = np.reshape(GlobalVar.data, -1, order='F')
            data_1column = [] #Single column array
            for i in range(GlobalVar.data.shape[1]):
                data_1column = np.hstack((data_1column, GlobalVar.data[:,i]))
            
            GlobalVar.data = data_1column.copy()

        #Retain original data
        GlobalVar.data_original = GlobalVar.data.copy()
        GlobalVar.data_modified = GlobalVar.data.copy()

        #Display data in spreadsheet
        grid_height = 1000
        grid_width = 1
        for row in range(grid_height): #Columns
            if row<GlobalVar.data.size and row<(grid_height-1):
                self.SpreadSheet_grid_tab1.SetCellValue(row,0,str(GlobalVar.data[row]))
            else:
                self.SpreadSheet_grid_tab1.SetCellValue(row,0,'...')
    
        #Plot data
        self.axes_tab1.cla()
        self.axes_tab1.set_ylabel('Data')
        if GlobalVar.data.size<1000000:
            self.axes_tab1.plot(GlobalVar.data[:])
        else:
            self.axes_tab1.plot(GlobalVar.data[0:1000000]) #Plot only first 1000000 data points
        self.PlotCanvas_tab1.draw() #Redraw plot

        #Message dialog
        MsgDialog=wx.MessageDialog(None, message='{} data points imported'.format(str(GlobalVar.data.size)), caption='Information', style=wx.OK | wx.CENTRE)
        MsgDialog.ShowModal()

# end of class MyNotebook_Tab1

#--------------------------------------------------------------------------
class MyNotebook_Tab2(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyNotebook_Tab2.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)

        Tab2_vbox = wx.BoxSizer(wx.VERTICAL)

        Tab2_vbox_hbox1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Replace NaN values by interpolation of neighboring data points"), wx.HORIZONTAL)
        Tab2_vbox.Add(Tab2_vbox_hbox1, 0, wx.ALL | wx.EXPAND, 5)

        interpMethod_label = wx.StaticText(self, wx.ID_ANY, "Interpolation method")
        Tab2_vbox_hbox1.Add(interpMethod_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.interpMethod = wx.ComboBox(self, wx.ID_ANY, choices=["linear", "nearest"], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.interpMethod.SetSelection(0)
        Tab2_vbox_hbox1.Add(self.interpMethod, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        static_line_1_tab2 = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
        Tab2_vbox_hbox1.Add(static_line_1_tab2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        self.ChangetoNaN_text_tab2 = wx.TextCtrl(self, wx.ID_ANY, "0.0")
        Tab2_vbox_hbox1.Add(self.ChangetoNaN_text_tab2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.ChangetoNaN_button_tab2 = wx.Button(self, wx.ID_ANY, "Change to NaN")
        Tab2_vbox_hbox1.Add(self.ChangetoNaN_button_tab2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        static_line_2_tab2 = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
        Tab2_vbox_hbox1.Add(static_line_2_tab2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        self.CheckforNaN_button_tab2 = wx.Button(self, wx.ID_ANY, "Check for NaN")
        Tab2_vbox_hbox1.Add(self.CheckforNaN_button_tab2, 0, wx.ALL, 5)

        self.ReplaceNaN_button_tab2 = wx.Button(self, wx.ID_ANY, "Replace NaN")
        Tab2_vbox_hbox1.Add(self.ReplaceNaN_button_tab2, 0, wx.ALL, 5)

        Tab2_vbox_hbox2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Replace unacceptable values by interpolation of neighboring data points"), wx.HORIZONTAL)
        Tab2_vbox.Add(Tab2_vbox_hbox2, 0, wx.ALL | wx.EXPAND, 5)

        self.what2replace = wx.TextCtrl(self, wx.ID_ANY, "0.0")
        Tab2_vbox_hbox2.Add(self.what2replace, 0, wx.ALL, 5)

        self.ReplaceValue_button_tab2 = wx.Button(self, wx.ID_ANY, "Replace Value")
        Tab2_vbox_hbox2.Add(self.ReplaceValue_button_tab2, 0, wx.ALL, 5)

        static_line_3_tab2 = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
        Tab2_vbox_hbox2.Add(static_line_3_tab2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        WindowSize_label = wx.StaticText(self, wx.ID_ANY, "Window size")
        Tab2_vbox_hbox2.Add(WindowSize_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.WindowSize = wx.ComboBox(self, wx.ID_ANY, choices=["3", "5", "7", "9", "11", "13", "15"], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.WindowSize.SetSelection(1)
        Tab2_vbox_hbox2.Add(self.WindowSize, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        zscore_threshold_label = wx.StaticText(self, wx.ID_ANY, "Z-Score threshold")
        Tab2_vbox_hbox2.Add(zscore_threshold_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.zscore_threshold = wx.ComboBox(self, wx.ID_ANY, choices=["1.5", "2", "2.5", "3"], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.zscore_threshold.SetSelection(1)
        Tab2_vbox_hbox2.Add(self.zscore_threshold, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.ReplaceOutliers_button_tab2 = wx.Button(self, wx.ID_ANY, "Replace Outliers")
        Tab2_vbox_hbox2.Add(self.ReplaceOutliers_button_tab2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Tab2_vbox_hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        Tab2_vbox.Add(Tab2_vbox_hbox3, 1, wx.ALL | wx.EXPAND, 5)

        #Set up spreadsheet
        grid_height = 1000
        grid_width = 1
        self.SpreadSheet_grid_tab2 = wx.grid.Grid(self, wx.ID_ANY, size=(1, 1))
        self.SpreadSheet_grid_tab2.CreateGrid(grid_height, grid_width)
        self.SpreadSheet_grid_tab2.EnableEditing(0)
        self.SpreadSheet_grid_tab2.SetColLabelValue(0, "Data")
        Tab2_vbox_hbox3.Add(self.SpreadSheet_grid_tab2, 1, wx.ALL | wx.EXPAND, 0)

        Tab2_vbox_hbox2_vbox1 = wx.BoxSizer(wx.VERTICAL)
        Tab2_vbox_hbox3.Add(Tab2_vbox_hbox2_vbox1, 4, wx.ALL | wx.EXPAND, 5)

        #Set up plot and its toolbar
        self.fig_tab2=mpl.figure.Figure(figsize=(6.4, 6.4/3), dpi=100)
        self.axes_tab2 = self.fig_tab2.add_subplot(111)
        #self.axes_tab2.set_xlabel('Time')
        self.axes_tab2.set_ylabel('Data')
        #self.axes_tab2.set_title('Input Data')
        self.PlotCanvas_tab2 = FigureCanvasWxAgg(self, -1, self.fig_tab2)
        self.PlotCanvas_tab2.Fit()
        PlotToolbar_tab2 = NavigationToolbar2WxAgg(self.PlotCanvas_tab2)
        PlotToolbar_tab2.Realize()
        PlotToolbar_tab2.update() #Update the axes menu on the toolbar

        Tab2_vbox_hbox2_vbox1.Add(PlotToolbar_tab2, 0, wx.ALL | wx.EXPAND, 5)
        Tab2_vbox_hbox2_vbox1.Add(self.PlotCanvas_tab2, 1, wx.ALL | wx.EXPAND, 5)

        Tab2_vbox_hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        Tab2_vbox.Add(Tab2_vbox_hbox4, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.ResetChanges_button_tab2 = wx.Button(self, wx.ID_ANY, "Reset Changes")
        Tab2_vbox_hbox4.Add(self.ResetChanges_button_tab2, 0, wx.RIGHT, 5)

        self.ApplyChanges_button_tab2 = wx.Button(self, wx.ID_ANY, "Apply Changes")
        Tab2_vbox_hbox4.Add(self.ApplyChanges_button_tab2, 0, wx.ALL, 0)

        self.SetSizer(Tab2_vbox)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.OnChangetoNaN, self.ChangetoNaN_button_tab2)
        self.Bind(wx.EVT_BUTTON, self.OnCheckforNaN, self.CheckforNaN_button_tab2)
        self.Bind(wx.EVT_BUTTON, self.OnReplaceNaN, self.ReplaceNaN_button_tab2)
        self.Bind(wx.EVT_BUTTON, self.OnReplaceValue, self.ReplaceValue_button_tab2)
        self.Bind(wx.EVT_BUTTON, self.OnReplaceOutliers, self.ReplaceOutliers_button_tab2)
        self.Bind(wx.EVT_BUTTON, self.OnResetChanges, self.ResetChanges_button_tab2)
        self.Bind(wx.EVT_BUTTON, self.OnApplyChanges, self.ApplyChanges_button_tab2)
        # end wxGlade

    def OnChangetoNaN(self, event):  # wxGlade: MyNotebook_Tab2.<event_handler>
        #print("Event handler 'OnChangetoNaN' not implemented!")
        #event.Skip()

        #Change to NaN
        Value2NaN = float(self.ChangetoNaN_text_tab2.GetValue())
        num_of_NaN = 0
        if Value2NaN in GlobalVar.data_modified:
            num_of_NaN = GlobalVar.data_modified[GlobalVar.data_modified==Value2NaN].size
            GlobalVar.data_modified[GlobalVar.data_modified==Value2NaN] = np.nan

        #Message dialog
        MsgDialog=wx.MessageDialog(None, message='{} points changed to NaN'.format(str(num_of_NaN)), caption='Information', style=wx.OK | wx.CENTRE)
        MsgDialog.ShowModal()

    def OnCheckforNaN(self, event):  # wxGlade: MyNotebook_Tab2.<event_handler>
        #print("Event handler 'OnCheckforNaN' not implemented!")
        #event.Skip()

        #Number of NaN
        NaN_Indx = np.isnan(GlobalVar.data_modified)
        num_of_NaN = NaN_Indx[NaN_Indx==True].size
        print(GlobalVar.data[0:10])
        print(GlobalVar.data_original[0:10])
        print(GlobalVar.data_modified[0:10])
        print(NaN_Indx)
        print(num_of_NaN)

        #Message dialog
        MsgDialog=wx.MessageDialog(None, message='{} points are NaN'.format(str(num_of_NaN)), caption='Information', style=wx.OK | wx.CENTRE)
        MsgDialog.ShowModal()

    def OnReplaceNaN(self, event):  # wxGlade: MyNotebook_Tab2.<event_handler>
        #print("Event handler 'OnReplaceNaN' not implemented!")
        #event.Skip()

        #Replace NaN
        wait = wx.BusyInfo("Please wait ...")
        interpMethod=self.interpMethod.GetValue()
        GlobalVar.data_modified, NaN_Indx = sm.replacemissing1d(GlobalVar.data_modified, what2replace='NaN', interpMethod=interpMethod, dispout='no')
        del wait

        #Display data in spreadsheet
        grid_height = 1000
        grid_width = 1
        for row in range(grid_height): #Columns
            if row<GlobalVar.data_modified.size and row<(grid_height-1):
                self.SpreadSheet_grid_tab2.SetCellValue(row,0,str(GlobalVar.data_modified[row]))
            else:
                self.SpreadSheet_grid_tab2.SetCellValue(row,0,'...')
    
        #Plot data
        self.axes_tab2.cla()
        self.axes_tab2.set_ylabel('Data')
        if GlobalVar.data_modified.size<1000000:
            self.axes_tab2.plot(GlobalVar.data_modified[:])
        else:
            self.axes_tab2.plot(GlobalVar.data_modified[0:1000000]) #Plot only first 1000000 data points
        self.PlotCanvas_tab2.draw() #Redraw plot

        #Number of NaN
        num_of_NaN = NaN_Indx[NaN_Indx==True].size

        #Message dialog
        MsgDialog=wx.MessageDialog(None, message='{} NaN points replaced'.format(str(num_of_NaN)), caption='Information', style=wx.OK | wx.CENTRE)
        MsgDialog.ShowModal()

    def OnReplaceValue(self, event):  # wxGlade: MyNotebook_Tab2.<event_handler>
        #print("Event handler 'OnReplaceValue' not implemented!")
        #event.Skip()

        #Replace value
        wait = wx.BusyInfo("Please wait ...")
        what2replace=float(self.what2replace.GetValue())
        interpMethod=self.interpMethod.GetValue()
        GlobalVar.data_modified, NaN_Indx = sm.replacemissing1d(GlobalVar.data_modified, what2replace=what2replace, interpMethod=interpMethod, dispout='no')
        del wait

        #Display data in spreadsheet
        grid_height = 1000
        grid_width = 1
        for row in range(grid_height): #Columns
            if row<GlobalVar.data_modified.size and row<(grid_height-1):
                self.SpreadSheet_grid_tab2.SetCellValue(row,0,str(GlobalVar.data_modified[row]))
            else:
                self.SpreadSheet_grid_tab2.SetCellValue(row,0,'...')
    
        #Plot data
        self.axes_tab2.cla()
        self.axes_tab2.set_ylabel('Data')
        if GlobalVar.data_modified.size<1000000:
            self.axes_tab2.plot(GlobalVar.data_modified[:])
        else:
            self.axes_tab2.plot(GlobalVar.data_modified[0:1000000]) #Plot only first 1000000 data points
        self.PlotCanvas_tab2.draw() #Redraw plot

        #Number of NaN
        num_of_NaN = NaN_Indx[NaN_Indx==True].size

        #Message dialog
        MsgDialog=wx.MessageDialog(None, message='{} points replaced'.format(str(num_of_NaN)), caption='Information', style=wx.OK | wx.CENTRE)
        MsgDialog.ShowModal()

    def OnReplaceOutliers(self, event):  # wxGlade: MyNotebook_Tab2.<event_handler>
        #print("Event handler 'OnReplaceOutliers' not implemented!")
        #event.Skip()

        #Replace outliers
        wait = wx.BusyInfo("Please wait ...")
        WindowSize=int(self.WindowSize.GetValue())
        zscore_threshold=float(self.zscore_threshold.GetValue())
        interpMethod=self.interpMethod.GetValue()
        GlobalVar.data_modified, outlier_Indx = sm.replaceoutlier(GlobalVar.data_modified, WindowSize=WindowSize, zscore_threshold=zscore_threshold, interpMethod=interpMethod, dispout='no')
        del wait

        #Display data in spreadsheet
        grid_height = 1000
        grid_width = 1
        for row in range(grid_height): #Columns
            if row<GlobalVar.data_modified.size and row<(grid_height-1):
                self.SpreadSheet_grid_tab2.SetCellValue(row,0,str(GlobalVar.data_modified[row]))
            else:
                self.SpreadSheet_grid_tab2.SetCellValue(row,0,'...')
    
        #Plot data
        self.axes_tab2.cla()
        self.axes_tab2.set_ylabel('Data')
        if GlobalVar.data_modified.size<1000000:
            self.axes_tab2.plot(GlobalVar.data_modified[:])
        else:
            self.axes_tab2.plot(GlobalVar.data_modified[0:1000000]) #Plot only first 1000000 data points
        self.PlotCanvas_tab2.draw() #Redraw plot

        #Number of NaN
        num_of_NaN = outlier_Indx[outlier_Indx==True].size

        #Message dialog
        MsgDialog=wx.MessageDialog(None, message='{} points replaced'.format(str(num_of_NaN)), caption='Information', style=wx.OK | wx.CENTRE)
        MsgDialog.ShowModal()

    def OnResetChanges(self, event):  # wxGlade: MyNotebook_Tab2.<event_handler>
        #print("Event handler 'OnResetChanges' not implemented!")
        #event.Skip()

        #Reset changes
        GlobalVar.data = GlobalVar.data_original.copy()
        GlobalVar.data_modified = GlobalVar.data_original.copy()

        #Display data in spreadsheet
        self.SpreadSheet_grid_tab2.ClearGrid()

        #Plot data
        self.axes_tab2.cla()
        self.axes_tab2.set_ylabel('Data')
        self.PlotCanvas_tab2.draw() #Redraw plot

        #Message dialog
        MsgDialog=wx.MessageDialog(None, message='All changes reset', caption='Information', style=wx.OK | wx.CENTRE)
        MsgDialog.ShowModal()

    def OnApplyChanges(self, event):  # wxGlade: MyNotebook_Tab2.<event_handler>
        #print("Event handler 'OnApplyChanges' not implemented!")
        #event.Skip()

        #Apply changes
        GlobalVar.data = GlobalVar.data_modified.copy()

        #Message dialog
        MsgDialog=wx.MessageDialog(None, message='Changes applied', caption='Information', style=wx.OK | wx.CENTRE)
        MsgDialog.ShowModal()

# end of class MyNotebook_Tab2

#--------------------------------------------------------------------------
class MyNotebook_Tab3(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyNotebook_Tab3.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)

        Tab3_vbox = wx.BoxSizer(wx.VERTICAL)

        Tab3_vbox_hbox1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Required properties"), wx.HORIZONTAL)
        Tab3_vbox.Add(Tab3_vbox_hbox1, 0, wx.ALL | wx.EXPAND, 5)

        self.InputType = wx.RadioBox(self, wx.ID_ANY, "Input data type", choices=["waterlevel", "pressure"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.InputType.SetSelection(0)
        Tab3_vbox_hbox1.Add(self.InputType, 1, wx.ALL | wx.EXPAND, 5)

        self.OutputType = wx.RadioBox(self, wx.ID_ANY, "Output data type", choices=["wave", "waterlevel", "wave+waterlevel"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.OutputType.SetSelection(0)
        Tab3_vbox_hbox1.Add(self.OutputType, 1, wx.ALL | wx.EXPAND, 5)

        self.AnalysisMethod = wx.RadioBox(self, wx.ID_ANY, "Analysis method", choices=["spectral", "zerocross"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.AnalysisMethod.SetSelection(0)
        Tab3_vbox_hbox1.Add(self.AnalysisMethod, 1, wx.ALL | wx.EXPAND, 5)

        Tab3_vbox_hbox1_gbox1 = wx.GridBagSizer(5, 5)
        Tab3_vbox_hbox1.Add(Tab3_vbox_hbox1_gbox1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        n_burst_label = wx.StaticText(self, wx.ID_ANY, "Number of burst")
        Tab3_vbox_hbox1_gbox1.Add(n_burst_label, (0, 0), (1, 1), wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)

        self.n_burst = wx.TextCtrl(self, wx.ID_ANY, "")
        Tab3_vbox_hbox1_gbox1.Add(self.n_burst, (0, 1), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        burst_duration_label = wx.StaticText(self, wx.ID_ANY, "Duration of each burst (s)")
        Tab3_vbox_hbox1_gbox1.Add(burst_duration_label, (1, 0), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        self.burst_duration = wx.TextCtrl(self, wx.ID_ANY, "")
        Tab3_vbox_hbox1_gbox1.Add(self.burst_duration, (1, 1), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        fs_label = wx.StaticText(self, wx.ID_ANY, "Sampling frequency (Hz)")
        Tab3_vbox_hbox1_gbox1.Add(fs_label, (2, 0), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        self.fs = wx.TextCtrl(self, wx.ID_ANY, "")
        Tab3_vbox_hbox1_gbox1.Add(self.fs, (2, 1), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        Tab3_vbox_hbox2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Required properties for spectral analysis (required only if analysis method is spectral)"), wx.HORIZONTAL)
        Tab3_vbox.Add(Tab3_vbox_hbox2, 0, wx.ALL | wx.EXPAND, 5)

        fmin_label = wx.StaticText(self, wx.ID_ANY, "Minimum frequency cut-off (Hz)")
        Tab3_vbox_hbox2.Add(fmin_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.fmin = wx.TextCtrl(self, wx.ID_ANY, "0.05")
        Tab3_vbox_hbox2.Add(self.fmin, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        static_line_1_tab3 = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
        Tab3_vbox_hbox2.Add(static_line_1_tab3, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        fmax_label = wx.StaticText(self, wx.ID_ANY, "Maximum frequency cut-off (fmax<=fs/2), (Hz)")
        Tab3_vbox_hbox2.Add(fmax_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.fmax = wx.TextCtrl(self, wx.ID_ANY, "1000000")
        Tab3_vbox_hbox2.Add(self.fmax, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Tab3_vbox_hbox3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Required properties for pressure data analysis (required only if input data type is pressure)"), wx.HORIZONTAL)
        Tab3_vbox.Add(Tab3_vbox_hbox3, 0, wx.ALL | wx.EXPAND, 5)

        self.fmaxpcorrCalcMethod = wx.RadioBox(self, wx.ID_ANY, "fmaxpcorr calculation method", choices=["user", "auto"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.fmaxpcorrCalcMethod.SetSelection(1)
        Tab3_vbox_hbox3.Add(self.fmaxpcorrCalcMethod, 1, wx.ALL | wx.EXPAND, 5)

        self.Kpafterfmaxpcorr = wx.RadioBox(self, wx.ID_ANY, "Pressure response factor for (frequency > fmaxpcorr)", choices=["one", "constant"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.Kpafterfmaxpcorr.SetSelection(1)
        Tab3_vbox_hbox3.Add(self.Kpafterfmaxpcorr, 1, wx.ALL | wx.EXPAND, 5)

        Tab3_vbox_hbox3_gbox1 = wx.GridBagSizer(5, 5)
        Tab3_vbox_hbox3.Add(Tab3_vbox_hbox3_gbox1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        fminpcorr_label = wx.StaticText(self, wx.ID_ANY, "Minimum frequency for fmaxpcorr (Hz)")
        Tab3_vbox_hbox3_gbox1.Add(fminpcorr_label, (0, 0), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        self.fminpcorr = wx.TextCtrl(self, wx.ID_ANY, "0.15")
        Tab3_vbox_hbox3_gbox1.Add(self.fminpcorr, (0, 1), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        fmaxpcorr_label = wx.StaticText(self, wx.ID_ANY, "Maximum frequency for fmaxpcorr (Hz)")
        Tab3_vbox_hbox3_gbox1.Add(fmaxpcorr_label, (1, 0), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        self.fmaxpcorr = wx.TextCtrl(self, wx.ID_ANY, "0.55")
        Tab3_vbox_hbox3_gbox1.Add(self.fmaxpcorr, (1, 1), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        heightfrombed_label = wx.StaticText(self, wx.ID_ANY, "Pressure sensor height from bed (m)")
        Tab3_vbox_hbox3_gbox1.Add(heightfrombed_label, (2, 0), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        self.heightfrombed = wx.TextCtrl(self, wx.ID_ANY, "0.0")
        Tab3_vbox_hbox3_gbox1.Add(self.heightfrombed, (2, 1), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        Tab3_vbox_hbox4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Optional properties"), wx.HORIZONTAL)
        Tab3_vbox.Add(Tab3_vbox_hbox4, 0, wx.ALL | wx.EXPAND, 5)

        Tab3_vbox_hbox4_gbox1 = wx.GridBagSizer(5, 5)
        Tab3_vbox_hbox4.Add(Tab3_vbox_hbox4_gbox1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Rho_label = wx.StaticText(self, wx.ID_ANY, "Water density (kg/m^3)")
        Tab3_vbox_hbox4_gbox1.Add(Rho_label, (0, 0), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        self.Rho = wx.TextCtrl(self, wx.ID_ANY, "1000")
        Tab3_vbox_hbox4_gbox1.Add(self.Rho, (0, 1), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        nfft_label = wx.StaticText(self, wx.ID_ANY, "NFFT")
        Tab3_vbox_hbox4_gbox1.Add(nfft_label, (1, 0), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        self.nfft = wx.ComboBox(self, wx.ID_ANY, choices=["256", "512", "1024", "2048", "4096"], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.nfft.SetSelection(1)
        Tab3_vbox_hbox4_gbox1.Add(self.nfft, (1, 1), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        static_line_2_tab3 = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
        Tab3_vbox_hbox4.Add(static_line_2_tab3, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        self.SeparateSeaSwell = wx.RadioBox(self, wx.ID_ANY, "Separate wind sea and swell waves", choices=["yes", "no"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.SeparateSeaSwell.SetSelection(1)
        Tab3_vbox_hbox4.Add(self.SeparateSeaSwell, 1, wx.ALL | wx.EXPAND, 5)

        Tab3_vbox_hbox4_gbox2 = wx.GridBagSizer(5, 5)
        Tab3_vbox_hbox4.Add(Tab3_vbox_hbox4_gbox2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        fmaxswell_label = wx.StaticText(self, wx.ID_ANY, "Maximum swell frequency (Hz)")
        Tab3_vbox_hbox4_gbox2.Add(fmaxswell_label, (0, 0), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        self.fmaxswell = wx.TextCtrl(self, wx.ID_ANY, "0.25")
        Tab3_vbox_hbox4_gbox2.Add(self.fmaxswell, (0, 1), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        fpminswell_label = wx.StaticText(self, wx.ID_ANY, "Minimum swell frequency (Hz)")
        Tab3_vbox_hbox4_gbox2.Add(fpminswell_label, (1, 0), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        self.fpminswell = wx.TextCtrl(self, wx.ID_ANY, "0.1")
        Tab3_vbox_hbox4_gbox2.Add(self.fpminswell, (1, 1), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        Tab3_vbox_hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        Tab3_vbox.Add(Tab3_vbox_hbox5, 1, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.StartAnalysis_button_tab3 = wx.Button(self, wx.ID_ANY, "Start Analysis")
        Tab3_vbox_hbox5.Add(self.StartAnalysis_button_tab3, 0, wx.ALL, 0)

        Tab3_vbox_hbox4_gbox2.AddGrowableCol(1)

        Tab3_vbox_hbox4_gbox1.AddGrowableCol(1)

        Tab3_vbox_hbox3_gbox1.AddGrowableCol(1)

        Tab3_vbox_hbox1_gbox1.AddGrowableCol(0)
        Tab3_vbox_hbox1_gbox1.AddGrowableCol(1)

        self.SetSizer(Tab3_vbox)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.OnStartAnalysis, self.StartAnalysis_button_tab3)
        # end wxGlade

    def OnStartAnalysis(self, event):  # wxGlade: MyNotebook_Tab3.<event_handler>
        #print("Event handler 'OnStartAnalysis' not implemented!")
        #event.Skip()

        #Check if n_burst, burst_duration, and fs are entered
        if (not self.n_burst.GetValue()) or (not self.burst_duration.GetValue()) or (not self.fs.GetValue()):
            #Message dialog
            MsgDialog=wx.MessageDialog(None, message='Number of burst, duration of each burst , or sampling frequency not entered', caption='Error', style=wx.OK | wx.CENTRE)
            MsgDialog.ShowModal()
            return

        #Check if n_burst, burst_duration, and fs are numbers
        try:
            #Use int(float(num)) to take care of both int entered as float such as '2.0'
            int(float(self.n_burst.GetValue()))
            int(float(self.burst_duration.GetValue()))
            int(float(self.fs.GetValue()))
        except:
            #Message dialog
            MsgDialog=wx.MessageDialog(None, message='Number of burst, duration of each burst , and sampling frequency should be integer', caption='Error', style=wx.OK | wx.CENTRE)
            MsgDialog.ShowModal()
            return

        #Check if (n_burst*burst_duration*fs) is equal to total number of data points
        n_total_datapoints = int(float(self.n_burst.GetValue()))*int(float(self.burst_duration.GetValue()))*int(float(self.fs.GetValue()))
        if GlobalVar.data.size!=n_total_datapoints:
            #Message dialog
            MsgDialog=wx.MessageDialog(None, message='(number of burst * duration of each burst * sampling frequency) should be equal to number of data points', caption='Error', style=wx.OK | wx.CENTRE)
            MsgDialog.ShowModal()
            return

        #Check if fmax<=fs/2
        if float(self.fmax.GetValue())>0.5*int(float(self.fs.GetValue())):
            fs_half = 0.5*int(float(self.fs.GetValue()))
            app.MainFrame.MainPanel.MainNotebook.Notebook_Tab3.fmax.SetValue(str(fs_half))

        #Run OCEANLYZ
        try:

            #Set up OCEANLYZ Input parameters
            ocn.data = GlobalVar.data
            ocn.InputType = self.InputType.GetStringSelection()
            ocn.OutputType = self.OutputType.GetStringSelection()
            ocn.AnalysisMethod = self.AnalysisMethod.GetStringSelection()
            ocn.n_burst = int(float(self.n_burst.GetValue()))
            ocn.burst_duration = int(float(self.burst_duration.GetValue()))
            ocn.fs = int(float(self.fs.GetValue()))
            ocn.fmin = float(self.fmin.GetValue())
            ocn.fmax = float(self.fmax.GetValue())
            ocn.fmaxpcorrCalcMethod = self.fmaxpcorrCalcMethod.GetStringSelection()
            ocn.Kpafterfmaxpcorr = self.Kpafterfmaxpcorr.GetStringSelection()
            ocn.fminpcorr = float(self.fminpcorr.GetValue())
            ocn.fmaxpcorr = float(self.fmaxpcorr.GetValue())
            ocn.heightfrombed = float(self.heightfrombed.GetValue())
            ocn.dispout='no'
            ocn.Rho = float(self.Rho.GetValue())
            ocn.nfft = int(float(self.nfft.GetValue()))
            ocn.SeparateSeaSwell = self.SeparateSeaSwell.GetStringSelection()
            ocn.fmaxswell = float(self.fmaxswell.GetValue())
            ocn.fpminswell = float(self.fpminswell.GetValue())

            #Print inputs
            #print(ocn.InputType)
            #print(ocn.OutputType)
            #print(ocn.AnalysisMethod)
            #print(ocn.n_burst)
            #print(ocn.burst_duration)
            #print(ocn.fs)
            #print(ocn.fmin)
            #print(ocn.fmax)
            #print(ocn.fmaxpcorrCalcMethod)
            #print(ocn.Kpafterfmaxpcorr)
            #print(ocn.fminpcorr)
            #print(ocn.fmaxpcorr)
            #print(ocn.heightfrombed)
            #print(ocn.Rho)
            #print(ocn.nfft)
            #print(ocn.SeparateSeaSwell)
            #print(ocn.fmaxswell)
            #print(ocn.fpminswell)

            #Progress dialog
            #style = wx.PD_APP_MODAL | wx.PD_CAN_ABORT | wx.PD_CAN_SKIP | wx.PD_ELAPSED_TIME | wx.PD_ESTIMATED_TIME | wx.PD_REMAINING_TIME | wx.PD_AUTO_HIDE
            #style = wx.PD_APP_MODAL | wx.PD_AUTO_HIDE
            ProgDialog = wx.ProgressDialog("Information", "Analysis started. Please wait, this might take a while ...", maximum = 100, parent=self, style = wx.PD_APP_MODAL)
            
            #Update progress dialog
            wx.MilliSleep(300)
            ProgDialog.Update(35,'')
            #ProgDialog.Pulse(newmsg='')
            #wx.GetApp().Yield()        

            #Run OCEANLYZ
            #wait = wx.BusyInfo("Analysis started. Please wait, this might take a while ...")
            ocn.runoceanlyz()
            GlobalVar.wave = ocn.wave.copy()
            ocn_keys = list(ocn.__dict__.keys())

            #Update progress dialog
            wx.MilliSleep(300)
            ProgDialog.Update(100,'Analysis finished')
            ProgDialog.Destroy()

            #del wait
            #Message dialog
            #MsgDialog=wx.MessageDialog(None, message='Analysis finished', caption='Information', style=wx.OK | wx.CENTRE)
            #MsgDialog.ShowModal()

        except Exception as e:
            
            #import traceback
            #traceback.print_exc()
            #print(e)
            
            #Message dialog
            MsgDialog=wx.MessageDialog(None, message='There is an error in input data or parameters', caption='Error', style=wx.OK | wx.CENTRE)
            MsgDialog.ShowModal()

            #Update progress dialog
            wx.MilliSleep(300)
            ProgDialog.Update(100,'Analysis interrupted')
            ProgDialog.Destroy()
            return

        #Assign variable names for each module
        #module=1 -> Data: Waterlevel, Method: Spectral Analysis, Calculate: Wave Parameters
        if ocn.module==1:
            wave_timeseries_names = ['Hm0', 'Tp', 'fp']
            wave_spectrum_names = ['f', 'Syy']
            wave_waterlevel_names = ['None']
    
        #module=2 -> Data: Waterlevel, Method: Zero-Crossing, Calculate: Wave Parameters
        elif ocn.module==2:
            wave_timeseries_names = ['Hs', 'Hz', 'Tz', 'Ts']
            wave_spectrum_names = ['None']
            wave_waterlevel_names = ['None']
        
        #module=3 -> Data: Pressure, Method: Spectral Analysis, Calculate: Waterlevel
        elif ocn.module==3:
            wave_timeseries_names = ['None']
            wave_spectrum_names = ['None']
            wave_waterlevel_names = ['Eta']
    
        #module=4 -> Data: Pressure, Method: Zero-Crossing, Calculate: Waterlevel
        elif ocn.module==4:
            wave_timeseries_names = ['None']
            wave_spectrum_names = ['None']
            wave_waterlevel_names = ['Eta']
        
        #module=5 -> Data: Waterlevel, Method: Spectral Analysis, Calculate: Wave Parameters (sea and Swell)
        elif ocn.module==5:
            wave_timeseries_names = ['Hm0', 'Hm0sea', 'Hm0swell', 'Tp', 'Tpsea', 'Tpswell', 'fp', 'fseparation']
            wave_spectrum_names = ['f', 'Syy']
            wave_waterlevel_names = ['None']
    
        #module=6 -> Data: Pressure, Method: Spectral Analysis, Calculate: Wave Parameters, Waterlevel
        elif ocn.module==6:
            wave_timeseries_names = ['Hm0', 'Tp', 'fp']
            wave_spectrum_names = ['f', 'Syy']
            wave_waterlevel_names = ['Eta']
    
        #module=7 -> Data: Pressure, Method: Zero-Crossing, Calculate: Wave Parameters, Waterlevel
        elif ocn.module==7:
            wave_timeseries_names = ['Hs', 'Hz', 'Tz', 'Ts']
            wave_spectrum_names = ['None']
            wave_waterlevel_names = ['Eta']
    
        #module=8 -> Data: Pressure, Method: Spectral Analysis, Calculate: Wave Parameters (sea and Swell), Waterlevel
        elif ocn.module==8:
            wave_timeseries_names = ['Hm0', 'Hm0sea', 'Hm0swell', 'Tp', 'Tpsea', 'Tpswell', 'fp', 'fseparation']
            wave_spectrum_names = ['f', 'Syy']
            wave_waterlevel_names = ['Eta']

        #Generate array contains timeseries
        if ocn.module==1 or ocn.module==2 or ocn.module==5 or ocn.module==6 or ocn.module==7 or ocn.module==8:
            GlobalVar.wave_timeseries_header = ['Burst Number'] 
            for item in wave_timeseries_names:
                GlobalVar.wave_timeseries_header.append(item)
            
            #GlobalVar.wave_timeseries = [] #Reset values
            GlobalVar.wave_timeseries = np.arange(1,ocn.n_burst+1,1)
            for item in wave_timeseries_names:
                GlobalVar.wave_timeseries = np.vstack((GlobalVar.wave_timeseries, GlobalVar.wave[item]))
            
            #GlobalVar.wave_timeseries_header = wave_timeseries_names.copy()
            #GlobalVar.wave_timeseries = np.zeros((ocn.n_burst,len(wave_timeseries_names)))
            #for i in range(0,len(wave_timeseries_names),1):
            #    GlobalVar.wave_timeseries[:,i] = GlobalVar.wave[wave_timeseries_names[i]]

            #Transpose array to columnwise
            GlobalVar.wave_timeseries = GlobalVar.wave_timeseries.T

        #Generate array contains spectrum
        if ocn.module==1 or ocn.module==5 or ocn.module==6 or ocn.module==8:
            GlobalVar.wave_spectrum_header = ['f (Hz)'] 
            for i in range(0,ocn.n_burst,1):
                GlobalVar.wave_spectrum_header.append('Syy (m^2/Hz) - burst_'+str(i+1))

            GlobalVar.wave_spectrum = [] #Reset values
            GlobalVar.wave_spectrum = np.concatenate((GlobalVar.wave_spectrum, GlobalVar.wave['f'][0,:]), axis=None)
            GlobalVar.wave_spectrum = np.vstack((GlobalVar.wave_spectrum, GlobalVar.wave['Syy']))

            #Transpose array to columnwise
            GlobalVar.wave_spectrum = GlobalVar.wave_spectrum.T

        #Generate array contains waterlevel
        if ocn.module==3 or ocn.module==4 or ocn.module==6 or ocn.module==7 or ocn.module==8:
            GlobalVar.wave_waterlevel_header = [] #Reset values
            for i in range(0,ocn.n_burst,1):
                GlobalVar.wave_waterlevel_header.append('Waterlevel (m) - burst_'+str(i+1))

            #GlobalVar.wave_waterlevel = [] #Reset values
            GlobalVar.wave_waterlevel = GlobalVar.wave['Eta'].copy()

            #Transpose array to columnwise
            GlobalVar.wave_waterlevel = GlobalVar.wave_waterlevel.T

        #Reset (reload) Tab4 to its initial configuration
        ResetTab4()

        #Reset (reload) Tab5 to its initial configuration
        ResetTab5()

        #Update timeseries variables to be plotted
        SetTimeseriesVariablestoPlot(ocn, wave_timeseries_names, wave_spectrum_names, wave_waterlevel_names)

        #Update spectrum range to be plotted
        SetSpectrumRangetoPlot(ocn)

# end of class MyNotebook_Tab3

#--------------------------------------------------------------------------
class MyNotebook_Tab4(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyNotebook_Tab4.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)

        Tab4_vbox = wx.BoxSizer(wx.VERTICAL)

        Tab4_vbox_hbox1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Select timeseries value to plot"), wx.HORIZONTAL)
        Tab4_vbox.Add(Tab4_vbox_hbox1, 0, wx.ALL | wx.EXPAND, 5)

        TimeSeriesValue_label_tab4 = wx.StaticText(self, wx.ID_ANY, "TimeSeries value")
        Tab4_vbox_hbox1.Add(TimeSeriesValue_label_tab4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.TimeSeriesValue_combo_box_tab4 = wx.ComboBox(self, wx.ID_ANY, choices=["None", "None", "None"], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        Tab4_vbox_hbox1.Add(self.TimeSeriesValue_combo_box_tab4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.PlotTimeSeries_button_tab4 = wx.Button(self, wx.ID_ANY, "Plot TimeSeries")
        Tab4_vbox_hbox1.Add(self.PlotTimeSeries_button_tab4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Tab4_vbox_hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        Tab4_vbox.Add(Tab4_vbox_hbox2, 1, wx.ALL | wx.EXPAND, 5)

        #Set up spreadsheet
        grid_height = 1000
        grid_width = 1
        self.SpreadSheet_grid_tab4 = wx.grid.Grid(self, wx.ID_ANY, size=(1, 1))
        self.SpreadSheet_grid_tab4.CreateGrid(grid_height, grid_width)
        self.SpreadSheet_grid_tab4.EnableEditing(0)
        self.SpreadSheet_grid_tab4.SetColLabelValue(0, "Results")
        Tab4_vbox_hbox2.Add(self.SpreadSheet_grid_tab4, 1, wx.ALL | wx.EXPAND, 0)

        Tab4_vbox_hbox2_vbox1 = wx.BoxSizer(wx.VERTICAL)
        Tab4_vbox_hbox2.Add(Tab4_vbox_hbox2_vbox1, 4, wx.ALL | wx.EXPAND, 5)

        #Set up plot and its toolbar
        self.fig_tab4=mpl.figure.Figure(figsize=(6.4, 6.4/2), dpi=100)
        self.axes_tab4 = self.fig_tab4.add_subplot(111)
        #self.axes_tab4.set_xlabel('Time')
        self.axes_tab4.set_ylabel('Data')
        #self.axes_tab4.set_title('Input Data')
        self.PlotCanvas_tab4 = FigureCanvasWxAgg(self, -1, self.fig_tab4)
        self.PlotCanvas_tab4.Fit()
        PlotToolbar_tab4 = NavigationToolbar2WxAgg(self.PlotCanvas_tab4)
        PlotToolbar_tab4.Realize()
        PlotToolbar_tab4.update() #Update the axes menu on the toolbar

        Tab4_vbox_hbox2_vbox1.Add(PlotToolbar_tab4, 0, wx.ALL | wx.EXPAND, 5)
        Tab4_vbox_hbox2_vbox1.Add(self.PlotCanvas_tab4, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(Tab4_vbox)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.OnPlotTimeSeries, self.PlotTimeSeries_button_tab4)
        # end wxGlade

    def OnPlotTimeSeries(self, event):  # wxGlade: MyNotebook_Tab4.<event_handler>
        #print("Event handler 'OnPlotTimeSeries' not implemented!")
        #event.Skip()

        #Check if there is timeseries results
        if ocn.module==1 or ocn.module==2 or ocn.module==5 or ocn.module==6 or ocn.module==7 or ocn.module==8:

            #Get variable name to plot
            var_name = self.TimeSeriesValue_combo_box_tab4.GetValue()

            #Display data in spreadsheet
            self.SpreadSheet_grid_tab4.SetColLabelValue(0, var_name)
            grid_height = 1000
            grid_width = 1
            for row in range(grid_height): #Columns
                if row<GlobalVar.wave[var_name].size and row<(grid_height-1):
                    self.SpreadSheet_grid_tab4.SetCellValue(row,0,str(GlobalVar.wave[var_name][row]))
                else:
                    self.SpreadSheet_grid_tab4.SetCellValue(row,0,'...')

            #Plot data
            self.axes_tab4.cla()
            self.axes_tab4.set_ylabel(var_name)
            self.axes_tab4.plot(GlobalVar.wave[var_name][:])
            self.PlotCanvas_tab4.draw() #Redraw plot

        else:
            #Message dialog
            MsgDialog=wx.MessageDialog(None, message='There is no TimeSeries results', caption='Information', style=wx.OK | wx.CENTRE)
            MsgDialog.ShowModal()
            return

# end of class MyNotebook_Tab4

#--------------------------------------------------------------------------
class MyNotebook_Tab5(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyNotebook_Tab5.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)

        Tab5_vbox = wx.BoxSizer(wx.VERTICAL)

        Tab5_vbox_hbox1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Enter spectrum burst number to plot"), wx.HORIZONTAL)
        Tab5_vbox.Add(Tab5_vbox_hbox1, 0, wx.ALL | wx.EXPAND, 5)

        BurstNumber_label_tab5 = wx.StaticText(self, wx.ID_ANY, "Burst number")
        Tab5_vbox_hbox1.Add(BurstNumber_label_tab5, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.BurstNumber_spin_ctrl_tab5 = wx.SpinCtrl(self, wx.ID_ANY, "1", min=1, max=100)
        Tab5_vbox_hbox1.Add(self.BurstNumber_spin_ctrl_tab5, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.PlotSpectrum_button_tab5 = wx.Button(self, wx.ID_ANY, "Plot Spectrum")
        Tab5_vbox_hbox1.Add(self.PlotSpectrum_button_tab5, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Tab5_vbox_hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        Tab5_vbox.Add(Tab5_vbox_hbox2, 1, wx.ALL | wx.EXPAND, 5)

        #Set up spreadsheet
        grid_height = 1000
        grid_width = 2
        self.SpreadSheet_grid_tab5 = wx.grid.Grid(self, wx.ID_ANY, size=(1, 1))
        self.SpreadSheet_grid_tab5.CreateGrid(grid_height, grid_width)
        self.SpreadSheet_grid_tab5.EnableEditing(0)
        self.SpreadSheet_grid_tab5.SetColLabelValue(0, "f (Hz)")
        self.SpreadSheet_grid_tab5.SetColLabelValue(1, "Syy (m^2/Hz)")
        Tab5_vbox_hbox2.Add(self.SpreadSheet_grid_tab5, 1, wx.ALL | wx.EXPAND, 0)

        Tab5_vbox_hbox2_vbox1 = wx.BoxSizer(wx.VERTICAL)
        Tab5_vbox_hbox2.Add(Tab5_vbox_hbox2_vbox1, 2, wx.ALL | wx.EXPAND, 5)

        #Set up plot and its toolbar
        self.fig_tab5=mpl.figure.Figure(figsize=(6.4, 6.4/2), dpi=100)
        self.axes_tab5 = self.fig_tab5.add_subplot(111)
        self.axes_tab5.set_xlabel('f (Hz)')
        self.axes_tab5.set_ylabel('Syy (m^2/Hz)')
        #self.axes_tab5.set_title('Input Data')
        self.PlotCanvas_tab5 = FigureCanvasWxAgg(self, -1, self.fig_tab5)
        self.PlotCanvas_tab5.Fit()
        PlotToolbar_tab5 = NavigationToolbar2WxAgg(self.PlotCanvas_tab5)
        PlotToolbar_tab5.Realize()
        PlotToolbar_tab5.update() #Update the axes menu on the toolbar

        #PlotToolbar_tab5 = wx.StaticText(self, wx.ID_ANY, "Plot Toolbar Place Holder", style=wx.ALIGN_CENTER_HORIZONTAL)
        #PlotCanvas_tab5 = wx.StaticText(self, wx.ID_ANY, "Plot Canvas Place Holder", style=wx.ALIGN_CENTER_HORIZONTAL)
        Tab5_vbox_hbox2_vbox1.Add(PlotToolbar_tab5, 0, wx.ALL | wx.EXPAND, 5)
        Tab5_vbox_hbox2_vbox1.Add(self.PlotCanvas_tab5, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(Tab5_vbox)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.OnPlotSpectrum, self.PlotSpectrum_button_tab5)
        # end wxGlade

    def OnPlotSpectrum(self, event):  # wxGlade: MyNotebook_Tab5.<event_handler>
        #print("Event handler 'OnPlotSpectrum' not implemented!")
        #event.Skip()

        #Check if there is spectrume results
        if ocn.module==1 or ocn.module==5 or ocn.module==6 or ocn.module==8:

            #Display data in spreadsheet
            burst_num = int(self.BurstNumber_spin_ctrl_tab5.GetValue())-1
            grid_height = 1000
            grid_width = 2
            for row in range(grid_height): #Columns
                if row<(GlobalVar.wave['f'].T).shape[0] and row<(grid_height-1):
                    self.SpreadSheet_grid_tab5.SetCellValue(row,0,str((GlobalVar.wave['f'].T)[row,burst_num]))
                    self.SpreadSheet_grid_tab5.SetCellValue(row,1,str((GlobalVar.wave['Syy'].T)[row,burst_num]))
                else:
                    self.SpreadSheet_grid_tab5.SetCellValue(row,0,'...')
                    self.SpreadSheet_grid_tab5.SetCellValue(row,1,'...')

            #Plot data
            self.axes_tab5.cla()
            self.axes_tab5.set_xlabel('f (Hz)')
            self.axes_tab5.set_ylabel('Syy (m^2/Hz)')
            self.axes_tab5.plot((GlobalVar.wave['f'].T)[:,burst_num],(GlobalVar.wave['Syy'].T)[:,burst_num])
            self.PlotCanvas_tab5.draw() #Redraw plot

        else:
            #Message dialog
            MsgDialog=wx.MessageDialog(None, message='There is no spectrum results', caption='Information', style=wx.OK | wx.CENTRE)
            MsgDialog.ShowModal()
            return

# end of class MyNotebook_Tab5

#--------------------------------------------------------------------------
class MyNotebook(wx.Notebook):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyNotebook.__init__
        kwds["style"] = kwds.get("style", 0) | wx.NB_TOP
        wx.Notebook.__init__(self, *args, **kwds)

        self.Notebook_Tab1 = MyNotebook_Tab1(self, wx.ID_ANY)
        self.AddPage(self.Notebook_Tab1, "Load Data")

        self.Notebook_Tab2 = MyNotebook_Tab2(self, wx.ID_ANY)
        self.AddPage(self.Notebook_Tab2, "Preprocess Data")

        self.Notebook_Tab3 = MyNotebook_Tab3(self, wx.ID_ANY)
        self.AddPage(self.Notebook_Tab3, "Analyze Data")

        self.Notebook_Tab4 = MyNotebook_Tab4(self, wx.ID_ANY)
        self.AddPage(self.Notebook_Tab4, "TimeSeries Results")

        self.Notebook_Tab5 = MyNotebook_Tab5(self, wx.ID_ANY)
        self.AddPage(self.Notebook_Tab5, "Spectrum Results")
        # end wxGlade

# end of class MyNotebook

#--------------------------------------------------------------------------
class MyPanel(wx.Panel):
#class MyPanel(wx.ScrolledWindow):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyPanel.__init__
        kwds["style"] = kwds.get("style", 0)
        wx.Panel.__init__(self, *args, **kwds)
        #wx.ScrolledWindow.__init__(self, *args, **kwds)
        #self.SetScrollRate(10, 10)

        MainPanel_vbox = wx.BoxSizer(wx.VERTICAL)

        self.MainNotebook = MyNotebook(self, wx.ID_ANY)
        MainPanel_vbox.Add(self.MainNotebook, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(MainPanel_vbox)

        self.Layout()
        # end wxGlade

# end of class MyPanel

#--------------------------------------------------------------------------
class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1024, 640))
        self.SetTitle("Oceanlyz GUI 1.2")

        # Menu Bar
        self.MainFrame_MenuBar = wx.MenuBar()
        self.fileMenu = wx.Menu()
        self.fileMenu.Append(wx.ID_OPEN, "Open Results", "Open results from Python pickle file")
        self.Bind(wx.EVT_MENU, self.OnOpenResults_Menu, id=wx.ID_OPEN)
        self.fileMenu.Append(wx.ID_SAVE, "Save Results", "Save results to Python pickle file")
        self.Bind(wx.EVT_MENU, self.OnSaveResults_Menu, id=wx.ID_SAVE)
        self.fileMenu.AppendSeparator()
        item = self.fileMenu.Append(wx.ID_ANY, "Export TimeSeries", "Export timeseries results to CSV file")
        self.Bind(wx.EVT_MENU, self.OnExportTimeSeries_Menu, item)
        item = self.fileMenu.Append(wx.ID_ANY, "Export Spectrum", "Export spectrum results to CSV file")
        self.Bind(wx.EVT_MENU, self.OnExportSpectrum_Menu, item)
        item = self.fileMenu.Append(wx.ID_ANY, "Export Waterlevel", "Export waterlevel results to CSV file")
        self.Bind(wx.EVT_MENU, self.OnExportWaterlevel_Menu, item)
        self.fileMenu.AppendSeparator()
        self.fileMenu.Append(wx.ID_EXIT, "&Exit", "Exit program")
        self.Bind(wx.EVT_MENU, self.OnExit_Menu, id=wx.ID_EXIT)
        self.MainFrame_MenuBar.Append(self.fileMenu, "&File")
        self.helpMenu = wx.Menu()
        item = self.helpMenu.Append(wx.ID_ANY, u"Help…", "Show help")
        self.Bind(wx.EVT_MENU, self.OnShowHelp_Menu, item)
        self.helpMenu.AppendSeparator()
        item = self.helpMenu.Append(wx.ID_ANY, "Purchase OCEANLYZ GUI", "Purchase OCEANLYZ GUI for commercial use")
        self.Bind(wx.EVT_MENU, self.OnPurchaseOCEANLYZGUI_Menu, item)
        item.Enable(False)
        item = self.helpMenu.Append(wx.ID_ANY, u"Register…", "Register product key")
        self.Bind(wx.EVT_MENU, self.OnRegister_Menu, item)
        item.Enable(False)
        self.helpMenu.Append(wx.ID_ABOUT, u"&About…", "Show about dialog")
        self.Bind(wx.EVT_MENU, self.OnShowAbout_Menu, id=wx.ID_ABOUT)
        self.MainFrame_MenuBar.Append(self.helpMenu, "&Help")
        self.SetMenuBar(self.MainFrame_MenuBar)
        # Menu Bar end

        # Tool Bar
        self.MainFrame_ToolBar = wx.ToolBar(self, -1, style=wx.TB_DEFAULT_STYLE | wx.TB_FLAT | wx.TB_HORZ_TEXT)
        tool = self.MainFrame_ToolBar.AddTool(wx.ID_ANY, "Open Results", wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, (24, 24)), wx.NullBitmap, wx.ITEM_NORMAL, "Open results from Python pickle file", "")
        self.Bind(wx.EVT_TOOL, self.OnOpenResults_Menu, id=tool.GetId())
        tool = self.MainFrame_ToolBar.AddTool(wx.ID_ANY, "Save Results", wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, (24, 24)), wx.NullBitmap, wx.ITEM_NORMAL, "Save results to Python pickle file", "")
        self.Bind(wx.EVT_TOOL, self.OnSaveResults_Menu, id=tool.GetId())
        self.MainFrame_ToolBar.AddSeparator()
        tool = self.MainFrame_ToolBar.AddTool(wx.ID_ANY, "Export TimeSeries", wx.ArtProvider.GetBitmap(wx.ART_REPORT_VIEW, wx.ART_TOOLBAR, (24, 24)), wx.NullBitmap, wx.ITEM_NORMAL, "Export timeseries results to CSV file", "")
        self.Bind(wx.EVT_TOOL, self.OnExportTimeSeries_Menu, id=tool.GetId())
        tool = self.MainFrame_ToolBar.AddTool(wx.ID_ANY, "Export Spectrum", wx.ArtProvider.GetBitmap(wx.ART_LIST_VIEW, wx.ART_TOOLBAR, (24, 24)), wx.NullBitmap, wx.ITEM_NORMAL, "Export spectrum results to CSV file", "")
        self.Bind(wx.EVT_TOOL, self.OnExportSpectrum_Menu, id=tool.GetId())
        tool = self.MainFrame_ToolBar.AddTool(wx.ID_ANY, "Export Waterlevel", wx.ArtProvider.GetBitmap(wx.ART_EXECUTABLE_FILE, wx.ART_TOOLBAR, (24, 24)), wx.NullBitmap, wx.ITEM_NORMAL, "Export waterlevel results to CSV file", "")
        self.Bind(wx.EVT_TOOL, self.OnExportWaterlevel_Menu, id=tool.GetId())
        self.SetToolBar(self.MainFrame_ToolBar)
        self.MainFrame_ToolBar.SetBackgroundColour((247, 250, 254, 255))
        self.MainFrame_ToolBar.Realize()
        # Tool Bar end

        self.MainPanel = MyPanel(self, wx.ID_ANY)
        self.Layout()
        self.Centre()

        self.Bind(wx.EVT_CLOSE, self.OnExit_Menu, self)

        #Validate license
        #wait = wx.BusyInfo("Oceanlyz GUI: Validating license, please wait ...")
        #ValidateLicense(self)
        #wx.MilliSleep(1000)
        #del wait

        #Check for non-commercial license
        #if GlobalVar.CommercialKeyValid==False:
        #    self.SetTitle("Oceanlyz GUI 1.2 (Non-Commercial Version)")
        #    self.MainPanel.MainNotebook.Notebook_Tab2.ResetChanges_button_tab2.Disable()
        #    self.MainPanel.MainNotebook.Notebook_Tab2.ApplyChanges_button_tab2.Disable()

        # end wxGlade

    def OnOpenResults_Menu(self, event):  # wxGlade: MyFrame.<event_handler>
        #print("Event handler 'OnOpenResults_Menu' not implemented!")
        #event.Skip()

        #Message dialog
        MsgDialog=wx.MessageDialog(None, message='Current contents will be lost, Proceed?', caption='Please confirm', style=wx.ICON_QUESTION | wx.YES_NO | wx.CENTRE)
        if MsgDialog.ShowModal() == wx.ID_NO:
            return

        #Open file
        with wx.FileDialog(self, "Open results from Python pickle file", wildcard='Pickle files (*.pkl)|*.pkl',
                        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     #User pressed Cancel

            #Get file information
            FilePath = fileDialog.GetPath()
            DirName = fileDialog.GetDirectory()
            FileName = fileDialog.GetFilename()
            FileRoot, FileExtension = os.path.splitext(FilePath)

            #Load results from file
            try:
                with open(FilePath, 'rb') as file:
                    ocn_imported = pickle.load(file)

            except:
                #pass
                #wx.LogError("Cannot open file '%s'." % FilePath)

                #Message dialog
                MsgDialog=wx.MessageDialog(None, message='Data cannot be loaded', caption='Error', style=wx.OK | wx.CENTRE)
                MsgDialog.ShowModal()
                return

        #Reset GlobalVar
        ResetGlobalVar()

        #Reset OCEANLYZ
        ResetOCEANLYZ()

        #Set data
        ocn = copy.deepcopy(ocn_imported)
        GlobalVar.data = ocn.data.copy()
        GlobalVar.data_original = ocn.data.copy()
        GlobalVar.data_modified = ocn.data.copy()
        GlobalVar.wave = ocn.wave.copy()

        #Assign variable names for each module
        #module=1 -> Data: Waterlevel, Method: Spectral Analysis, Calculate: Wave Parameters
        if ocn.module==1:
            wave_timeseries_names = ['Hm0', 'Tp', 'fp']
            wave_spectrum_names = ['f', 'Syy']
            wave_waterlevel_names = ['None']
    
        #module=2 -> Data: Waterlevel, Method: Zero-Crossing, Calculate: Wave Parameters
        elif ocn.module==2:
            wave_timeseries_names = ['Hs', 'Hz', 'Tz', 'Ts']
            wave_spectrum_names = ['None']
            wave_waterlevel_names = ['None']
        
        #module=3 -> Data: Pressure, Method: Spectral Analysis, Calculate: Waterlevel
        elif ocn.module==3:
            wave_timeseries_names = ['None']
            wave_spectrum_names = ['None']
            wave_waterlevel_names = ['Eta']
    
        #module=4 -> Data: Pressure, Method: Zero-Crossing, Calculate: Waterlevel
        elif ocn.module==4:
            wave_timeseries_names = ['None']
            wave_spectrum_names = ['None']
            wave_waterlevel_names = ['Eta']
        
        #module=5 -> Data: Waterlevel, Method: Spectral Analysis, Calculate: Wave Parameters (sea and Swell)
        elif ocn.module==5:
            wave_timeseries_names = ['Hm0', 'Hm0sea', 'Hm0swell', 'Tp', 'Tpsea', 'Tpswell', 'fp', 'fseparation']
            wave_spectrum_names = ['f', 'Syy']
            wave_waterlevel_names = ['None']
    
        #module=6 -> Data: Pressure, Method: Spectral Analysis, Calculate: Wave Parameters, Waterlevel
        elif ocn.module==6:
            wave_timeseries_names = ['Hm0', 'Tp', 'fp']
            wave_spectrum_names = ['f', 'Syy']
            wave_waterlevel_names = ['Eta']
    
        #module=7 -> Data: Pressure, Method: Zero-Crossing, Calculate: Wave Parameters, Waterlevel
        elif ocn.module==7:
            wave_timeseries_names = ['Hs', 'Hz', 'Tz', 'Ts']
            wave_spectrum_names = ['None']
            wave_waterlevel_names = ['Eta']
    
        #module=8 -> Data: Pressure, Method: Spectral Analysis, Calculate: Wave Parameters (sea and Swell), Waterlevel
        elif ocn.module==8:
            wave_timeseries_names = ['Hm0', 'Hm0sea', 'Hm0swell', 'Tp', 'Tpsea', 'Tpswell', 'fp', 'fseparation']
            wave_spectrum_names = ['f', 'Syy']
            wave_waterlevel_names = ['Eta']

        #Reset (reload) Tab1 to its initial configuration
        ResetTab1()

        #Reset (reload) Tab2 to its initial configuration
        ResetTab2()

        #Reset (reload) Tab3 to its initial configuration
        ResetTab3()

        #Reset (reload) Tab4 to its initial configuration
        ResetTab4()

        #Reset (reload) Tab5 to its initial configuration
        ResetTab5()

        #Update timeseries variables to be plotted
        SetTimeseriesVariablestoPlot(ocn, wave_timeseries_names, wave_spectrum_names, wave_waterlevel_names)

        #Update spectrum range to be plotted
        SetSpectrumRangetoPlot(ocn)

        #Set focus on Tab4
        app.MainFrame.MainPanel.MainNotebook.SetSelection(3)

        #Message dialog
        MsgDialog=wx.MessageDialog(None, message='Data imported, all analysis properties reset', caption='Information', style=wx.OK | wx.CENTRE)
        MsgDialog.ShowModal()

    def OnSaveResults_Menu(self, event):  # wxGlade: MyFrame.<event_handler>
        #print("Event handler 'OnSaveResults_Menu' not implemented!")
        #event.Skip()

        with wx.FileDialog(self, "Save results to Python pickle file", wildcard='Pickle files (*.pkl)|*.pkl',
                        style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     #User pressed Cancel

            #Get file information
            FilePath = fileDialog.GetPath()
            DirName = fileDialog.GetDirectory()
            FileName = fileDialog.GetFilename()
            FileRoot, FileExtension = os.path.splitext(FilePath)

            #Save results to file
            try:
                with open(FilePath, 'wb') as file:
                    pickle.dump(ocn, file)

                with open(FileRoot+'_config'+'.txt', 'w') as file:
                    file.write('#--------------------------------------\n')
                    file.write('#\n')
                    file.write('# OCEANLYZ GUI Ver {}\n'.format(GlobalVar.oceanlyz_gui_ver))
                    file.write('# OCEANLYZ Ver {}\n'.format(GlobalVar.oceanlyz_ver))
                    file.write('# Saved on {}\n'.format(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                    file.write('#\n')
                    file.write('#--------------------------------------\n')
                    file.write('Configurations\n')
                    file.write('#--------------------------------------\n')
                    file.write('Input data type (InputType) = {}\n'.format(ocn.InputType))
                    #file.write('InputType_Selection = {}\n'.format(ocn.))
                    file.write('Input data type (OutputType) = {}\n'.format(ocn.OutputType))
                    #file.write('OutputType_Selection = {}\n'.format(ocn.))
                    file.write('Analysis method (AnalysisMethod) = {}\n'.format(ocn.AnalysisMethod))
                    #file.write('AnalysisMethod_Selection = {}\n'.format(ocn.))
                    file.write('Number of burst (n_burst) = {}\n'.format(ocn.n_burst))
                    file.write('Duration of each burst (burst_duration) in second = {}\n'.format(ocn.burst_duration))
                    file.write('Sampling frequency (fs) in Hz = {}\n'.format(ocn.fs))
                    file.write('Minimu frequency cut-off (fmin) in Hz = {}\n'.format(ocn.fmin))
                    file.write('Maximum frequency cut-off (fmax) in Hz = {}\n'.format(ocn.fmax))
                    file.write('fmaxpcorr calculation method (fmaxpcorrCalcMethod) = {}\n'.format(ocn.fmaxpcorrCalcMethod))
                    #file.write('fmaxpcorrCalcMethod_Selection = {}\n'.format(ocn.))
                    file.write('Pressure response factor for frequency>fmaxpcorr (Kpafterfmaxpcorr) = {}\n'.format(ocn.Kpafterfmaxpcorr))
                    #file.write('Kpafterfmaxpcorr_Selection = {}\n'.format(ocn.))
                    file.write('Minimu frequency for fmaxpcorr (fminpcorr) in Hz = {}\n'.format(ocn.fminpcorr))
                    file.write('Maximum frequency for fmaxpcorr (fmaxpcorr) in Hz = {}\n'.format(ocn.fmaxpcorr))
                    file.write('Pressure sensor height from bed (heightfrombed) in meter = {}\n'.format(ocn.heightfrombed))
                    file.write('Water density (Rho) in kg/m^3 = {}\n'.format(ocn.Rho))
                    file.write('NFFT (nfft) = {}\n'.format(ocn.nfft))
                    #file.write('nfft_Selection = {}\n'.format(ocn.))
                    file.write('Separate wind sea and swell waves (SeparateSeaSwell) = {}\n'.format(ocn.SeparateSeaSwell))
                    #file.write('SeparateSeaSwell_Selection = {}\n'.format(ocn.))
                    file.write('Maximum swell frequency (fmaxswell) in Hz = {}\n'.format(ocn.fmaxswell))
                    file.write('Minimum swell frequency (fpminswell) in Hz = {}\n'.format(ocn.fpminswell))
                    file.write('#--------------------------------------')

            except:
                #pass
                #wx.LogError("Cannot save current data in file '%s'." % FilePath)

                #Message dialog
                MsgDialog=wx.MessageDialog(None, message='Data cannot be saved', caption='Error', style=wx.OK | wx.CENTRE)
                MsgDialog.ShowModal()
                return

    def OnExportTimeSeries_Menu(self, event):  # wxGlade: MyFrame.<event_handler>
        #print("Event handler 'OnExportTimeSeries_Menu' not implemented!")
        #event.Skip()

        #Check if there is timeseries results
        if ocn.module==1 or ocn.module==2 or ocn.module==5 or ocn.module==6 or ocn.module==7 or ocn.module==8:

            with wx.FileDialog(self, "Export timeseries results to CSV file", wildcard='CSV files (*.csv)|*.csv',
                            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

                if fileDialog.ShowModal() == wx.ID_CANCEL:
                    return     #User pressed Cancel

                #Get file information
                FilePath = fileDialog.GetPath()
                DirName = fileDialog.GetDirectory()
                FileName = fileDialog.GetFilename()
                FileRoot, FileExtension = os.path.splitext(FilePath)

                #Save timeseries results to file
                try:
                    header=','.join(GlobalVar.wave_timeseries_header)
                    np.savetxt(FilePath, GlobalVar.wave_timeseries, delimiter=',', header=header, comments='')

                except:
                    #pass
                    #wx.LogError("Cannot save current data in file '%s'." % FilePath)

                    #Message dialog
                    MsgDialog=wx.MessageDialog(None, message='Data cannot be saved', caption='Error', style=wx.OK | wx.CENTRE)
                    MsgDialog.ShowModal()
                    return

        else:
            #Message dialog
            MsgDialog=wx.MessageDialog(None, message='There is no TimeSeries results', caption='Information', style=wx.OK | wx.CENTRE)
            MsgDialog.ShowModal()
            return

    def OnExportSpectrum_Menu(self, event):  # wxGlade: MyFrame.<event_handler>
        #print("Event handler 'OnExportSpectrum_Menu' not implemented!")
        #event.Skip()

        #Check if there is spectrume results
        if ocn.module==1 or ocn.module==5 or ocn.module==6 or ocn.module==8:

            with wx.FileDialog(self, "Export spectrum results to CSV file", wildcard='CSV files (*.csv)|*.csv',
                            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

                if fileDialog.ShowModal() == wx.ID_CANCEL:
                    return     #User pressed Cancel

                #Get file information
                FilePath = fileDialog.GetPath()
                DirName = fileDialog.GetDirectory()
                FileName = fileDialog.GetFilename()
                FileRoot, FileExtension = os.path.splitext(FilePath)

                #Save spectrum results to file
                try:
                    header=','.join(GlobalVar.wave_spectrum_header)
                    np.savetxt(FilePath, GlobalVar.wave_spectrum, delimiter=',', header=header, comments='')

                except:
                    #pass
                    #wx.LogError("Cannot save current data in file '%s'." % FilePath)

                    #Message dialog
                    MsgDialog=wx.MessageDialog(None, message='Data cannot be saved', caption='Error', style=wx.OK | wx.CENTRE)
                    MsgDialog.ShowModal()
                    return

        else:
            #Message dialog
            MsgDialog=wx.MessageDialog(None, message='There is no spectrum results', caption='Information', style=wx.OK | wx.CENTRE)
            MsgDialog.ShowModal()
            return

    def OnExportWaterlevel_Menu(self, event):  # wxGlade: MyFrame.<event_handler>
        #print("Event handler 'OnExportWaterlevel_Menu' not implemented!")
        #event.Skip()

        #Check if there is watrelevel results
        if ocn.module==3 or ocn.module==4 or ocn.module==6 or ocn.module==7 or ocn.module==8:

            with wx.FileDialog(self, "Export waterlevel results to CSV file", wildcard='CSV files (*.csv)|*.csv',
                            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

                if fileDialog.ShowModal() == wx.ID_CANCEL:
                    return     #User pressed Cancel

                #Get file information
                FilePath = fileDialog.GetPath()
                DirName = fileDialog.GetDirectory()
                FileName = fileDialog.GetFilename()
                FileRoot, FileExtension = os.path.splitext(FilePath)

                #Save waterlevel results to file
                try:
                    header=','.join(GlobalVar.wave_waterlevel_header)
                    np.savetxt(FilePath, GlobalVar.wave_waterlevel, delimiter=',', header=header, comments='')

                except:
                    #pass
                    #wx.LogError("Cannot save current data in file '%s'." % FilePath)

                    #Message dialog
                    MsgDialog=wx.MessageDialog(None, message='Data cannot be saved', caption='Error', style=wx.OK | wx.CENTRE)
                    MsgDialog.ShowModal()
                    return

        else:
            #Message dialog
            MsgDialog=wx.MessageDialog(None, message='There is no waterlevel results', caption='Information', style=wx.OK | wx.CENTRE)
            MsgDialog.ShowModal()
            return

    def OnExit_Menu(self, event):  # wxGlade: MyFrame.<event_handler>
        #print("Event handler 'OnExit_Menu' not implemented!")
        #event.Skip()

        #Message dialog
        MsgDialog=wx.MessageDialog(None, message='Are you sure to quit?', caption='Please confirm', style=wx.YES_NO | wx.NO_DEFAULT | wx.CENTRE)
        if MsgDialog.ShowModal() == wx.ID_YES:
            #for item in wx.GetTopLevelWindows():
            #    print(item)
            #self.Close()
            self.Destroy()

    def OnShowHelp_Menu(self, event):  # wxGlade: MyFrame.<event_handler>
        #print("Event handler 'OnShowHelp_Menu' not implemented!")
        #event.Skip()

        #Open OCEANLYZ GUI help page
        webbrowser.open('https://oceanlyz.readthedocs.io')
        #help_dir_abspath = os.path.join(GlobalVar.oceanlyz_dir_abspath, r'help')
        #help_file_abspath = os.path.join(GlobalVar.oceanlyz_dir_abspath, r'help\index.html')
        #webbrowser.open(help_file_abspath)

    def OnPurchaseOCEANLYZGUI_Menu(self, event):  # wxGlade: MyFrame.<event_handler>
        #print("Event handler 'OnPurchaseOCEANLYZGUI_Menu' not implemented!")
        #event.Skip()

        pass

    def OnRegister_Menu(self, event):  # wxGlade: MyFrame.<event_handler>
        #print("Event handler 'OnRegister_Menu' not implemented!")
        #event.Skip()

        pass

    def OnShowAbout_Menu(self, event):  # wxGlade: MyFrame.<event_handler>
        #print("Event handler 'OnShowAbout_Menu' not implemented!")
        #event.Skip()

        descriptionText = 'OCEANLYZ GUI 1.2\n' + \
            'Ocean Wave Analyzing Toolbox, GUI version\n' + \
            'Build Date: August 2023\n' + \
            'Copyright (c) 2023 Arash Karimpour\n' + \
            'All Rights Reserved\n' + \
            'http://www.arashkarimpour.com\n' + \
            '\n' + \
            'Technical Support\n' + \
            'https://oceanlyz.readthedocs.io\n' + \
            'https://github.com/akarimp/Oceanlyz/issues\n' + \
            '\n' + \
            'Some of the following libraries and applications are used by this application: \n' + \
            'OCEANLYZ, ScientiMate, ' + \
            'Python, NumPy, SciPy, pandas, Matplotlib, ' + \
            'Spyder, GNU Octave, ' + \
            'wxPython, wxGlade, Sphinx, ' + \
            'PyInstaller, Inno Setup.'
    
        licenseText = 'For complete license agreement, read the END USER LICENSE AGREEMENT for this application.' + \
            '\n\n' + \
            'LICENSOR, AND AUTHOR OF THE SOFTWARE, HEREBY EXPRESSLY DISCLAIM ANY WARRANTY FOR THE SOFTWARE. ' + \
            'THE SOFTWARE AND ANY RELATED DOCUMENTATION IS PROVIDED “AS IS” WITHOUT WARRANTY OF ANY KIND, ' + \
            'EITHER EXPRESS OR IMPLIED, INCLUDING, WITHOUT LIMITATION, THE IMPLIED WARRANTIES OF MERCHANTABILITY, ' + \
            'FITNESS FOR A PARTICULAR PURPOSE, OR NON-INFRINGEMENT. ' + \
            'LICENSEE ACCEPTS ANY AND ALL RISK ARISING OUT OF USE OR PERFORMANCE OF THE SOFTWARE.' + \
            '\n\n' + \
            'LICENSOR AND ANY THIRD PARTY THAT HAS BEEN INVOLVED IN THE CREATION, PRODUCTION, OR DELIVERY OF THE SOFTWARE ' + \
            'SHALL NOT BE LIABLE TO LICENSEE, OR ANY OTHER PERSON OR ENTITY CLAIMING THROUGH LICENSEE ANY LOSS OF PROFITS, ' + \
            'INCOME, SAVINGS, OR ANY OTHER CONSEQUENTIAL, INCIDENTAL, SPECIAL, PUNITIVE, DIRECT OR INDIRECT DAMAGE, ' + \
            'WHETHER ARISING IN CONTRACT, TORT, WARRANTY, OR OTHERWISE. ' + \
            'THESE LIMITATIONS SHALL APPLY REGARDLESS OF THE ESSENTIAL PURPOSE OF ANY LIMITED REMEDY. ' + \
            'UNDER NO CIRCUMSTANCES SHALL LICENSOR’S AGGREGATE LIABILITY TO LICENSEE, ' + \
            'OR ANY OTHER PERSON OR ENTITY CLAIMING THROUGH LICENSEE, ' + \
            'EXCEED THE FINANCIAL AMOUNT ACTUALLY PAID BY LICENSEE TO LICENSOR FOR THE SOFTWARE.'

        info = wx.adv.AboutDialogInfo()

        #info.SetIcon(wx.Icon('oceanlyz.png', wx.BITMAP_TYPE_PNG))
        info.SetName('OCEANLYZ GUI')
        info.SetVersion('1.2')
        info.SetDescription(wx.lib.wordwrap.wordwrap(descriptionText, 400, wx.ClientDC(self) ,margin=5))
        info.SetCopyright('Copyright (C) 2012 - '+str(datetime.datetime.now().year)+' Arash Karimpour')
        info.SetWebSite('http://www.arashkarimpour.com')
        info.SetLicence(wx.lib.wordwrap.wordwrap(licenseText, 400, wx.ClientDC(self), margin=5))
        #info.AddDeveloper('Arash Karimpour')
        #info.AddDocWriter('Arash Karimpour')
        #info.AddArtist('Arash Karimpour')
        #info.AddTranslator('Arash Karimpour')

        wx.adv.AboutBox(info)
        #wx.adv.GenericAboutBox(info)

# end of class MyFrame

#--------------------------------------------------------------------------
class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("Registration")

        RegisterDialog_vbox = wx.BoxSizer(wx.VERTICAL)

        NoLicenseFound_label = wx.StaticText(self, wx.ID_ANY, "Enter license information or load license information from file.")
        RegisterDialog_vbox.Add(NoLicenseFound_label, 0, wx.ALL, 5)

        RegisterDialog_vbox_hbox1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Enter license information"), wx.HORIZONTAL)
        RegisterDialog_vbox.Add(RegisterDialog_vbox_hbox1, 1, wx.ALL | wx.EXPAND, 5)

        RegisterDialog_vbox_hbox1_gbox = wx.GridBagSizer(5, 5)
        RegisterDialog_vbox_hbox1.Add(RegisterDialog_vbox_hbox1_gbox, 1, wx.ALL | wx.EXPAND, 5)

        UserNameEntered_label = wx.StaticText(self, wx.ID_ANY, "User Name")
        RegisterDialog_vbox_hbox1_gbox.Add(UserNameEntered_label, (0, 0), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        self.UserNameEntered_text = wx.TextCtrl(self, wx.ID_ANY, "")
        RegisterDialog_vbox_hbox1_gbox.Add(self.UserNameEntered_text, (0, 1), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        SerialNumberEntered_label = wx.StaticText(self, wx.ID_ANY, "Serial Number")
        RegisterDialog_vbox_hbox1_gbox.Add(SerialNumberEntered_label, (1, 0), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        self.SerialNumberEntered_text = wx.TextCtrl(self, wx.ID_ANY, "")
        RegisterDialog_vbox_hbox1_gbox.Add(self.SerialNumberEntered_text, (1, 1), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        ProductKeyEntered_label = wx.StaticText(self, wx.ID_ANY, "Product Key")
        RegisterDialog_vbox_hbox1_gbox.Add(ProductKeyEntered_label, (2, 0), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        self.ProductKeyEntered_text = wx.TextCtrl(self, wx.ID_ANY, "")
        RegisterDialog_vbox_hbox1_gbox.Add(self.ProductKeyEntered_text, (2, 1), (1, 1), wx.ALIGN_CENTER_VERTICAL, 0)

        RegisterDialog_vbox_vbox1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Load license information from file"), wx.VERTICAL)
        RegisterDialog_vbox.Add(RegisterDialog_vbox_vbox1, 0, wx.ALL | wx.EXPAND, 5)

        self.LoadLicenseInfo_button = wx.Button(self, wx.ID_ANY, "Load License Info")
        RegisterDialog_vbox_vbox1.Add(self.LoadLicenseInfo_button, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        RegisterDialog_vbox_hbox2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Contact Info"), wx.HORIZONTAL)
        RegisterDialog_vbox.Add(RegisterDialog_vbox_hbox2, 0, wx.ALL | wx.EXPAND, 5)

        ContactInfo_label = wx.StaticText(self, wx.ID_ANY, "For questions and support contact:\n\narkarimp@gmail.com\nwww.arashkarimpour.com\n")
        RegisterDialog_vbox_hbox2.Add(ContactInfo_label, 0, wx.ALL, 5)

        RegisterDialog_vbox_bbox = wx.StdDialogButtonSizer()
        RegisterDialog_vbox.Add(RegisterDialog_vbox_bbox, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.OKRegistration_button = wx.Button(self, wx.ID_OK, "")
        self.OKRegistration_button.SetDefault()
        RegisterDialog_vbox_bbox.AddButton(self.OKRegistration_button)

        self.CANCELRegistration_button = wx.Button(self, wx.ID_CANCEL, "")
        RegisterDialog_vbox_bbox.AddButton(self.CANCELRegistration_button)

        RegisterDialog_vbox_bbox.Realize()

        self.SetSizer(RegisterDialog_vbox)
        RegisterDialog_vbox.Fit(self)

        self.SetAffirmativeId(self.OKRegistration_button.GetId())
        self.SetEscapeId(self.CANCELRegistration_button.GetId())

        self.Layout()
        self.Centre()

        self.Bind(wx.EVT_BUTTON, self.OnLoadLicenseInfo, self.LoadLicenseInfo_button)
        # end wxGlade

    def OnLoadLicenseInfo(self, event):  # wxGlade: MyDialog.<event_handler>
        #print("Event handler 'OnLoadLicenseInfo' not implemented!")
        #event.Skip()

        #Load license information from product key file
        wildcard = 'License files (*.*)|*.*'
        with wx.FileDialog(self, "Load License Information", wildcard=wildcard,
                        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     #User pressed Cancel

            #Get file information
            FilePath = fileDialog.GetPath()
            DirName = fileDialog.GetDirectory()
            FileName = fileDialog.GetFilename()
            FileRoot, FileExtension = os.path.splitext(FilePath)

            #Read user name, serial number, and product key from product key file loaded by user
            user_name_fromfile_loaded, serial_number_fromfile_loaded, product_key_fromfile_loaded = ReadProductKeyFile(FilePath)
            self.UserNameEntered_text.SetValue(user_name_fromfile_loaded)
            self.SerialNumberEntered_text.SetValue(serial_number_fromfile_loaded)
            self.ProductKeyEntered_text.SetValue(product_key_fromfile_loaded)

# end of class MyDialog

#--------------------------------------------------------------------------
class MyApp(wx.App):
    def OnInit(self):
        self.MainFrame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.MainFrame)
        self.MainFrame.Show()
        #ValidateLicense(self)
        return True

# end of class MyApp

#--------------------------------------------------------------------------
if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()

    #https://stackoverflow.com/questions/6256181/wx-app-object-must-be-created-first
    del app
#--------------------------------------------------------------------------
