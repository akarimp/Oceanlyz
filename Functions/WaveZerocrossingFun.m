function [Hs,Hz,Tz,Ts,H,T]=WaveZerocrossingFun(input,fs,duration,dispout)
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

WaveZerocrossingFun
===================

.. code:: MATLAB

    [Hs,Hz,Tz,Ts,H,T]=WaveZerocrossingFun(input,fs,duration,dispout)

DESCRIPTION
-----------

Calculate wave properties using Up-going zero crossing method

INPUT
-----

input=importdata('h.mat');
                                Load water depth (h)/surface elevation (Eta) data and rename it "input" in (m)
fs=10;
                                Sampling frequency that data collected at in (Hz)
duration=1024;
                                Duration time that data collected in input in each burst in second
dispout='on';
                                Define to display outputs or not ('off': not display, 'on': display)

OUTPUT
------

Hs
                                Significant Wave Height (m)
Hz
                                Zero Crossing Mean Wave Height (m)
Tz
                                Zero Crossing Mean Wave Period (second)
Ts
                                Significant Wave Period (second)
H
                                Wave Height Data Series (m)
T
                                Wave Period Data Series (second)

EXAMPLE
-------

.. code:: MATLAB

    [Hs,Hz,Tz,Ts,H,T]=WaveZerocrossingFun(water_pressure/(1000*9.81),10,1024,'on')

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

sample=duration*fs; %number of sample in input file
dt=1/fs; %calculating delta t in second (dt=duration/sample)
t(:,1)=linspace(dt,duration,sample); %time
len=length(t(:,1));
input1=detrend(input,'linear');

%--------------------------------------------------------------------------
% detecting the start point of first wave (fisr complete crest-trough)

if input1(1,1)==0 & input1(2,1)>0 
    len3=1;
end

if (input1(1,1)==0 & input1(2,1)<0) | (input1(1,1)~=0)
    for i=1:len-1
        if input1(i,1)<0 & input1(i+1,1)>0 
            len3=i;
            break
        end
    end
end

% detecting the end point of last wave (fisr complete crest-trough)

if input1(end,1)==0 & input1(end-1,1)<0 
    len4=len;
end

if (input1(end,1)==0 & input1(end-1,1)>0) | (input1(end,1)~=0)
    for i=len-1:-1:1
        if input1(i,1)<0 & input1(i+1,1)>0 
            len4=i;
            break
        end
    end
end

%--------------------------------------------------------------------------
% detecting zero crossing points from original data

m=0;
n=0;

for i=len3:len4 
    
    %detecting up-crossing zero-crossing points
    if i==1
        m=m+1;
        xupcross(m,1)=dt;
        yupcross(m,1)=0;
        positionxupcross(m,1)=i;
    end
    
    if i>1 & i<len
        if input1(i,1)<0 & input1(i+1,1)>0
            m=m+1;
            xupcross(m,1)=t(i,1)-(t(i+1,1)-t(i,1))/(input1(i+1,1)-input1(i,1))*input1(i,1);
            yupcross(m,1)=0;
            positionxupcross(m,1)=i;
        end
    end
    
    if i==len
        m=m+1;
        xupcross(m,1)=t(end,1);
        yupcross(m,1)=0;
        positionxupcross(m,1)=i;
    end
    
    %detecting down-crossing zero-crossing points
    if i>1 & i<len
        if input1(i,1)>0 & input1(i+1,1)<0
            n=n+1;
            xdowncross(n,1)=t(i,1)-(t(i+1,1)-t(i,1))/(input1(i+1,1)-input1(i,1))*input1(i,1);
            ydowncross(n,1)=0;
            positionxdowncross(n,1)=i;
            if positionxdowncross(n,1)>=len
                positionxdowncross(n,1)=len-1;
            end
        end
    end
    
end

%--------------------------------------------------------------------------
% detecting crest and trough from original data

m=0;
n=0;
for i=positionxupcross(1,1):positionxupcross(end,1)
    
    % detecting crest
    if i>1 & i<len
        
        if input1(i,1)>input1(i-1,1) & input1(i,1)>input1(i+1,1)
            
            if input1(i,1)>0
                
                if m==n % check if after last crest, the program detect the trough or not (m==n mean it detected and the new y(i,1) is the crest in next wave)
                    
                    m=m+1;
                    xmax(m,1)=t(i,1);
                    ymax(m,1)=input1(i,1);
                    positionxmax(m,1)=i;
                    
                else
                    
                    if m~=0
                        
                        if input1(i,1)>ymax(m,1) & m~=0 %replacingthe old crest location with new one if the new one is larger
                            
                            xmax(m,1)=t(i,1);
                            ymax(m,1)=input1(i,1);
                            positionxmax(m,1)=i;
                            
                        end
                        
                    end
                    
                end
                
            end
            
        end
        
    end
    
    %detecting trough
    if i>1 & i<len
        
        if input1(i,1)<input1(i-1,1) & input1(i,1)<input1(i+1,1)
            
            if input1(i,1)<0
                
                if n==m-1 % check if after last trough, the program detect the crest or not (n==m-1 mean it detected and the new y(i,1) is the trough in next wave)
                    
                    n=n+1;
                    xmin(n,1)=t(i,1);
                    ymin(n,1)=input1(i,1);
                    positionxmin(n,1)=i;
                    
                else
                    
                    if n~=0
                        
                        if input1(i,1)<ymin(n,1) %replacingthe old crest location with new one if the new one is smaller
                            
                            xmin(n,1)=t(i,1);
                            ymin(n,1)=input1(i,1);
                            positionxmin(n,1)=i;
                            
                        end
                        
                    end
                    
                end
                
            end
            
        end
        
    end
    
    
end

Eta=input1; %water surface level time series

%--------------------------------------------------------------------------
%calculating Wave height from original data

len1=length(xmax(:,1));
len2=length(xmin(:,1));

H=zeros(len1,1); %Pre-assigning array
for i=1:len1
    
    H(i,1)=ymax(i,1)-ymin(i,1); %wave height
    xmean(i,1)=(xmax(i,1)+xmin(i,1))/2;
    Etac(i,1)=ymax(i,1); %water level of the wave crest
    Etat(i,1)=ymin(i,1); %water level of the wave trough
    
end
        
%--------------------------------------------------------------------------
%calculating Wave period

T=zeros(length(H(:,1)),1); %Pre-assigning array
for i=1:length(H(:,1))
    for j=1:length(xupcross(:,1))-1
        
        if xupcross(j,1)<xmean(i,1) & xupcross(j+1,1)>xmean(i,1)
            T(i,1)=xupcross(j+1,1)-xupcross(j,1);
        end
        
    end
end

%--------------------------------------------------------------------------
%calculating wave parameters

Etarms=sqrt(sum(Eta.^2)/len);
[Hsort,HsortIndex]=sort(H,'descend');
HTop3rd=round(1/3*length(Hsort(:,1)));
Hs=mean(Hsort(1:HTop3rd,1)); % Zero-crossing significant wave height
Tsort=T(HsortIndex);
TTop3rd=round(1/3*length(Tsort(:,1)));
Ts=mean(Tsort(1:TTop3rd,1)); % Zero-crossing significant wave period
Hz=mean(H(:,1)); % Zero-crossing mean wave height
Tz=mean(T(:,1)); % Zero-crossing mean wave period

%--------------------------------------------------------------------------
%Displaying results

if strcmp(dispout,'on')==1
    
    val=[Hs Hz Tz Ts];
    name={'Hs','Hz','Tz','Ts'};
    for i=1:length(val)
        fprintf('%14s   %g\n',name{i},val(i));
    end
    
    plot(t,input1)
    hold on
    
    scatter(xmax,ymax,'*r')
    scatter(xmin,ymin,'r')
    
    scatter(xupcross,yupcross,'^k')
    
    for i=1:length(H(:,1))
        
        plot([xmean(i,1),xmean(i,1)],[(ymax(i,1)+ymin(i,1))/2-H(i,1)/2,(ymax(i,1)+ymin(i,1))/2+H(i,1)/2],':m')
        
    end
    
    xlim([t(1,1) t(end,1)])
    title('Water Level')
    xlabel('Time (s)')
    ylabel('\eta (m)')
    
    legend('Original Data Series','Crest','Trough','Up Crossing','Wave Height')
    
end

%--------------------------------------------------------------------------
