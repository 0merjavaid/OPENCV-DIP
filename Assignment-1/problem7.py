"""
NAME: UMER JAVAID
Class: BESE 5A
CMS: 111238


How it works:

program looks for desired color example red blue or yellow using numpy slicing and Set all other as white.
then using connected component it returns the number of fore ground objects
in the end it calculated percentage of circles in image i.e   pixels_of_circle/total_pixels
"""




import cv2,numpy as np
import matplotlib.pyplot as plt

def threshold(image,color):
    if(color=="red"):
        image[(image[:,:,2]<=120) ]=[255,255,255]   #Select non red and set them to white
        image[(image[:,:,1]>=120) ]=[255,255,255]   #select remaining yellow and set them to background result is just red
    
    elif(color=="blue"):  #Selects non blue and set them to white
        image[(image[:,:,0]<=120)]=[255,255,255]
    
    elif(color=="yellow"):#select non yellow and set them white
        image[(image[:,:,1]<=120)]=[255,255,255]
    
    else:
        print "color not found,\n Red or Yellow or Blue"
    return image



def counter_and_area(img):
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #convert color to gray
    _,thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) #thresholding
    thresh=255-thresh
    
    circle=np.count_nonzero(thresh)   #counting total non background pix
    total= thresh.shape[0]*thresh.shape[1]  #total pixels

    percentage=str(float(circle*100)/total)+"%"   #Percentage formula
    connectivity = 4  
    # Perform the operation
    output = cv2.connectedComponentsWithStats(thresh, connectivity, cv2.CV_32S) #getting results of conn componenets
    # Get the results
    # The first cell is the number of labels
    num_labels = output[0]-1
    return num_labels,percentage

def get_total_circles(color):  #it takes input color and gives result of pipeline
    
    img=cv2.imread("blobs.png")
    blobs=None
    if color=="blue":    #Do operations on blue blobs
        blobs=threshold(img.copy(),"blue")
        num_labels,percentage=counter_and_area(blobs)
        print "Area covered by Blue is:",percentage," \nTotal Blue circles are :",num_labels
        plt.imshow(cv2.cvtColor(blobs, cv2.COLOR_BGR2RGB))
        plt.show()
    
    
    elif(color=="yellow"):
        blobs=threshold(img.copy(),"yellow")
        num_labels,percentage=counter_and_area(blobs)   #Do ops on yellow
        print "Area covered by Yellow is:",percentage," \nTotal Yellow circles are :",num_labels
        plt.imshow(cv2.cvtColor(blobs, cv2.COLOR_BGR2RGB))
        plt.show()
        
        
    elif(color=="red"):    
        blobs=threshold(img.copy(),"red")
        num_labels,percentage=counter_and_area(blobs)
        print "Area covered by Red is:",percentage," \nTotal Red circles are :",num_labels
        plt.imshow(cv2.cvtColor(blobs, cv2.COLOR_BGR2RGB))
        plt.show()

        

    
