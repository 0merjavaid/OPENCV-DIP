"""
NAME: UMER JAVAID
Class: BESE 5A
CMS: 111238

Problem 5:
 
Brightness corrected  
"""
import cv2,numpy as np

def brightness(image,percentage,b_or_d):
    im=image.copy().astype(float)
    image=image.astype(float)
     
    im*=percentage
    
    if(b_or_d=="bright"):
        image+=im
        image[image>255]=255
    elif(b_or_d=="dark"): 
        image-=im
        
        image[image<0]=0 
    return image.astype("uint8")


def correct():
    Child1=cv2.imread("Child_1.png",0)
    Child1=brightness(Child1,0.5,'dark')
    
    Child2=cv2.imread("Child_2.PNG",0)
    Child2=brightness(Child2,0.8,'bright') 
    cv2.imshow("Made Dark 50%",Child1)
    cv2.imshow("Made bright 80%",Child2)
    
    
     
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    cv2.imwrite("Child_1_corrected.png",Child1)
    cv2.imwrite("Child_2_corrected.png",Child2)
 
