# to use your phone as a camera 
# step 1 - install ip webcam app from playstore
# step 2 - open app scroll down to start server click on that]
# step 3 - after starting the server write the ipvs address in the request get code of images with http://
# step 4 - run this code and you are good to go.


import requests
import numpy as np
import cv2

while True:
    images = requests.get("http://192.168.43.83:8080/shot.jpg")
    video = np.array(bytearray(images.content),dtype=np.uint8)
    render = cv2.imdecode(video, -1)
    cv2.imshow('frame', render)
    if (cv2.waitKey(1) and 0xFF == ord('q')):
        break


