"""
NAME: UMER JAVAID
Class: BESE 5A
CMS: 111238



Stretches contrast using Method 1 from lab manual
"""


import numpy as np,cv2
import matplotlib.pyplot as plt
def contrast_stretching(image,clip):  #input image and clipping percentile
    clip_right=clip
    clip_left=100-clip
   
    hist=cv2.calcHist([image],[0],None,[256],[0,256])  # Calculate histogram to get value of c and d
 
    x=np.arange(256)    # for plotting
    tem=np.zeros_like(hist) 
    a=tem[0]=0
    b=255
    plt.plot(x,hist)
    plt.show()
    
    total=np.sum(hist)
    for i in range(1,len(hist)):
        tem[i]=(np.sum(hist[0:i])/total)*100    #getting cummulative histogram
    c = (np.abs(tem-clip_right)).argmin()       #getting index to 5percenile and 95
    d = (np.abs(tem-clip_left)).argmin()
     
    image=image.astype(int)  
    out=((image-c)*((b-a)/((d-c))))+a    # Applying formula
    out[out<0]=0
    out[out>255]=255
    out=out.astype("uint8")
    his=cv2.calcHist([out],[0],None,[256],[0,256])
    x=np.arange(256)

    plt.plot(x,his)
    plt.show()
                                                          # Showing output stretched contrast
    plt.imshow(image,cmap="gray")
    plt.show()
    plt.imshow(out,cmap="gray")
    plt.show()
    
    
    print "done"    

