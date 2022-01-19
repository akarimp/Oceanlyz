def SeaSwellFun(input,fs,duration,nfft,h,fmin,fmax,ftailcorrection,tailpower,fminswell,fmaxswell,mincutoff,maxcutoff,tailcorrection,dispout):
    """
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
    
    SeaSwellFun
    ===========

    .. code:: python

        Hm0,Hm0sea,Hm0swell,Tp,Tpsea,Tpswell,fp,fseparation,f,Syy=SeaSwellFun(input,fs,duration,nfft,h,fmin,fmax,ftailcorrection,tailpower,fminswell,fmaxswell,mincutoff,maxcutoff,tailcorrection,dispout)

    DESCRIPTION
    -----------

    Separate sea wave from swell wave

    INPUT
    -----

    input=importdata('h.mat')
                                    Load water depth (h)/surface elevation (Eta) data and rename it "input" in (m)
    fs=10
                                    Sampling frequency that data collected at in (Hz)
    duration=1024
                                    Duration time that data collected in input in each burst in second
    nfft=2^10
                                    NFFT for Fast Fourier Transform
    h=1
                                    Mean water depth in (m)
    fmin=0.04
                                    Minimum frequency for cut off the lower part of spectra
    fmax=1
                                    Maximum frequency for cut off the upper part of spectra
    ftailcorrection=1
                                    Frequency that diagnostic tail apply after that (typically set at 2.5fm, fm=1/Tm01)
    tailpower=-5
                                    Power that diagnostic tail apply based on that (-3 for shallow water to -5 for deep water)
    fminswell=0.1
                                    Minimum frequency that is used for Tpswell calculation
    fmaxswell=0.25
                                    Maximum frequency that swell can have, It is about 0.2 in Gulf of Mexico
    mincutoff='off'
                                    Define if to cut off the spectra below fmin
                                        mincutoff='off': Cutoff off

                                        mincutoff='on': Cutoff on
    maxcutoff='off'
                                    Define if to cut off the spectra beyond fmax
                                        maxcutoff='off': Cutoff off

                                        maxcutoff='on': Cutoff on
    tailcorrection='off'
                                    Define if to apply diagnostic tail correction or not 
                                        tailcorrection='off': Not apply

                                        tailcorrection='jonswap': JONSWAP Spectrum tail

                                        tailcorrection='tma': TMA Spectrum tail
    dispout='on'
                                    Define to display outputs or not ('off': not display, 'on': display)

    OUTPUT
    ------

    Hm0
                                    Zero-Moment Wave Height (m)
    Hm0sea
                                    Sea Zero-Moment Wave Height (m)
    Hm0swell
                                    Swell Zero-Moment Wave Height (m)
    Tp
                                    Peak wave period (second)
    Tpsea
                                    Peak Sea period (second)
    Tpswell
                                    Peak Swell Period (second)
    fp
                                    Peak Wave Frequency (Hz)
    f
                                    Frequency (Hz)
    fseparation
                                    Sea and Swell Separation Frequency (Hz)
    Syy
                                    Wave Surface Elevation Power Spectrum (m^2s)

    EXAMPLE
    -------

    .. code:: python

        Hm0,Hm0sea,Hm0swell,Tp,Tpsea,Tpswell,fp,fseparation,f,Syy=SeaSwellFun(water_pressure/(1000*9.81),10,1024,256,1.07,0.05,5,1,-5,0.1,0.25,'on','on','off','on')

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
    """

    #==========================================================================

    #CODE
    #Import required packages

    import numpy as np
    import scipy as sp
    from scipy import signal
    if dispout=='on':
        import matplotlib.pyplot as plt 

    #--------------------------------------------------------------------------
    #Convert inputs to numpy array

    #Changing type to numpy array
    def type2numpy(variable):
        if type(variable) is not str:
            if np.size(variable)==1:
                if ((type(variable) is list) or (type(variable) is np.ndarray)):
                    variable=np.array(variable)
                else:
                    variable=np.array([variable])
            elif np.size(variable)>1:
                if (type(variable).__module__)!='numpy':
                    variable=np.array(variable) 
        return variable
    
    input=type2numpy(input)

    #--------------------------------------------------------------------------
    #deterending

    input1=sp.signal.detrend(input,type='linear')

    #--------------------------------------------------------------------------
    #calculating Fast Fourier transform and power density

    if (fmax>fs/2): fmax=int(fs/2)
    #nfft = 2^(nextpow2(length(input1)))

    #--------------------------------------------------------------------------
    #calculating power density 

    windowelem = 256 # number of elements in each window
    overlapelem = 128 #number of overlap element

    f,Syy=sp.signal.welch(input1,fs=fs,nfft=nfft) #Wave power spectrum and Frequency

    w=2*np.pi*f #angular velocity
    deltaf=f[1]-f[0]

    #--------------------------------------------------------------------------
    #Applying tail correction

    #Index of ftailcorrection
    if tailcorrection=='jonswap' or tailcorrection=='tma':
        Indxftail=int(np.min((np.nonzero(f>=ftailcorrection))[0]))

    #Applying diagnostic frequency tail based on JONSWAP after fmax
    if tailcorrection=='jonswap':
        
        Syy[f>ftailcorrection]=Syy[Indxftail]*(f[f>ftailcorrection]/ftailcorrection)**tailpower #Adding diagnostic tail
        Syy[Syy<0]=0 #Syy can not be negative

    #Applying diagnostic frequency tail based on TMA after fmax
    elif tailcorrection=='tma':
        
        omega=2*np.pi*f*np.sqrt(h/9.81)

        #Transformation function from JONSWAP into TMA, approximated method
        PHI=np.ones(len(omega))
        PHI[omega<=1]=omega[omega<=1]**2/2
        PHI[((omega>1) & (omega<2))]=1-0.5*(2-omega[((omega>1) & (omega<2))])**2
        PHI[omega>=2]=1

        Syy[f>ftailcorrection]=Syy[Indxftail]*(PHI[f>ftailcorrection]/PHI[Indxftail])*(f[f>ftailcorrection]/ftailcorrection)**tailpower #Adding TMA Spectrum tail
        Syy[Syy<0]=0 #Syy can not be negative


    #--------------------------------------------------------------------------
    #cut off spectra based on fmin and fmax 

    if mincutoff=='on':
        Syy[f<fmin]=0


    if maxcutoff=='on':
        Syy[f>fmax]=0


    #--------------------------------------------------------------------------
    #calculating 1D separation frequency of sea from swell (Hwang, 2012)
    #Hwang, P. A., Francisco J. O. T., H?ctor G. N., 2012, Wind sea and swell separation of 1d wave spectrum by a spectrum integration method, J. Atmos. Oceanic Technol., 29, 116?128.

    fup=f[f<=0.5]
    fstar=np.zeros(len(fup))
    m1fstar=np.zeros(len(fup))
    mminus1fstar=np.zeros(len(fup))
    for i1 in range(0,len(fup),1):
        fstar[i1]=fup[i1]
        m1fstar[i1]=np.sum(Syy[i1:len(fup)]*f[i1:len(fup)]**1*deltaf)
        mminus1fstar[i1]=np.sum(Syy[i1:len(fup)]*f[i1:len(fup)]**(-1)*deltaf)


    alfafstar=(m1fstar)/np.sqrt(mminus1fstar)

    loc1=np.nanargmax(alfafstar)
    fm=fstar[loc1]
    fseparation=24.2084*fm**3-9.2021*fm**2+1.8906*fm-0.04286

    if ((fseparation>fmaxswell) or (np.isinf(fseparation)==1) or (np.isnan(fseparation)==1) or (fseparation==0)): fseparation=fmaxswell #fseperation is about 0.2 in Gulf of Mexico
        
    #calculate the exact location of separation frequency
    loc2=len((np.nonzero(f<=fseparation))[0])-1 #location of fseperation
    fpsea1=(np.sum(Syy[loc2:]**5*f[loc2:]**1*deltaf))/(np.sum(Syy[loc2:]**5*f[loc2:]**0*deltaf)) #sea peak frequency based on fseparation from previous step
    fpswell1=(np.sum(Syy[0:loc2+1]**5*f[0:loc2+1]**1*deltaf))/(np.sum(Syy[0:loc2+1]**5*f[0:loc2+1]**0*deltaf)) #swell peak frequency based on fseparation from previous step
    loc7=np.argmin(Syy[((f<fpsea1) & (f>fpswell1))])
    loc8=len((np.nonzero(f<=fpswell1))[0])-1
    fseparation=f[loc7+loc8+1]
    if ((fseparation>fmaxswell) | (np.isinf(fseparation)==1) | (np.isnan(fseparation)==1) | (fseparation==0)): fseparation=fmaxswell #fseperation is about 0.2 in Gulf of Mexico
    #if (len(fseparation)==0): fseparation=fmaxswell #fseperation is about 0.2 in Gulf of Mexico

    #--------------------------------------------------------------------------

    #Calculating spectral moments

    m0=np.sum(Syy*f**0*deltaf)

    # calculating wave properties
    Hm0=4*np.sqrt(m0) #Zero-Moment wave height

    # calculation peak period
    loc6=np.argmax(Syy)
    Tp=1/f[loc6] #peak period

    # calculating peak frequency from weighted integral (Young, 1995)
    fp=(np.sum(Syy**5*f**1*deltaf))/(np.sum(Syy**5*f**0*deltaf)) #peak frequency

    #--------------------------------------------------------------------------
    #calculating swell and sea

    loc2=len((np.nonzero(f<=fseparation))[0])-1 #location of fseperation
    m0swell=np.sum(Syy[0:loc2+1]*f[0:loc2+1]**0*deltaf)
    m0sea=np.sum(Syy[loc2+1:]*f[loc2+1:]**0*deltaf) #Zero-Moment wave height
    Hm0sea=4*np.sqrt(m0sea) #sea Zero-Moment wave height
    Hm0swell=4*np.sqrt(m0swell) #swell Zero-Moment wave height
    loc3=np.argmax(Syy[loc2:])
    Tpsea=1/(f[loc2+loc3]) #sea peak period, loc4+loc5-1 is the location of sea peak
    loc4=len((np.nonzero(f<=fminswell))[0])-1 #location of fminswell
    if loc4>=loc2:
        loc4=1

    loc5=np.argmax(Syy[loc4:loc2+1])
    Tpswell=1/(f[loc4+loc5]) #swell peak period, loc4+loc5-1 is the location of swell peak
    fpsea=(np.sum(Syy[loc2:]**5*f[loc2:]**1*deltaf))/(np.sum(Syy[loc2:]**5*f[loc2:]**0*deltaf)) #sea peak frequency based on fseparation from previous step
    fpswell=(np.sum(Syy[0:loc2+1]**5*f[0:loc2+1]**1*deltaf))/(np.sum(Syy[0:loc2+1]**5*f[0:loc2+1]**0*deltaf)) #swell peak frequency based on fseparation from previous step

    #--------------------------------------------------------------------------
    #Displaying results

    if dispout=='on':
        
        val=[Hm0, Hm0sea, Hm0swell, Tp, Tpsea, Tpswell, fp, fseparation]
        name=['Hm0','Hm0-sea','Hm0-swell','Tp','Tp-sea','Tp-swell','fp','fseparation']
        for i in range(0,len(val)):
            #print ('\n',name[i],val[i],sep='     ',end='')
            print('{0:10}= {1:0.10f}'.format(name[i],val[i])) 
        
        #plotting
        plt.loglog(f[f!=0],Syy[f!=0])
        plt.loglog([fseparation,fseparation],[np.min(Syy[Syy!=0]),np.max(Syy)],'m-.')
        
        plt.title('Power Spectral Density')
        plt.xlabel('Frequency(Hz)')
        plt.ylabel('Spectral Density(m^2s)')
        

    #--------------------------------------------------------------------------
    #Outputs
    return Hm0,Hm0sea,Hm0swell,Tp,Tpsea,Tpswell,fp,fseparation,f,Syy

    #--------------------------------------------------------------------------
