function [wave]=CalcFun(OceanlyzInputFileName,OceanlyzFolder,OceanlyzPath)
%.. ++++++++++++++++++++++++++++++++YA LATIF++++++++++++++++++++++++++++++++++
%.. +                                                                        +
%.. + Oceanlyz                                                               +
%.. + Ocean Wave Analyzing Toolbox                                           +
%.. + Ver 1.5                                                                +
%.. +                                                                        +
%.. + Developed by: Arash Karimpour                                          +
%.. + Contact     : www.arashkarimpour.com                                   +
%.. + Developed/Updated (yyyy-mm-dd): 2020-07-01                             +
%.. +                                                                        +
%.. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
%  
%CalcFun
%=======
%
%.. code:: MATLAB
%
%    [wave]=CalcFun(OceanlyzInputFileName,OceanlyzFolder,OceanlyzPath)
%
%DESCRIPTION
%-----------
%
%Main calculating function, loading data, calling functions and passing values and parameters
%
%INPUT
%-----
%
%OceanlyzFolder
%                                OCEANLYZ folder location
%OceanlyzPath
%                                OCEANLYZ folder and its subfolders path
%
%OUTPUT
%------
%Output the wave properties depending on the selected module as a structure array such as:
%
%wave.Tp
%                                Peak wave period in (Second)
%wave.Hm0
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
%Printing

CurrentDate=clock;
clc;
disp('--------------------------------------------------')
disp('OCEANLYZ Ver 1.5')
disp('www.ArashKarimpour.com')
%disp('Copyright (C) 2018 Arash Karimpour')
disp(['Copyright (C) 2012-',num2str(CurrentDate(1)),' Arash Karimpour'])
disp('--------------------------------------------------')

%--------------------------------------------------------------------------
%Reading input values and parameters

disp('Reading input values and parameters')

ReadMethod='fgetl'; %Reading method 

[...
    InputFileName,InputFileFolder,...
    SaveOutput,OutputFileFolder,...
    AnalysisMethod,WaveParameterCalc,seaswellCalc,...
    n_burst,burst_duration,nfft,fs,heightfrombed,...
    fmin,fmax,fminpcorr,fmaxpcorr,ftailcorrection,tailpower,fminswell,fmaxswell,...
    pressureattenuation,autofmaxpcorr,mincutoff,maxcutoff,tailcorrection,dispout...
    ]...
    =ReadInputFile(OceanlyzInputFileName,OceanlyzFolder,ReadMethod);

%--------------------------------------------------------------------------
%Addinng the input folder and its subfolders to the search path

disp('Adding an input folder and its subfolders to the search path')
InputPath=genpath(InputFileFolder); % Generating path for input folder and its subfolders
addpath(InputPath);

%--------------------------------------------------------------------------
%Addinng the OCEANLYZ folder and its subfolders to the search path

disp('Adding an OCEANLYZ folder and its subfolders to the search path')
addpath(OceanlyzPath);

%--------------------------------------------------------------------------
%Assigning data file path

% disp('Assigning path')
% 
% if strcmp(OS,'win')==1
%     cd('.\Functions')
% elseif strcmp(OS,'linux')==1
%     cd('./Functions')
% end

%--------------------------------------------------------------------------
%Define a module number based on the input parameters

% module=1 : Calculates wave parameters using a spectral analysis method
%            Input Data: water depth or surface elevation data
% module=2 : Calculates wave parameters using a zero-crossing method
%            Input Data: water depth or surface elevation data
% module=3 : Correctes water wevel data measured by a pressure sensor, using a spectral analysis method (Fast Fourier Transform) 
%            It accounts for pressure attenuation in depth 
%            Input Data: water depth data measured by a pressure sensor
% module=4 : Correctes water level data measured by a pressure sensor, using the linear wave theory
%            It accounts for pressure attenuation in depth 
%            Input Data: water depth data measured by a pressure sensor
% module=5 : Separates wind sea and swell waves
%            Calculates wave parameters using a spectral analysis method
%            Input Data: water depth or surface elevation data
% module=6 : Correctes water level data measured by a pressure sensor, using a spectral analysis method (Fast Fourier Transform()
%            Calculates wave parameters using a spectral analysis method
%            It accounts for pressure attenuation in depth 
%            Input Data: water depth data measured by a pressure sensor
% module=7 : Correctes water level data measured by a pressure sensor, using the linear wave theory
%            Calculates wave parameters using a zero-crossing method
%            It accounts for pressure attenuation in depth 
%            Input Data: water depth data measured by a pressure sensor
% module=8 : Correctes wave pressure data using a spectral analysis method (Fast Fourier Transform)
%            Separates wind sea and swell waves
%            Calculates wave parameters using a spectral analysis method
%            It accounts for pressure attenuation in depth 
%            Input Data: water depth data measured by a pressure sensor

disp('--------------------------------------------------')
disp('Calculation Method:')

%Default value
module=1;

%Checking input values
if strcmp(WaveParameterCalc,'off')==1
    if strcmp(pressureattenuation,'off')==1
        pressureattenuation='all';
        disp('pressureattenuation is set to "all"')
    end
end

%Setting calculation method
if strcmp(AnalysisMethod,'spectral')==1
    if strcmp(WaveParameterCalc,'on')==1
        if strcmp(seaswellCalc,'off')==1
            if strcmp(pressureattenuation,'off')==1
                module=1;
                disp('module=1 : Calculates wave parameters using a spectral analysis method')
                disp('Input Data: water depth or surface elevation data')
            elseif (strcmp(pressureattenuation,'on')==1 | strcmp(pressureattenuation,'all')==1)
                module=6;
                disp('module=6 : Correctes water level data measured by a pressure sensor, using a spectral analysis method')
                disp('Calculates wave parameters using a spectral analysis method')
                disp('It accounts for pressure attenuation in depth')
                disp('Input Data: water depth data measured by a pressure sensor')
            end
        elseif strcmp(seaswellCalc,'on')==1
            if strcmp(pressureattenuation,'off')==1
                module=5;
                disp('module=5 : Separates wind sea and swell waves')
                disp('Calculates wave parameters using a spectral analysis method')
                disp('Input Data: water depth or surface elevation data')
            elseif (strcmp(pressureattenuation,'on')==1 | strcmp(pressureattenuation,'all')==1)
                module=8;
                disp('module=8 : Correctes wave pressure data using a spectral analysis method (Fast Fourier Transform)')
                disp('Separates wind sea and swell waves')
                disp('Calculates wave parameters using a spectral analysis method')
                disp('It accounts for pressure attenuation in depth')
                disp('Input Data: water depth data measured by a pressure sensor')
            end
        end
    elseif strcmp(WaveParameterCalc,'off')==1
        if (strcmp(pressureattenuation,'on')==1 | strcmp(pressureattenuation,'all')==1)
            module=3;
            disp('module=3 : Correctes water wevel data measured by a pressure sensor, using a spectral analysis method')
            disp('It accounts for pressure attenuation in depth')
            disp('Input Data: water depth data measured by a pressure sensor')
        end
    end
elseif strcmp(AnalysisMethod,'zerocross')==1
    if strcmp(WaveParameterCalc,'on')==1
        if strcmp(pressureattenuation,'off')==1
            module=2;
            disp('module=2 : Calculates wave parameters using a zero-crossing method')
            disp('Input Data: water depth or surface elevation data')
        elseif (strcmp(pressureattenuation,'on')==1 | strcmp(pressureattenuation,'all')==1)
            module=7;
            disp('module=7 : Correctes water level data measured by a pressure sensor, using the linear wave theory')
            disp('Calculates wave parameters using a zero-crossing method')
            disp('It accounts for pressure attenuation in depth')
            disp('Input Data: water depth data measured by a pressure sensor')
        end
    elseif strcmp(WaveParameterCalc,'off')==1
        if (strcmp(pressureattenuation,'on')==1 | strcmp(pressureattenuation,'all')==1)
            module=4;
            disp('module=4 : Correctes water level data measured by a pressure sensor, using the linear wave theory')
            disp('It accounts for pressure attenuation in depth')
            disp('Input Data: water depth data measured by a pressure sensor')
        end
    end
end

disp('--------------------------------------------------')

%--------------------------------------------------------------------------
%Calculating wave properties

disp('Calculating wave properties')

%pkg load signal; % for Octave GNU User, it loads Signal Package 

[wave]...
    =CalcWaveFun...
    (...
    InputFileName,InputFileFolder,...
    module,...
    n_burst,burst_duration,nfft,fs,heightfrombed,...
    fmin,fmax,fminpcorr,fmaxpcorr,ftailcorrection,tailpower,fminswell,fmaxswell,...
    pressureattenuation,autofmaxpcorr,mincutoff,maxcutoff,tailcorrection,dispout...
    );

%Output fields
disp('--------------------------------------------------')
disp('Output array is a structure array named "wave"')
disp('Field(s) in a structure array "wave" can be called by using "."')
disp('Example: Output for a peak wave period is : "wave.Tp"')
disp('Field names may be obtained from fieldnames(wave) command')
disp('Output field names are')
fieldnames(wave)
disp('--------------------------------------------------')

%--------------------------------------------------------------------------
%Saving output

if strcmp(SaveOutput,'on')==1
    disp('Saving output(s)')
    cd(OutputFileFolder)
    save('wave.mat','wave')
    disp('Output(s) is saved in an output folder in a file named "wave.mat" as a structure array')
    disp('--------------------------------------------------')
    cd(OceanlyzFolder)
end


%--------------------------------------------------------------------------
%Returning to OCEANLYZ folder

cd(OceanlyzFolder)

%--------------------------------------------------------------------------
%Removing input folder and OCEANLYZ floders and their subfolders from the search path

disp('Removing input folder and OCEANLYZ floders and their subfolders from the search path')

rmpath(InputPath);
rmpath(OceanlyzPath);

%--------------------------------------------------------------------------

disp('Calculation finished')
disp('--------------------------------------------------')

%--------------------------------------------------------------------------
