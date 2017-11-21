"""
NAME: UMER JAVAID
Class: BESE 5A
CMS: 111238

main function to run all
 
Enter choice in box to run desired problem
"""


import problem4,problem5,problem6,problem7,problem8
import cv2,numpy as np
#,problem5.py,problem6.py,problem7.py,problem8.py
def main():
    while(True):
        choice=int(raw_input("\n\n\nPlease Enter Problem Number (4-9) to execute   \nEnter 0 to Exit\n\n"))
        if(choice==4):
            image=cv2.imread("Einstein.PNG",0)
            problem4.contrast_stretching( image,10)

        elif(choice==5):
            problem5.correct()
            
        
        elif(choice==6):
            problem6.with_log_and_power()
                
        elif(choice==7):        
            problem7.get_total_circles("red")
            
        elif(choice==8):        
            problem8.selective_equalize() 
            
        elif(choice==0):
            break
    return
if __name__ == '__main__':
    main()
     

