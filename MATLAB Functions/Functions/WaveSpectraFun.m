function [Hm0,Tm01,Tm02,Tp,fp,f,Syy]=WaveSpectraFun(input,fs,duration,nfft,h,heightfrombed,fmin,fmax,ftailcorrection,tailpower,mincutoff,maxcutoff,tailcorrection,dispout)
%{
.. ++++++++++++++++++++++++++++++++YA LATIF++++++++++++++++++++++++++++++++++
.. +                                                                        +
.. + Oceanlyz                                                               +
.. + Ocean Wave Analyzing Toolbox                                           +
.. + Ver 2.0                                                                +
.. +                                                                        +
.. + Developed by: Arash Karimpour                                          +
.. + Contact     : www.arashkarimpour.com                                   +
.. + Developed/Updated (yyyy-mm-dd): 2020-08-01                             +
.. +                                                                        +
.. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

WaveSpectraFun
==============

.. code:: MATLAB

    [Hm0,Tm01,Tm02,Tp,fp,f,Syy]=WaveSpectraFun(input,fs,duration,nfft,h,heightfrombed,fmin,fmax,ftailcorrection,tailpower,mincutoff,maxcutoff,tailcorrection,dispout)

DESCRIPTION
-----------

Calculate wave properties from power spectral density

INPUT
-----

input=importdata('h.mat');
                                Load water depth (h)/surface elevation (Eta) data and rename it "input" in (m)
fs=10;
                                Sampling frequency that data collected at in (Hz)
duration=1024;
                                Duration time that data collected in input in each burst in second
nfft=2^10;
                                NFFT for Fast Fourier Transform
h=1;
                                Mean water depth in (m)
heightfrombed=0.0;
                                Sensor height from bed
fmin=0.04;
                                Minimum frequency for cut off the lower part of spectra
fmax=1;
                                Maximum frequency for cut off the upper part of spectra
ftailcorrection=1;
                                Frequency that diagnostic tail apply after that (typically set at 2.5fm, fm=1/Tm01)
tailpower=-4;
                                Power that diagnostic tail apply based on that (-3 for shallow water to -5 for deep water)
mincutoff='off';
                                Define if to cut off the spectra below fmin
                                    mincutoff='off': Cutoff off

                                    mincutoff='on': Cutoff on
maxcutoff='off';
                                Define if to cut off the spectra beyond fmax
                                    maxcutoff='off': Cutoff off

                                    maxcutoff='on': Cutoff on
tailcorrection='off';
                                Define if to apply diagnostic tail correction or not 
                                    tailcorrection='off': Not apply

                                    tailcorrection='jonswap': JONSWAP Spectrum tail

                                    tailcorrection='tma': TMA Spectrum tail
dispout='on';
                                Define to display outputs or not ('off': not display, 'on': display)

OUTPUT
------

Hm0
                                Zero-Moment Wave Height (m)
Tm01
                                Wave Period from m01 (second), Mean Wave Period
Tm02
                                Wave Period from m02 (second), Mean Zero Crossing Period
Tp
                                Peak Wave Period (second)
fp
                                Peak Wave Frequency (Hz)
f
                                Frequency (Hz)
Syy
                                Wave Surface Elevation Power Spectrum (m^2s)

EXAMPLE
-------

.. code:: MATLAB

    [Hm0,Tm01,Tm02,Tp,fp,f,Syy]=WaveSpectraFun(water_pressure/(1000*9.81),10,1024,256,1.07,0.05,0.05,5,1,-5,'on','on','off','on')

.. LICENSE & DISCLAIMER
.. -------------------- 
.. Copyright (c) 2020 Arash Karimpour
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
%}

%--------------------------------------------------------------------------
%CODE
%--------------------------------------------------------------------------
%deterending

input1=detrend(input,'linear');

%--------------------------------------------------------------------------
%calculating Fast Fourier transform and power density

fmax(fmax>fs/2)=fix(fs/2);
%nfft = 2^(nextpow2(length(input1)));

%--------------------------------------------------------------------------
clear j1 j2 i

%calculating power density 

clear f w HS hpsd Syy

windowelem = 256; %number of elements in each window
overlapelem = 128; %number of overlap element

%[Syy,f] = pwelch(input1,hanning(windowelem),overlapelem,nfft,fs); %Wave power spectrum and Frequency
[Syy,f]=pwelch(input1,[],[],nfft,fs); %Wave power spectrum and Frequency

w=2*pi*f; %angular velocity
deltaf=f(2,1)-f(1,1);

%--------------------------------------------------------------------------
%Applying tail correction

%Index of ftailcorrection
if strcmp(tailcorrection,'jonswap')==1 | strcmp(tailcorrection,'tma')==1
    Indxftail=min(find(f>=ftailcorrection));
end

%Applying diagnostic frequency tail based on JONSWAP after fmax
if strcmp(tailcorrection,'jonswap')==1
    
    Syy(f>ftailcorrection)=Syy(Indxftail,1).*(f(f>ftailcorrection)./ftailcorrection).^tailpower; %Adding diagnostic tail
    Syy(Syy<0)=0; %Syy can not be negative

%Applying diagnostic frequency tail based on TMA after fmax
elseif strcmp(tailcorrection,'tma')==1
    
    omega=2*pi.*f.*sqrt(h/9.81);

    %Transformation function from JONSWAP into TMA, approximated method
    PHI=ones(length(omega(:,1)),1);
    PHI(omega<=1)=omega(omega<=1).^2./2;
    PHI(omega>1 & omega<2)=1-0.5*(2-omega(omega>1 & omega<2)).^2;
    PHI(omega>=2)=1;

    Syy(f>ftailcorrection)=Syy(Indxftail,1).*(PHI(f>ftailcorrection)./PHI(Indxftail,1)).*(f(f>ftailcorrection)./ftailcorrection).^tailpower; %Adding TMA Spectrum tail
    Syy(Syy<0)=0; %Syy can not be negative

end

%--------------------------------------------------------------------------
%cut off spectra based on fmin and fmax 

if strcmp(mincutoff,'on')==1
    Syy(f<fmin)=0;
end

if strcmp(maxcutoff,'on')==1
    Syy(f>fmax)=0;
end

%--------------------------------------------------------------------------

%Calculating spectral moments
clear m0 m1 m2

m0=sum(Syy.*f.^0*deltaf);
m1=sum(Syy.*f.^1*deltaf);
m2=sum(Syy.*f.^2*deltaf);

%calculating wave properties
Hm0=4*sqrt(m0); %Zero-Moment wave height
Tm01=m0/m1; %mean period
Tm02=(m0/m2)^0.5; %zero crossing period

%calculation peak period
[Syymax loc4]=max(Syy(:,1));
Tp=1/f(loc4,1); %peak period

%calculating peak frequency from weighted integral (Young, 1995)
fp=(sum(Syy.^5.*f.^1*deltaf))./(sum(Syy.^5.*f.^0*deltaf)); %peak frequency

%--------------------------------------------------------------------------
%Displaying results

if strcmp(dispout,'on')==1
    
    val=[m0 m1 m2 Hm0 Tm01 Tm02 Tp fp];
    name={'m0','m1','m2','Hm0','Tm01','Tm02','Tp','fp'};
    for i=1:length(val)
        fprintf('%14s   %g\n',name{i},val(i));
    end
    
    %plotting
    loglog(f(f~=0),Syy(f~=0))
    hold on
    
    title('Power Spectral Density')
    xlabel('Frequency(Hz)')
    ylabel('Spectral Density(m^2s)')
    
end
%--------------------------------------------------------------------------
