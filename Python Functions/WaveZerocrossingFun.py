def WaveZerocrossingFun(input,fs,duration,dispout):
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
    
    WaveZerocrossingFun
    ===================

    .. code:: python

        Hs,Hz,Tz,Ts,H,T=WaveZerocrossingFun(input,fs,duration,dispout)

    DESCRIPTION
    -----------

    Calculate wave properties using Up-going zero crossing method

    INPUT
    -----

    input=importdata('h.mat')
                                    Load water depth (h)/surface elevation (Eta) data and rename it "input" in (m)
    fs=10
                                    Sampling frequency that data collected at in (Hz)
    duration=1024
                                    Duration time that data collected in input in each burst in second
    dispout='on'
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

    .. code:: python

        Hs,Hz,Tz,Ts,H,T=WaveZerocrossingFun(water_pressure/(1000*9.81),10,1024,'on')

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

    sample=duration*fs #number of sample in input file
    dt=1/fs #calculating delta t in second (dt=duration/sample)
    t=np.linspace(dt,duration,sample) #time
    len_=len(t)
    input1=sp.signal.detrend(input,type='linear')

    #--------------------------------------------------------------------------
    # detecting the start point of first wave (fisr complete crest-trough)

    if ((input1[0]==0) and (input1[1]>0)):
        len3=1


    if (((input1[0]==0) and (input1[1]<0)) or (input1[0]!=0)):
        for i in range(0,len_-1,1):
            if ((input1[i]<0) and (input1[i+1]>0)):
                len3=i
                break


    # detecting the end point of last wave (fisr complete crest-trough)

    if ((input1[-1]==0) and (input1[-2]<0)):
        len4=len_


    if (((input1[-1]==0) and (input1[-2]>0)) or (input1[-1]!=0)):
        for i in range(len_-2,0,-1):
            if ((input1[i]<0) and (input1[i+1]>0)):
                len4=i
                break


    #--------------------------------------------------------------------------
    # detecting zero crossing points from original data

    m=-1
    n=-1

    xupcross=np.array([])
    yupcross=np.array([])
    positionxupcross=np.array([])
    
    xdowncross=np.array([])
    ydowncross=np.array([])
    positionxdowncross=np.array([])

    for i in range(len3,len4,1):

        #detecting up-crossing zero-crossing points
        if i==1:
            m=m+1
            xupcross=np.append(xupcross,dt)
            yupcross=np.append(yupcross,0)
            positionxupcross=np.append(positionxupcross,i)

        if ((i>1) and (i<len_)):
            if ((input1[i]<0) and (input1[i+1]>0)):
                m=m+1
                xupcross=np.append(xupcross,t[i]-(t[i+1]-t[i])/(input1[i+1]-input1[i])*input1[i])
                yupcross=np.append(yupcross,0)
                positionxupcross=np.append(positionxupcross,i)

        if i==len_:
            m=m+1
            xupcross=np.append(xupcross,t[-1])
            yupcross=np.append(yupcross,0)
            positionxupcross=np.append(positionxupcross,i)

        #detecting down-crossing zero-crossing points
        if ((i>1) and (i<len_)):
            if ((input1[i]>0) and (input1[i+1]<0)):
                n=n+1
                xdowncross=np.append(xdowncross,t[i]-(t[i+1]-t[i])/(input1[i+1]-input1[i])*input1[i])
                ydowncross=np.append(ydowncross,0)
                positionxdowncross=np.append(positionxdowncross,i)
                if positionxdowncross[n]>=len_:
                    positionxdowncross[n]=len_-1

    #Converting to int
    positionxupcross=np.int64(positionxupcross)
    positionxdowncross=np.int64(positionxdowncross)

    #--------------------------------------------------------------------------
    # detecting crest and trough from original data

    m=-1
    n=-1

    xmax=np.array([])
    ymax=np.array([])
    positionxmax=np.array([])
    
    xmin=np.array([])
    ymin=np.array([])
    positionxmin=np.array([])

    for i in range(positionxupcross[0],positionxupcross[-1]+1,1):

        # detecting crest
        if ((i>1) and (i<len_)):

            if ((input1[i]>input1[i-1]) and (input1[i]>input1[i+1])):

                if input1[i]>0:

                    if m==n: # check if after last crest, the program detect the trough or not (m==n mean it detected and the new y(i,1) is the crest in next wave)

                        m=m+1
                        xmax=np.append(xmax,t[i])
                        ymax=np.append(ymax,input1[i])
                        positionxmax=np.append(positionxmax,i)

                    else:

                        if m!=-1:

                            if ((input1[i]>ymax[m]) and (m!=-1)): #replacing the old crest location with new one if the new one is larger

                                xmax[m]=t[i]
                                ymax[m]=input1[i]
                                positionxmax[m]=i


        #detecting trough
        if ((i>1) and (i<len_)):

            if ((input1[i]<input1[i-1]) and (input1[i]<input1[i+1])):

                if input1[i]<0:

                    if n==m-1: # check if after last trough, the program detect the crest or not (n==m-1 mean it detected and the new y(i,1) is the trough in next wave)

                        n=n+1
                        xmin=np.append(xmin,t[i])
                        ymin=np.append(ymin,input1[i])
                        positionxmin=np.append(positionxmin,i)

                    else:

                        if n!=-1:

                            if input1[i]<ymin[n]: #replacing the old crest location with new one if the new one is smaller

                                xmin[n]=t[i]
                                ymin[n]=input1[i]
                                positionxmin[n]=i


    Eta=input1.copy() #water surface level time series

    #Converting to int
    positionxmax=np.int64(positionxmax)
    positionxmin=np.int64(positionxmin)

    #--------------------------------------------------------------------------
    #calculating Wave height from original data

    len1=len(xmax)
    len2=len(xmin)

    H=np.zeros(len1) #Pre-assigning array
    xmean=np.zeros(len1)
    Etac=np.zeros(len1)
    Etat=np.zeros(len1)

    for i in range (0,len1,1):

        H[i]=ymax[i]-ymin[i] #wave height
        xmean[i]=(xmax[i]+xmin[i])/2
        Etac[i]=ymax[i] #water level of the wave crest
        Etat[i]=ymin[i] #water level of the wave trough


    #--------------------------------------------------------------------------
    #calculating Wave period

    T=np.zeros(len(H)) #Pre-assigning array
    for i in range (0,len(H),1):
        for j in range (0,len(xupcross)-1,1):

            if ((xupcross[j]<xmean[i]) and (xupcross[j+1]>xmean[i])):
                T[i]=xupcross[j+1]-xupcross[j]


    #--------------------------------------------------------------------------
    #calculating wave parameters

    Etarms=np.sqrt(np.sum(Eta**2)/len_)
    Hsort=np.sort(H)[::-1]
    HsortIndex=np.argsort(H)[::-1]
    HTop3rd=int(1/3*len(Hsort))
    Hs=np.mean(Hsort[0:HTop3rd+1]) # Zero-crossing significant wave height
    Tsort=T[HsortIndex]
    TTop3rd=int(1/3*len(Tsort))
    Ts=np.mean(Tsort[0:TTop3rd+1]) # Zero-crossing significant wave period
    Hz=np.mean(H) # Zero-crossing mean wave height
    Tz=np.mean(T) # Zero-crossing mean wave period

    #--------------------------------------------------------------------------
    #Displaying results

    if dispout=='on':
        
        val=[Hs, Hz, Tz, Ts]
        name=['Hs','Hz','Tz','Ts']
        for i in range(0,len(val)):
            #print ('\n',name[i],val[i],sep='     ',end='')
            print('{0:10}= {1:0.10f}'.format(name[i],val[i])) 
        
        plt.plot(t,input1, label='Original Data Series')
        
        #plt.scatter(xmax,ymax,marker='*',c='r')
        plt.scatter(xmax,ymax,marker='*',c='r',label='Crest')
        plt.scatter(xmin,ymin,c='r',label='Trough')
        
        plt.scatter(xupcross,yupcross,marker='^',c='k',label='Up Crossing')
        
        for i in range(0,len(H),1):
            
            plt.plot([xmean[i],xmean[i]],[(ymax[i]+ymin[i])/2-H[i]/2,(ymax[i]+ymin[i])/2+H[i]/2],':m')
            
        
        plt.xlim(t[0], t[-1])
        plt.title('Water Level')
        plt.xlabel('Time (s)')
        plt.ylabel('\eta (m)')
        
        plt.legend()
        

    #--------------------------------------------------------------------------
    #Outputs
    return Hs,Hz,Tz,Ts,H,T

    #--------------------------------------------------------------------------
