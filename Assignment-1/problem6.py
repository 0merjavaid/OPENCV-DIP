"""
NAME: UMER JAVAID
Class: BESE 5A
CMS: 111238

Problem 5:
 
Brightness corrected  with log and power
"""

import cv2, numpy as np
def log_transform(image,c=1):    #formula implemented for log transformation
    image=image.astype(int)
    image=np.log(1+image)
    image=c*image
    
    image[image>255]=255          #Clipping
    image[image<0]=0 
    return image.astype("uint8")






def power_transform(image,power,c):   # Power formula implementation
    image=image.astype(int)
    image=np.power(image,power)
    image=c*image 
    image[image>255]=255            #Clipping
    image[image<0]=0
    return image.astype('uint8')

def with_log_and_power():
    im=cv2.imread("Child_1.png",0)
    im1=cv2.imread("Child_2.PNG",0)

    child1=power_transform(im,0.9,1)   #applying transforms
    child2=log_transform(im1,30)
    
    
    cv2.imshow("power",child1)
    cv2.imshow("log",child2)   #Showing
    
    
    cv2.imwrite("Child_1_corrected_with_power.png",child1) #writing
    cv2.imwrite("Child_2_corrected_with_log.png",child2)


    print "Images Enhanced and Written in directory"
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
