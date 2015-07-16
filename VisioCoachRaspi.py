__author__ = 'emc333'
__version__ = '1.6'

# import the necessary packages
from collections import deque
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


class OpenCVTEST:
    def __init__(self):
        # initialize the camera and grab a reference to the raw camera capture
        factor = 1.5
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 32
        self.rawCapture = PiRGBArray(self.camera, size=(640, 480))
        # allow the camera to warmup
        time.sleep(0.1)
        cv2.namedWindow("Video")

        self.pictureBuffer = deque()

        self.currentPicture = None
        self.firstPicture = None

    def showPicture(self, picture):
        cv2.imshow("Video", picture)

    def addPicture(self, picture):
        self.pictureBuffer.append(picture)

    def getCurrentPicture(self):
        return self.currentPicture

    def getPicture(self):
        return self.pictureBuffer.popleft()

    def forePlay(self):
        number = 0
        for frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
            self.currentPicture = frame.array
            self.addPicture(self.currentPicture)
            self.rawCapture.truncate(0)

            number += 1
            if number >= 100:
                break
        self.play()

    def play(self):
        for frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
            self.currentPicture = frame.array
            self.addPicture(self.currentPicture)
            self.showPicture(self.getPicture())
            self.rawCapture.truncate(0)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        print("Bye bye!")

if __name__ == "__main__":
    o = OpenCVTEST()
    o.forePlay()
