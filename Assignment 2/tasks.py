"""
Name Muhammad Umer Javaid
Bese 5a
111238


"""


from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np 
import os,glob
from collections import Counter 
blur_size =9  # Standard deviation in pixels.

# Convert to float so that negatives don't cause problems
def task1(): 
    for i,file in enumerate(glob.glob("A2_updated/Retinal_Images_Task_1/*.jpg")):  #READ ALL JPGS
        
        image =cv2.imread(file,0)
        kernel = np.ones((9,9),np.uint8)
        image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel).astype(float)  # opening

        blur=cv2.GaussianBlur(image.astype("uint8"),(499,499),0).astype(float)  #background estimation
        image_copy=image/255.0
        blurr=blur/255.0    #im to double
        result=image_copy-blurr
        
        result=(result*255).astype(int)
        
        b = Counter(result.ravel())
        max_value= b.most_common(1)[0][0]
        
         
        result[result>255]=255
        result[result<0]=0
        i=(result.astype(float)/255.0)+0.5 - float(max_value)/255     #formula
        name="A2_updated/output_Umer/Task1_outputs/"+file.split("/")[-1]
        plt.imsave(name,i,format="jpg",cmap="gray") 
        
        
        #cv2.imwrite(name,(result*255).astype("uint8"))
        print "File written  "+name
 


















#Task 2 Central line detection







def normalization(image,size):
    im=image.copy()       # Preprocessing
    kernel=np.ones((size,size),np.float32)/(size*size)
     
    im=cv2.blur(image.astype(float)/255,(size,size))
    
    im=image.astype(float)/255.0-im 
    """plt.imshow(image,cmap="gray")
    plt.show()
    plt.imshow(im,cmap="gray")
    plt.show()""" 
    
    
    return im


def thin_enhancement(image):   #enhancing thin edges by adding max result of 4 kernels
    
    
    zero=np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]],np.float32)/6
    fortyfive=np.array([[-1,-1,2],[-1,2,-1],[2,-1,-1]],np.float32)/6
    ninty=np.array([[-1,2,-1],[-1,2,-1],[-1,2,-1]],np.float32)/6
    one_thirty_five=np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]],np.float32)/6
    
    
    
    Z0=cv2.filter2D(image,-1,zero)
    F45=cv2.filter2D(image,-1,fortyfive)
    N90=cv2.filter2D(image,-1,ninty)
    O135=cv2.filter2D(image,-1,one_thirty_five)
     
    k=np.maximum(np.maximum(Z0,F45),np.maximum(N90,O135))   #max resutl
    
     
    #cv2.imshow("normalize",im)
    return image+k+k   #adding twice for betterrestlt

def DoOG(image): 
    zero=np.array([[-1,-2,0,2,1],
                    [-2,-4,0,4,2],
                    [-1,-2,0,2,1]])     # DoOG filters calculated by image rotation
    one_thirty_five=np.array(
    [[0,     0,     1,     0,     0,     0],
     [0,     2,     2,     2,     0,     0],
     [1,     2,     4,     0,    -2,     0],
     [0,     2,     0,    -4,    -2,    -1],
     [0,     0,    -2,    -2,    -2,     0],
     [0,     0,     0,    -1,     0,     0]])
        
        
    forty_five=np.array(
     [[0,     0,     0,     1,     0,     0],
     [0 ,    0 ,    2 ,    2,     2,     0],
     [0  ,  -2 ,    0    , 4   ,  2  ,   1],
     [-1  ,  -2  ,  -4  ,   0  ,   2    , 0],
     [0    ,-2  ,  -2 ,   -2 ,    0    , 0],
     [0 ,    0,    -1,     0,     0   ,  0 ]] )   
     
    ninty=np.array([
    [1,    2,     1],
    [2,     4,     2],
    [0,     0,     0],
    [-2,    -4,    -2],
    [-1,    -2,    -1],
       
   ])    
       
    im0=cv2.filter2D(image,-1,zero)
    im45=cv2.filter2D(image,-1,forty_five)
    im90=cv2.filter2D(image,-1,ninty)
    im135=cv2.filter2D(image,-1,one_thirty_five)
    #print im 
    
     
    return im0,im45,im90,im135



def central_line(image,angle): 
    test=np.zeros_like(image)
    for i in range(3,image.shape[0]-3):    #Applying all for cases to all 4 images and thresholding and saving
        for j in range(3,image.shape[1]-3):
            if angle==0:
                if(image[i,j]>0 and image[i,j+1]>0 and image[i,j+2]<0 and image[i,j+3]<0):
                    index= image[i,j:j+4].argmax()
                    value=np.max(np.abs(image[i,j+2:j+4]))+np.max(image[i,j:j+2])
                    test[i,j+index]=value
                elif(image[i,j]>0 and image[i,j+1]>0 and image[i,j+2]<0 ):
                    index= image[i,j:j+4].argmax()
                    value=np.max(np.abs(image[i,j:j+2]))+np.max(image[i,j:j+2])
                    test[i,j+index]=value
                elif(image[i,j+1]>0 and image[i,j+2]<0 and image[i,j+3]<0 ):
                    index= image[i,j:j+4].argmax()
                    value=np.max(np.abs(image[i,j+2:j+4]))+np.max(image[i,j:j+1])
                    test[i,j+index]=value
                elif(image[i,j]>0 and image[i,j+1]==0 and image[i,j+2]<0):
                    index= image[i,j:j+3].argmax()
                    value=np.max(np.abs(image[i,j]))+np.max(image[i,j+3])
                    test[i,j+index]=value
                    
                    
            elif angle==135:
                
                if(image[i,j]>0 and image[i+1,j+1]>0 and image[i+2,j+2]<0 and image[i+3,j+3]<0):
                    index= np.array([image[i,j],image[i+1,j+1]]).argmax()
                    value=max(np.abs(image[i+2,j+2]),np.abs(image[i+3,j+3]))+max(image[i,j],image[i+1,j+1])
                    test[i+index,j+index]=value
                elif(image[i,j]>0 and image[i+1,j+1]>0 and image[i+2,j+2]<0 ):
                    index= np.array([image[i,j],image[i+1,j+1],image[i+2,j+2],image[i+3,j+3]]).argmax()
                    value= max(image[i,j],image[i+2,j+2])+abs(image[i+2,j+2])
                     
                    test[i+index,j+index]=value 
                elif(image[i+1,j+1]>0 and image[i+2,j+2]<0 and image[i+3,j+3]<0 ):
                    index= np.array([image[i,j],image[i+1,j+1],image[i+2,j+2],image[i+3,j+3]]).argmax()
                    value= abs(min(image[i+2,j+2],image[i+3,j+3]))+image[i,j]
                     
                    test[i+index,j+index]=value
                elif(image[i,j]>0 and image[i+1,j+1]==0 and image[i+2,j+2]<0):
                    index= np.array([image[i,j],image[i+1,j+1],image[i+3,j+3]]).argmax()
                    value=max(np.abs(image[i+2,j+2]))+(image[i,j])
                    test[i+index,j+index]=value
                
            elif angle==90:
                if(image[i,j]>0 and image[i+1,j]>0 and image[i+2,j]<0 and image[i+3,j]<0):
                    index= image[i:i+4,j].argmax()
                    value=np.max(np.abs(image[i+2:i+4,j]))+np.max(image[i:i+2,j])
                    test[i+index,j]=value
                elif(image[i,j]>0 and image[i+1,j]>0 and image[i+2,j]<0 ):
                    index= image[i:i+4,j].argmax()
                    value=np.max(np.abs(image[i:i+2,j]))+np.max(image[i:i+2,j])
                    test[i+index,j]=value
                elif(image[i+1,j]>0 and image[i+2,j]<0 and image[i+3,j]<0 ):
                    index= image[i:i+4,j].argmax()
                    value=np.max(np.abs(image[i+2:i+4,j+2:j+4]))+np.max(image[i:i+1,j])
                    test[i+index,j]=value
                elif(image[i,j]>0 and image[i+1,j]==0 and image[i+2,j]<0):
                    index= image[i:i+3,j].argmax()
                    value=np.max(np.abs(image[i,j]))+np.max(image[i+3,j])
                    test[i+index,j]=value
                
                
            elif angle==45:
                if(image[i,j+3]>0 and image[i+1,j+2]>0 and image[i+2,j+1]<0 and image[i+3,j]<0):
                    index= np.array([image[i,j+3],image[i+1,j+2]]).argmax()
                    value=max(np.abs(image[i+2,j+1]),np.abs(image[i+3,j]))+max(image[i,j+3],image[i+1,j+2])
                    test[i+3-index,j+index]=value
                elif(image[i,j+3]>0 and image[i+1,j+2]>0 and image[i+2,j+1]<0 ):
                    index= np.array(image[i,j+3]>0 and image[i+1,j+2]>0 and image[i+2,j+1]<0 and image[i+3,j]<0).argmax()
                    value= max(image[i,j+3],image[i+1,j+2])+abs(image[i+2,j+1])
                     
                    test[i+3-index,j+index]=value 
                elif(image[i+1,j+2]>0 and image[i+2,j+1]<0 and image[i+3,j]<0 ):
                    index= np.array(image[i,j+3]>0 and image[i+1,j+2]>0 and image[i+2,j+1]<0 and image[i+3,j]<0).argmax()
                    value= abs(min(image[i+2,j+1],image[i+3,j]))+image[i+1,j+2]
                     
                    test[i+3-index,j+index]=value
                elif(image[i,j+3]>0 and image[i+1,j+2]==0 and image[i+2,j+1]<0):
                    index= np.array(image[i,j+3]>0 and image[i+1,j+2]>0 and image[i+2,j+1]<0 and image[i+3,j]<0).argmax()
                    value=max(np.abs(image[i+2,j+1]))+(image[i,j+3])
                    test[i+3-index,j+index]=value
                
    test[test<0.4]=0

    
    
    return test



        
def task2():   # Calling all processline
    for i,file in enumerate(glob.glob("A2_updated/Retinal_Images_Task_2/*.tif")):
        
        im=cv2.imread(file)[:,:,1]
        im=normalization(im,399) 
         
        im=thin_enhancement(im)  
        im0,im45,im90,im135=DoOG(im)
        c1=central_line(im0,0)
        c2=central_line(im45,45)
        c3=central_line(im90,90)
        c4=central_line(im135,135) 
        name="A2_updated/output_Umer/"+file.split("/")[-1]+"_zero.jpg"
        cv2.imwrite(name,c1*255)
        name="A2_updated/output_Umer/"+file.split("/")[-1]+"_45.jpg"
        cv2.imwrite(name,c2*255)
        name="A2_updated/output_Umer/"+file.split("/")[-1]+"_90.jpg"
        cv2.imwrite(name,c3*255)
        name="A2_updated/output_Umer/"+file.split("/")[-1]+"_135.jpg"
        cv2.imwrite(name,c4*255)
        print "File written"+ name
      
