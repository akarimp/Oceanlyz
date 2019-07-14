%.. ++++++++++++++++++++++++++++++++YA LATIF++++++++++++++++++++++++++++++++++
%.. +                                                                        +
%.. + Oceanlyz                                                               +
%.. + Ocean Wave Analyzing Toolbox                                           +
%.. + Ver 1.4                                                                +
%.. +                                                                        +
%.. + Developed by: Arash Karimpour                                          +
%.. + Contact     : www.arashkarimpour.com                                   +
%.. + Developed/Updated (yyyy-mm-dd): 2019-07-01                             +
%.. +                                                                        +
%.. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
%
%RunOceanlyz
%===========
%
%DESCRIPTION
%-----------
%
%Runs Oceanlyz
%
%INPUT
%-----
%
%OUTPUT
%------
%Output the wave properties depending on the selected parameters as a structure array such as:
%
% wave.Tp
%                                Peak wave period in (Second)
% wave.Hm0
%                                Zero-moment wave height in (m)
%
%Output is a structure array
%Name of output file is 'wave.mat'
%Name of output array is 'wave'
%Field(s) in 'wave' structure array can be called by using '.'
%Example: Output peak wave period is : "wave.Tp"
%
%EXAMPLE
%-------
%
%.. LICENSE & DISCLAIMER
%.. -------------------- 
%.. Copyright (c) 2018 Arash Karimpour
%..
%.. http://www.arashkarimpour.com
%..
%.. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
%.. IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
%.. FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
%.. AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
%.. LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
%.. OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
%.. SOFTWARE.
%
%==========================================================================

%CODE
%--------------------------------------------------------------------------
%Clearing all variables

%clear all;

%--------------------------------------------------------------------------
%Turnning off warning

warning('off');

%--------------------------------------------------------------------------
%Addinng the OCEANLYZ folder and its subfolders to the search path

OceanlyzFolder=pwd; %Current (OCEANLYZ) path
OceanlyzPath=genpath(OceanlyzFolder); %Generating path for OCEANLYZ folder and its subfolders
addpath(OceanlyzPath);

%FUNCTION------------------------------------------------------------------
%Calling main calculating function

OceanlyzInputFileName='oceanlyzinput.m'; %Oceanlyz input file name in ' ', example:'oceanlyzinput.m'

[wave]=CalcFun(OceanlyzInputFileName,OceanlyzFolder,OceanlyzPath);

%--------------------------------------------------------------------------
%Removing OCEANLYZ floder and its subfolders from the search path

rmpath(OceanlyzPath);

%--------------------------------------------------------------------------
%Turnning on warning

warning('on');

%--------------------------------------------------------------------------
%Clearing all variables except wave properties

clear OceanlyzInputFileName
clear OceanlyzFolder
clear OceanlyzPath

%--------------------------------------------------------------------------
