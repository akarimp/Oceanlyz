def PcorFFTFun(input,fs,duration,nfft,h,heightfrombed,fminpcorr,fmaxpcorr,ftailcorrection,pressureattenuation,autofmaxpcorr,dispout):
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
    
    PcorFFTFun
    ==========

    .. code:: python

        Eta,ftailcorrection=PcorFFTFun(input,fs,duration,nfft,h,heightfrombed,fminpcorr,fmaxpcorr,ftailcorrection,pressureattenuation,autofmaxpcorr,dispout)

    DESCRIPTION
    -----------

    Apply pressure correction factor to water depth data from pressure gauge reading using FFT

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
    heightfrombed=0.0
                                    Sensor height from bed
    fminpcorr=0.15
                                    Minimum frequency that automated calculated fmaxpcorr can have if autofmaxpcorr='on' in (Hz)
    fmaxpcorr=0.8
                                    Maximum frequency for applying pressure attenuation factor
    ftailcorrection=1
                                    Frequency that diagnostic tail apply after that (typically set at 2.5fm, fm=1/Tm01)
    pressureattenuation='all'
                                    Define if to apply pressure attenuation factor or not 
                                        pressureattenuation='off': No pressure attenuation applied

                                        pressureattenuation='on': Pressure attenuation applied without correction after fmaxpcorr

                                        pressureattenuation='all': Pressure attenuation applied with constant correction after fmaxpcorr
    autofmaxpcorr='on'
                                    Define if to calculate fmaxpcorr and ftailcorrection based on water depth or not
                                        autofmaxpcorr='off': Off

                                        autofmaxpcorr='on': On
    dispout='on'
                                    Define to display outputs or not ('off': not display, 'on': display)

    OUTPUT
    ------

    Eta
                                    Corrected Water Surface Level Time Series (m)

    EXAMPLE
    -------

    .. code:: python

        Eta,ftailcorrection=PcorFFTFun(water_pressure/(1000*9.81),10,1024,256,1.07,0.05,0.15,0.8,1,'all','on','on')

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
    #--------------------------------------------------------------------------
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

    sample=fs*duration #number of sample in input file
    len_=sample
    # h=np.mean(input) #mean water depth in (m)
    # h[h<=0]=0.001
    dt=1/fs #calculating delta t in second (dt=duration/sample)
    t=np.linspace(dt,duration,sample) #time

    #--------------------------------------------------------------------------

    if (fmaxpcorr>fs/2) : fmaxpcorr=int(fs/2)
    #nfft = 2^(nextpow2(len_))
    f=np.linspace(0,fs,len_) #frequency
    w=2*np.pi*f #Angular frequency

    #calculating Fast Fourier transform
    FFTEta = np.fft.fft(input1,len_)
    #Syy=np.abs((2/fs)*FFTEta*np.conjugate(FFTEta)/len_)
    #Syy[f>fs/2]=0
    Syy=np.zeros(len_)
    f1,Syy_half=sp.signal.welch(input1,fs=fs,nfft=len_)
    Syy[0:len(Syy_half)]=Syy_half.copy()

    #Estimation of wave number (k) from Hunt (1979)
    #k0=w**2/9.81 #Deep water wave number
    #k0h=k0*h
    #kh=k0h*(1+k0h**1.09*np.exp(-(1.55+1.3*k0h+0.216*k0h**2)))/np.sqrt(np.tanh(k0h)) #Calculating wave number from Beji (2013)
    #kini=kh/h #initial value for k (Wave number from Beji (2013))
    #kini[w==0]=0

    #Estimation of wave number (k) from Goad (2010)
    k0=w**2/9.81 #Deep water wave number
    k0h=k0*h
    kh=np.zeros(len(k0h))
    kh[k0h>=1]=k0h[k0h>=1]
    kh[k0h<1]=(k0h[k0h<1])**0.5
    for i in range(0,3,1):
        kh=kh-((kh-k0h*(np.tanh(kh))**-1)/(1+k0h*((np.tanh(kh))**(-2)-1))) #Calculating wave number from Goda (2010)
    
    k=kh/h #Calculating wave number from Goda (2010)
    k[w==0]=0

    #Calculation exact of wave number (k)
    #for i in range(0,len_,1):
    #    fun = @(x)(w(i,1)^2-(9.81*x*tanh(x*h)))
    #    k[i]=fzero(fun,kini(i,1))

    #Calculation of pressure response factor
    Kp=np.cosh(k*heightfrombed)/np.cosh(k*h)
    kmaxL=np.pi/(h-heightfrombed) # Wave number associated with fmaxpcorrL
    KpminL=np.cosh(kmaxL*heightfrombed)/np.cosh(kmaxL*h) # Minimum Limit for K_p calculated based on linear wave theory
    Kp[Kp < KpminL] = KpminL # Check to avoid large amplification, Kp should be larger than minimum K_p calculated based on linear wave theory

    #automatically estimating fmaxpcorr and ftailcorrection
    if autofmaxpcorr=='on':
        locfminpcorr=int(np.max((np.nonzero(f<=fminpcorr))[0])) #Locating the location of fminpcorr (fmaxpcorr should be larger than fminpcorr)
        locSyymax=np.argmax(Syy[locfminpcorr:]) # Locating the peak frequency, fp, of original dataset
        fmaxpcorrL=1/(2*np.pi)*np.sqrt(9.81*kmaxL*np.tanh(kmaxL*h)) # Maximum frequency that K_p can be applied, calculated from linear wave theory
        locfmaxpcorrL=int(np.max((np.nonzero(f<=fmaxpcorrL))[0])) #Location the location of fmaxpcorr1
        if (locfmaxpcorrL<locfminpcorr+(locSyymax)): locfmaxpcorrL=locfminpcorr+(locSyymax) #Check if locfmaxpcorrL locataed after fp
        Syy1=Syy/(Kp**2)
        locSyymin=np.argmin(Syy1[locfminpcorr+(locSyymax):locfmaxpcorrL+1]) #Locating the location of minimum value for Syy between fp and fmaxpcorr1
        fmaxpcorr1=f[locfminpcorr+(locSyymax)+(locSyymin)] #Asigning the frequency of the location of minimum value for Syy between fp and fmaxpcorr1
        ftailcorrection1=f[locfminpcorr+(locSyymax)+(locSyymin)]
        if (fmaxpcorr1>fmaxpcorrL): fmaxpcorr1=fmaxpcorrL #Check fmaxpcorr1 be smaller than fmaxpcorrL
        if ((fmaxpcorr1==f[locfminpcorr+(locSyymax)]) and (fmaxpcorrL>f[locfminpcorr+(locSyymax)])): fmaxpcorr1=fmaxpcorrL #if fmaxpcorrL>fp then fmaxpcorr1 should not be equal to fp
        if (ftailcorrection1>fmaxpcorrL): ftailcorrection1=fmaxpcorrL
        if (fmaxpcorr>fmaxpcorr1): fmaxpcorr=fmaxpcorr1
        if (ftailcorrection>ftailcorrection1): ftailcorrection=ftailcorrection1


    if pressureattenuation=='off':
        Kp[0:]=1

    elif pressureattenuation=='on':

        Kp[f>fmaxpcorr]=1 # correction factor larger than fmaxpcorr should be 1 (no correction)

        # linear decrease of correction for f larger than maximum frequency
        loc1=int(np.max((np.nonzero(f<=fmaxpcorr-0.05))[0]))
        loc2=int(np.max((np.nonzero(f<=fmaxpcorr+0.05))[0]))
        if (loc2>len(f)): loc2=len(f)
        for i in range(loc1,loc2+1,1):
            Kp[i]=(Kp[loc2]-Kp[loc1])/(loc2-loc1)*(i-loc1)+Kp[loc1]


    elif pressureattenuation=='all':
        loc2=int(np.max((np.nonzero(f<=fmaxpcorr))[0]))
        if (loc2>len(f)): loc2=len(f)
        Kp[f>fmaxpcorr]=Kp[loc2] # correction factor larger than fmaxpcorr stays constant


    Kp1=Kp[0:int(len_/2)]
    Kp1=np.flipud(Kp1)
    Kp[int(len_/2):]=Kp1 #make Kp symetric around fr/2

    #correcting pressure
    FFTEtacor= FFTEta/Kp			    # applies corection factor
    Eta = np.real(np.fft.ifft(FFTEtacor,len_))	# corected water surface levels time series

    #--------------------------------------------------------------------------
    #Displaying results

    if dispout=='on':
        plt.plot(t,input1,label='Original Water Level')
        plt.plot(t,Eta,'r',label='Corrected Water Level')
        plt.xlim(t[0], t[-1])
        plt.title('Water Level')
        plt.xlabel('Time(s)')
        plt.ylabel('\eta(m)')
        plt.legend()


    #--------------------------------------------------------------------------
    #Outputs
    return Eta, ftailcorrection

    #--------------------------------------------------------------------------
