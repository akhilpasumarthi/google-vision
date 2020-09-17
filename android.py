import urllib3
import urllib.request
import requests
import cv2
import numpy as np
import pytesseract 
from googlesearch import *      
import timeit
import time
import webbrowser
from PIL import Image 

from vision import detect

start_time = time.time()


# adds image processing

# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.1.6:8080/shot.jpg'
img_counter = 0
while True:

    imgResp=urllib.request.urlopen(url)
   
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)

    # put the image on screen
    
    img = cv2.resize(img, (540, 540)) 
    cv2.imshow('IPWebcam',img)
    
    #To give the processor some less stress
    #time.sleep(0.1) 

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "test{}.png".format(img_counter)
        cv2.imwrite(img_name, img)
        print("{} written!".format(img_name))
        detect(img_counter)
        img_counter += 1

cv2.destroyAllWindows()
