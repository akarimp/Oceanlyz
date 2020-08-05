function [Hm0,Hm0sea,Hm0swell,Tp,Tpsea,Tpswell,fp,fseparation,f,Syy]=SeaSwellFun(input,fs,duration,nfft,h,fmin,fmax,ftailcorrection,tailpower,fminswell,fmaxswell,mincutoff,maxcutoff,tailcorrection,dispout)
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
%SeaSwellFun
%===========
%
%.. code:: MATLAB
%
%    [Hm0,Hm0sea,Hm0swell,Tp,Tpsea,Tpswell,fp,fseparation,f,Syy]=SeaSwellFun(input,fs,duration,nfft,h,fmin,fmax,ftailcorrection,tailpower,fminswell,fmaxswell,mincutoff,maxcutoff,tailcorrection,dispout)
%
%DESCRIPTION
%-----------
%
%Separate sea wave from swell wave
%
%INPUT
%-----
%
%input=importdata('h.mat');
%                                Load water depth (h)/surface elevation (Eta) data and rename it "input" in (m)
%fs=10;
%                                Sampling frequency that data collected at in (Hz)
%duration=1024;
%                                Duration time that data collected in input in each burst in second
%nfft=2^10;
%                                NFFT for Fast Fourier Transform
%h=1;
%                                Mean water depth in (m)
%fmin=0.04;
%                                Minimum frequency for cut off the lower part of spectra
%fmax=1;
%                                Maximum frequency for cut off the upper part of spectra
%ftailcorrection=1;
%                                Frequency that diagnostic tail apply after that (typically set at 2.5fm, fm=1/Tm01)
%tailpower=-4;
%                                Power that diagnostic tail apply based on that (-3 for shallow water to -5 for deep water)
%fminswell=0.1;
%                                Minimum frequency that is used for Tpswell calculation
%fmaxswell=0.25;
%                                Maximum frequency that swell can have, It is about 0.2 in Gulf of Mexico
%mincutoff='off';
%                                Define if to cut off the spectra below fmin
%                                    mincutoff='off': Cutoff off
%
%                                    mincutoff='on': Cutoff on
%maxcutoff='off';
%                                Define if to cut off the spectra beyond fmax
%                                    maxcutoff='off': Cutoff off
%
%                                    maxcutoff='on': Cutoff on
%tailcorrection='off';
%                                Define if to apply diagnostic tail correction or not 
%                                    tailcorrection='off': Not apply
%
%                                    tailcorrection='jonswap': JONSWAP Spectrum tail
%
%                                    tailcorrection='tma': TMA Spectrum tail
%dispout='on';
%                                Define to display outputs or not ('off': not display, 'on': display)
%
%OUTPUT
%------
%
%Hm0
%                                Zero-Moment Wave Height (m)
%Hm0sea
%                                Sea Zero-Moment Wave Height (m)
%Hm0swell
%                                Swell Zero-Moment Wave Height (m)
%Tp
%                                Peak wave period (second)
%Tpsea
%                                Peak Sea period (second)
%Tpswell
%                                Peak Swell Period (second)
%fp
%                                Peak Wave Frequency (Hz)
%f
%                                Frequency (Hz)
%fseparation
%                                Sea and Swell Separation Frequency (Hz)
%Syy
%                                Wave Surface Elevation Power Spectrum (m^2s)
%
%EXAMPLE
%-------
%
%.. code:: MATLAB
%
%    [Hm0,Hm0sea,Hm0swell,Tp,Tpswell,fp,fseparation,f,Syy]= SeaSwellFun(input,10,1024,2^10,1.07,0.05,2,0.9,-4,0.1,0.25,'on','on','off','on');
%
%EXAMPLE
%-------
%
%.. code:: MATLAB
%
%    [Eta]=PcorFFTFun(input,10,1024,2^10,1.07,0.05,0.04,0.8,'all','off','on');
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
%deterending

input1=detrend(input,'linear');

%--------------------------------------------------------------------------
%calculating Fast Fourier transform and power density

fmax(fmax>fs/2)=fix(fs/2);
%nfft = 2^(nextpow2(length(input1)));

%--------------------------------------------------------------------------
%calculating power density 

windowelem = 256; % number of elements in each window
overlapelem = 128; %number of overlap element

%[Syy,f] = pwelch(input1,hanning(windowelem),overlapelem,nfft,fs); %Wave power spectrum and Frequency
[Syy,f]=pwelch(input1,[],[],nfft,fs); %Wave power spectrum and Frequency

w=2*pi*f; %angular velocity
deltaf=f(2,1)-f(1,1);

%--------------------------------------------------------------------------
%Applying tail correction

%Index of ftailcorrection
Indxftail=min(find(f>=ftailcorrection));

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
%calculating 1D separation frequency of sea from swell (Hwang, 2012)
%Hwang, P. A., Francisco J. O. T., H?ctor G. N., 2012, Wind sea and swell separation of 1d wave spectrum by a spectrum integration method, J. Atmos. Oceanic Technol., 29, 116?128.

fup=f(f<=0.5);
for i1=1:length(fup(:,1))
    fstar(i1,1)=fup(i1,1);
    m1fstar(i1,1)=sum(Syy(i1:length(fup(:,1)),1).*f(i1:length(fup(:,1)),1).^1*deltaf);
    mminus1fstar(i1,1)=sum(Syy(i1:length(fup(:,1)),1).*f(i1:length(fup(:,1)),1).^(-1)*deltaf);
end

alfafstar=(m1fstar)./sqrt(mminus1fstar);

[alfafstarmax loc1]=max(alfafstar(:,1));
fm=fstar(loc1,1);
fseparation=24.2084*fm^3-9.2021*fm^2+1.8906*fm-0.04286;

fseparation(fseparation>fmaxswell | fseparation==inf | fseparation==NaN | fseparation==0)=fmaxswell; %fseperation is about 0.2 in Gulf of Mexico
    
%calculate the exact location of separation frequency
loc2=length(find(f<=fseparation)); %location of fseperation
fpsea1=(sum(Syy(loc2:end,1).^5.*f(loc2:end,1).^1*deltaf))./(sum(Syy(loc2:end,1).^5.*f(loc2:end,1).^0*deltaf)); %sea peak frequency based on fseparation from previous step
fpswell1=(sum(Syy(1:loc2,1).^5.*f(1:loc2,1).^1*deltaf))./(sum(Syy(1:loc2,1).^5.*f(1:loc2,1).^0*deltaf));%swell peak frequency based on fseparation from previous step
[Syyminswell loc7]=min(Syy(f<fpsea1 & f>fpswell1));
loc8=length(find(f<=fpswell1)); 
fseparation=f(loc7+loc8,1);
fseparation(fseparation>fmaxswell | fseparation==inf | fseparation==NaN | fseparation==0)=fmaxswell; %fseperation is about 0.2 in Gulf of Mexico
fseparation(length(fseparation)==0)=fmaxswell; %fseperation is about 0.2 in Gulf of Mexico

%--------------------------------------------------------------------------

%Calculating spectral moments
clear m0 m1 m2

m0=sum(Syy.*f.^0*deltaf);

% calculating wave properties
Hm0=4*sqrt(m0); %Zero-Moment wave height

% calculation peak period
[Syymax loc6]=max(Syy(:,1));
Tp=1/f(loc6,1); %peak period

% calculating peak frequency from weighted integral (Young, 1995)
fp=(sum(Syy.^5.*f.^1*deltaf))./(sum(Syy.^5.*f.^0*deltaf)); %peak frequency

%--------------------------------------------------------------------------
%calculating swell and sea

loc2=length(find(f<=fseparation)); %location of fseperation
m0swell=sum(Syy(1:loc2,1).*f(1:loc2,1).^0*deltaf);
m0sea=sum(Syy(loc2+1:end,1).*f(loc2+1:end,1).^0*deltaf); %Zero-Moment wave height
Hm0sea=4*sqrt(m0sea); %sea Zero-Moment wave height
Hm0swell=4*sqrt(m0swell); %swell Zero-Moment wave height
[Syymaxsea loc3]=max(Syy(loc2:end,:));
Tpsea=1/(f(loc2+loc3-1,1)); %sea peak period, loc4+loc5-1 is the location of sea peak
loc4=length(find(f<=fminswell)); %location of fminswell
if loc4>=loc2
    loc4=1
end
[Syymaxswell loc5]=max(Syy(loc4:loc2,:));
Tpswell=1/(f(loc4+loc5-1,1)); %swell peak period, loc4+loc5-1 is the location of swell peak
fpsea=(sum(Syy(loc2:end,1).^5.*f(loc2:end,1).^1*deltaf))./(sum(Syy(loc2:end,1).^5.*f(loc2:end,1).^0*deltaf)); %sea peak frequency based on fseparation from previous step
fpswell=(sum(Syy(1:loc2,1).^5.*f(1:loc2,1).^1*deltaf))./(sum(Syy(1:loc2,1).^5.*f(1:loc2,1).^0*deltaf));%swell peak frequency based on fseparation from previous step

%--------------------------------------------------------------------------
%Displaying results

if strcmp(dispout,'on')==1
    
    val=[Hm0 Hm0sea Hm0swell Tp Tpsea Tpswell fp fseparation];
    name={'Hm0','Hm0-sea','Hm0-swell','Tp','Tp-sea','Tp-swell','fp','fseparation'};
    for i=1:length(val)
        fprintf('%14s   %g\n',name{i},val(i));
    end
    
    %plotting
    loglog(f(f~=0),Syy(f~=0))
    hold on
    loglog([fseparation fseparation],[min(Syy(Syy~=0)) max(Syy)],'m-.')
    
    title('Power Spectral Density')
    xlabel('Frequency(Hz)')
    ylabel('Spectral Density(m^2s)')
    
end
%--------------------------------------------------------------------------
