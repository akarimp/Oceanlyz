function [Eta,ftailcorrection]=PcorFFTFun(input,fs,duration,nfft,h,heightfrombed,fminpcorr,fmaxpcorr,ftailcorrection,pressureattenuation,autofmaxpcorr,dispout)
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
  
PcorFFTFun
==========

.. code:: MATLAB

    [Eta,ftailcorrection]=PcorFFTFun(input,fs,duration,nfft,h,heightfrombed,fminpcorr,fmaxpcorr,ftailcorrection,pressureattenuation,autofmaxpcorr,dispout)

DESCRIPTION
-----------

Apply pressure correction factor to water depth data from pressure gauge reading using FFT

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
fminpcorr=0.15;
                                Minimum frequency that automated calculated fmaxpcorr can have if autofmaxpcorr='on' in (Hz)
fmaxpcorr=0.8;
                                Maximum frequency for applying pressure attenuation factor
ftailcorrection=1;
                                Frequency that diagnostic tail apply after that (typically set at 2.5fm, fm=1/Tm01)
pressureattenuation='all';
                                Define if to apply pressure attenuation factor or not 
                                    pressureattenuation='off': No pressure attenuation applied

                                    pressureattenuation='on': Pressure attenuation applied without correction after fmaxpcorr

                                    pressureattenuation='all': Pressure attenuation applied with constant correction after fmaxpcorr
autofmaxpcorr='on';
                                Define if to calculate fmaxpcorr and ftailcorrection based on water depth or not
                                    autofmaxpcorr='off': Off

                                    autofmaxpcorr='on': On
dispout='on';
                                Define to display outputs or not ('off': not display, 'on': display)

OUTPUT
------

Eta
                                Corrected Water Surface Level Time Series (m)

EXAMPLE
-------

.. code:: MATLAB

    [Eta,ftailcorrection]=PcorFFTFun(water_pressure/(1000*9.81),10,1024,256,1.07,0.05,0.15,0.8,1,'all','on','on')

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

sample=fs*duration; %number of sample in input file
len=sample;
% h=mean(input(:,1)); %mean water depth in (m)
% h(h<=0)=0.001;
dt=1/fs; %calculating delta t in second (dt=duration/sample)
t(:,1)=linspace(dt,duration,sample); %time

%--------------------------------------------------------------------------

fmaxpcorr(fmaxpcorr>fs/2)=fix(fs/2);
%nfft = 2^(nextpow2(len));
f(:,1)=linspace(0,fs,len); %frequency
w=2*pi*f; %Angular frequency

%calculating Fast Fourier transform
FFTEta = fft(input1,len);
%Syy=abs((2/fs)*FFTEta.*conj(FFTEta)/len);
%Syy(f>fs/2)=0;
Syy=zeros(len,1);
[Syy_half,f1]=pwelch(input1,[],[],len,fs);
Syy(1:length(Syy_half(:,1)),1)=Syy_half;

%Estimation of wave number (k) from Hunt (1979)
%k0=w.^2/9.81; %Deep water wave number
%k0h=k0.*h;
%kh=k0h.*(1+k0h.^1.09.*exp(-(1.55+1.3.*k0h+0.216.*k0h.^2)))./sqrt(tanh(k0h)); %Calculating wave number from Beji (2013)
%kini=kh./h; %initial value for k (Wave number from Beji (2013))
%kini(w==0)=0;

%Estimation of wave number (k) from Goad (2010)
k0=w.^2/9.81; %Deep water wave number
k0h=k0.*h;
kh=zeros(length(k0h(:,1)),1);
kh(k0h>=1)=k0h(k0h>=1);
kh(k0h<1)=(k0h(k0h<1)).^0.5;
for i=1:3
    kh=kh-((kh-k0h.*coth(kh))./(1+k0h.*((coth(kh)).^2-1))); %Calculating wave number from Goda (2010)
end
k=kh./h; %Calculating wave number from Goda (2010)
k(w==0)=0;

%Calculation exact of wave number (k)
%for i=1:len
%    fun = @(x)(w(i,1)^2-(9.81*x*tanh(x*h)));
%    k(i,1)=fzero(fun,kini(i,1));
%end

%Calculation of pressure response factor
Kp=cosh(k*heightfrombed)./cosh(k*h);
kmaxL=pi./(h-heightfrombed); % Wave number associated with fmaxpcorrL
KpminL=cosh(kmaxL*heightfrombed)/cosh(kmaxL*h); % Minimum Limit for K_p calculated based on linear wave theory
Kp(Kp < KpminL) = KpminL; % Check to avoid large amplification, Kp should be larger than minimum K_p calculated based on linear wave theory

%automatically estimating fmaxpcorr and ftailcorrection
if strcmp(autofmaxpcorr,'on')==1
    locfminpcorr=max(find(f<=fminpcorr)); %Locating the location of fminpcorr (fmaxpcorr should be larger than fminpcorr)
    [Syymax locSyymax]=max(Syy(locfminpcorr:end,1)); % Locating the peak frequency, fp, of original dataset
    fmaxpcorrL=1/(2*pi)*sqrt(9.81*kmaxL*tanh(kmaxL*h)); % Maximum frequency that K_p can be applied, calculated from linear wave theory
    locfmaxpcorrL=max(find(f<=fmaxpcorrL)); %Location the location of fmaxpcorr1
    locfmaxpcorrL(locfmaxpcorrL<locfminpcorr+(locSyymax-1))=locfminpcorr+(locSyymax-1); %Check if locfmaxpcorrL locataed after fp
    Syy1=Syy./(Kp.^2);
    [Syymin locSyymin]=min(Syy1(locfminpcorr+(locSyymax-1):locfmaxpcorrL,1));%Locating the location of minimum value for Syy between fp and fmaxpcorr1
    fmaxpcorr1=f(locfminpcorr+(locSyymax-1)+(locSyymin-1),1);%Asigning the frequency of the location of minimum value for Syy between fp and fmaxpcorr1
    ftailcorrection1=f(locfminpcorr+(locSyymax-1)+(locSyymin-1),1);
    fmaxpcorr1(fmaxpcorr1>fmaxpcorrL)=fmaxpcorrL;%Check fmaxpcorr1 be smaller than fmaxpcorrL
    fmaxpcorr1(fmaxpcorr1==f(locfminpcorr+(locSyymax-1))&fmaxpcorrL>f(locfminpcorr+(locSyymax-1)))=fmaxpcorrL;%if fmaxpcorrL>fp then fmaxpcorr1 should not be equal to fp
    ftailcorrection1(ftailcorrection1>fmaxpcorrL)=fmaxpcorrL;
    fmaxpcorr(fmaxpcorr>fmaxpcorr1)=fmaxpcorr1;
    ftailcorrection(ftailcorrection>ftailcorrection1)=ftailcorrection1;
end

if strcmp(pressureattenuation,'off')==1
    Kp(1:end,1)=1;

elseif strcmp(pressureattenuation,'on')==1

    Kp(f>fmaxpcorr)=1; % correction factor larger than fmaxpcorr should be 1 (no correction)

    % linear decrease of correction for f larger than maximum frequency
    loc1=max(find(f<=fmaxpcorr-0.05));
    loc2=max(find(f<=fmaxpcorr+0.05));
    loc2(loc2>length(f))=length(f);
    for i=loc1:loc2
        Kp(i)=(Kp(loc2)-Kp(loc1))/(loc2-loc1)*(i-loc1)+Kp(loc1);
    end

elseif strcmp(pressureattenuation,'all')==1
    loc2=max(find(f<=fmaxpcorr));
    loc2(loc2>length(f))=length(f);
    Kp(f>fmaxpcorr)=Kp(loc2); % correction factor larger than fmaxpcorr stays constant
end

Kp1=Kp(1:len/2,1);
Kp1=flipud(Kp1);
Kp(len/2+1:end,1)=Kp1; %make Kp symetric around fr/2

%correcting pressure
FFTEtacor= FFTEta./Kp;			    % applies corection factor
Eta = real(ifft(FFTEtacor,len));	% corected water surface levels time series

%--------------------------------------------------------------------------
%Displaying results

if strcmp(dispout,'on')==1
    plot(t,input1)
    hold on
    plot(t,Eta,'r')
    xlim([t(1,1) t(end,1)])
    title('Water Level')
    xlabel('Time(s)')
    ylabel('\eta(m)')
    legend('Original Water Level','Corrected Water Level')
end

%--------------------------------------------------------------------------
