function [wave]...
    =CalcWaveFun...
    (...
    InputFileName,InputFileFolder,...
    module,...
    burst,duration,nfft,fs,heightfrombed,...
    fmin,fmax,fminpcorr,fmaxpcorr,ftailcorrection,tailpower,fminswell,fmaxswell,...
    pressureattenuation,autofmaxpcorr,mincutoff,maxcutoff,tailcorrection,dispout...
    )
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
%CalcWaveFun
%===========
%
%.. code:: MATLAB
%
%    [wave]...
%    =CalcWaveFun...
%    (...
%    InputFileName,InputFileFolder,...
%    module,...
%    burst,duration,nfft,fs,heightfrombed,...
%    fmin,fmax,fminpcorr,fmaxpcorr,ftailcorrection,tailpower,fminswell,fmaxswell,...
%    pressureattenuation,autofmaxpcorr,mincutoff,maxcutoff,tailcorrection,dispout...
%    )
%
%DESCRIPTION
%-----------
%
%Calculate wave properties
%
%INPUT
%-----
%
%Oceanlyz input values and parameters
%
%OUTPUT
%------
%
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
%Load water depth data

currentpath=pwd;
cd(InputFileFolder);
d=importdata(InputFileName);

%Checking if inputs are column vectors
if isrow(d)==1, 
    d=d';
end

%Checking data for NaN
if sum(isnan(d))~=0
    %error('Input file contains NaN value(s), Oceanlyz will be terminated.');
    warning('Input file contains NaN value(s).');
    warning('NaN value(s) are replaced by linearly interpolated value(s).');
    warning('Oceanlyz contniues with modified data.');
    
    %Replacing NaN values
    Indx(:,1)=linspace(1,length(d(:,1)),length(d(:,1)));
    d=interp1(Indx(isnan(d)==0),d(isnan(d)==0),Indx);
end

%Checking data for Inf
if sum(isinf(d))~=0
    %error('Input file contains Inf value(s), Oceanlyz will be terminated.');
    warning('Input file contains Inf value(s).');
    warning('Inf value(s) are replaced by linearly interpolated value(s).');
    warning('Oceanlyz contniues with modified data.');
    
    %Replacing Inf values
    Indx(:,1)=linspace(1,length(d(:,1)),length(d(:,1)));
    d=interp1(Indx(isinf(d)==0),d(isinf(d)==0),Indx);
end

%Checking data for zero values
if sum(d==0)~=0
    warning('Input file contains Zero value(s), Oceanlyz contniues with current data.');
end

%--------------------------------------------------------------------------

sample=fs*duration; %number of sample in 1 burst
fmaxpcorr1=fmaxpcorr; %storing user defined fmaxpcorr

%define if pressure attenuation factor applied or not
%pressureattenuation='off': No pressure attenuation applied
%pressureattenuation='on': Pressure attenuation applied without correction after fmaxpcorr
%pressureattenuation='all': Pressure attenuation applied with constant correction after fmaxpcorr

if module==3 | module==4 | module==6 | module==7 | module==8
    pressureattenuation=pressureattenuation; %Define if pressure attenuation factor applied or not
else
    pressureattenuation='off'; %Define if pressure attenuation factor applied or not
end

%CALLING-FUNCTION----------------------------------------------------------
% Calling calculation functions

cd(currentpath);

for i=1:burst
    
    if strcmp(dispout,'on')==1
        Step=['Burst = ',num2str(i)];
        disp('--------------------------------------------------')
        disp(Step)
    end

    %loading data
    j1=(i-1)*sample+1;
    j2=i*sample;
    input=d(j1:j2,1);
    h=mean(input(:,1)); % calculating mean water depth
    if h<=0
	    warning('Mean water depth is Zero or negative, Oceanlyz contniues with mean water depth=0.001 m.');
        h=0.001;
    end
	
    %calling function
    if module==1
        [wave.Hm0(i,1),wave.Tm01(i,1),wave.Tm02(i,1),wave.Tp(i,1),wave.fp(i,1),wave.f(i,:),wave.Syy(i,:)]=WaveSpectraFun(input,fs,duration,nfft,h,heightfrombed,fmin,fmax,ftailcorrection,tailpower,mincutoff,maxcutoff,tailcorrection,dispout);
    
    elseif module==2
        [wave.Hs(i,1),wave.Hz(i,1),wave.Tz(i,1),wave.Ts(i,1)]=WaveZerocrossingFun(input,fs,duration,'off');
    
    elseif module==3
        [wave.Eta(i,:),ftailcorrection]=PcorFFTFun(input,fs,duration,nfft,h,heightfrombed,fminpcorr,fmaxpcorr,ftailcorrection,pressureattenuation,autofmaxpcorr,'off');
    
    elseif module==4
        [wave.Eta(i,:)]=PcorZerocrossingFun(input,fs,duration,h,heightfrombed,'off');
    
    elseif module==5
        [wave.Hm0(i,1),wave.Hm0sea(i,1),wave.Hm0swell(i,1),wave.Tp(i,1),wave.Tpsea(i,1),wave.Tpswell(i,1),wave.fp(i,1),wave.fseparation(i,1),wave.f(i,:),wave.Syy(i,:)]=SeaSwellFun(input,fs,duration,nfft,h,fmin,fmax,ftailcorrection,tailpower,fminswell,fmaxswell,mincutoff,maxcutoff,tailcorrection,dispout);
    
    elseif module==6
       [wave.Eta(i,:),ftailcorrection]=PcorFFTFun(input,fs,duration,nfft,h,heightfrombed,fminpcorr,fmaxpcorr,ftailcorrection,pressureattenuation,autofmaxpcorr,'off'); 
       [wave.Hm0(i,1),wave.Tm01(i,1),wave.Tm02(i,1),wave.Tp(i,1),wave.fp(i,1),wave.f(i,:),wave.Syy(i,:)]=WaveSpectraFun((wave.Eta(i,:))',fs,duration,nfft,h,heightfrombed,fmin,fmax,ftailcorrection,tailpower,mincutoff,maxcutoff,tailcorrection,dispout);
    
    elseif module==7
        [wave.Eta(i,:)]=PcorZerocrossingFun(input,fs,duration,h,heightfrombed,'off');
        [wave.Hs(i,1),wave.Hz(i,1),wave.Tz(i,1),wave.Ts(i,1)]=WaveZerocrossingFun((wave.Eta(i,:))',fs,duration,'off');
    
    elseif module==8
        [wave.Eta(i,:),ftailcorrection]=PcorFFTFun(input,fs,duration,nfft,h,heightfrombed,fminpcorr,fmaxpcorr,ftailcorrection,pressureattenuation,autofmaxpcorr,'off');
        [wave.Hm0(i,1),wave.Hm0sea(i,1),wave.Hm0swell(i,1),wave.Tp(i,1),wave.Tpsea(i,1),wave.Tpswell(i,1),wave.fp(i,1),wave.fseparation(i,1),wave.f(i,:),wave.Syy(i,:)]=SeaSwellFun((wave.Eta(i,:))',fs,duration,nfft,h,fmin,fmax,ftailcorrection,tailpower,fminswell,fmaxswell,mincutoff,maxcutoff,tailcorrection,dispout);
    end
    
    if strcmp(dispout,'on')==1
        wb=waitbar(i/burst);
        waitbar(i/burst,wb,sprintf('Percentage = %0.2f',i/burst*100))
    end

end

wave.Input=d; % Saving input water depth

%--------------------------------------------------------------------------

