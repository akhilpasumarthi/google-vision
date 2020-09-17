from google.cloud import vision
import io
import timeit
import time
import os
from googlesearch import *      
import timeit
import time
import webbrowser
def detect(num):
    start_time = time.time()
    list1=[]
    b=""
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key.json"
    client = vision.ImageAnnotatorClient()


    path = "test{}.png".format(num)
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    response = client.text_detection(image=image)

    for text in response.text_annotations:
        list1.append(text.description)
    
    print(list1)
    b=list1[0]
    
    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
    for url in search(b, tld="co.in", num=1, stop = 1, pause = 2):
        webbrowser.open("https://google.com/search?q=%s" % b)
    print("--- %s seconds ---" % (time.time() - start_time))
detect(0)
 