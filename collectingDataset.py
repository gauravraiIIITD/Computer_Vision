import cv2
import time as t
# Camera 0 is the integrated web cam on my netbook
camera_port = 0

#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30

# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)

import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im
p = 0
_, frame = camera.read()
frame = cv2.flip(frame,1)
cv2.imshow("Frame", frame)
name=input("Enter your Name")
createFolder(name)
while True:


# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
    #for i in xrange(ramp_frames):
    temp = get_image()
    print("Taking image...",p)
# Take the actual image we want to keep
    camera_capture = get_image()
    file = name+"/your_image"+str(p)+".png"
# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!
    cv2.imwrite(file, camera_capture)
    p+=1
    t.sleep(1)
    if p==100:
        break
# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del(camera)
