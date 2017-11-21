"""
NAME: UMER JAVAID
Class: BESE 5A
CMS: 111238



USAGE:
1)Run script and image will appear
2) click and drag area that you want to equilize
3) it will draw a box just to let you know area you selected( added intentionlly )
4) Press 'z' to quit
"""

import time,cv2,numpy as np   #imports
refPt = np.array(())  #To store points top left and right bottom

image=None
def click_and_crop(event, x, y, flags, param):    #This method is used to crop area to apply equaliaztion
	# grab references to the global variables
	global refPt,image
    
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
 
	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
 
		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", image)

def hist(image):
    return cv2.equalizeHist(image)#return equalized portion
    

def selective_equalize():  
    print "Click and Drag to Equalize\nPress z to quit\n"  
    global refPt,image
    image=cv2.imread('Child.PNG',0) #Read image 
    clone = image.copy()
    cv2.namedWindow("image")
    cv2.moveWindow("image", 750,20);
    cv2.setMouseCallback("image", click_and_crop)#Call mouse handle function and wait for user
    done=True
    while True:

                # display the image and wait for a keypress
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF


        # if the 'c' key is pressed, break from the loop
        if key == ord("z"):

            break
        elif(len(refPt)%2==0 and len(refPt)!=0  ):  #if 2 points selected 



            refPt=np.array(refPt)
 
            top_left= np.sort(refPt[:,1])   #REtrieve points
            bottom_right= np.sort(refPt[:,0])
             
            crop=clone[top_left[0]:top_left[1], bottom_right[0]:bottom_right[1]]   #Crop that area
            crop=hist(crop) #Apply histogram eq
            image[top_left[0]:top_left[1], bottom_right[0]:bottom_right[1]]=crop   #merge to original image
             
            refPt=[]

    cv2.destroyAllWindows()
    
    

 
