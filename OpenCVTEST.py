__author__ = 'emcNinja333'
__version__ = '1.6'


from collections import deque
from time import sleep
import cv2
import cv

class OpenCVTEST:

    def __init__(self):
        camera_index = 0
        factor = 1.5
        self.cap = cv2.VideoCapture(camera_index)
        self.cap.set(4, int(640 * factor))
        self.cap.set(5, int(360 * factor))
        cv2.namedWindow("Video")

        self.pictureBuffer = deque()

        self.currentPicture = None
        self.firstPicture = None

    def takePicture(self):
        self.cap.grab()
        buf, self.currentPicture = self.cap.read()
        self.addPicture(self.currentPicture)

    def showPicture(self, picture):
        cv2.imshow("Video", picture)

    def addPicture(self, picture):
        self.pictureBuffer.append(picture)

    def getCurrentPicture(self):
        return self.currentPicture

    def getPicture(self):
        return self.pictureBuffer.popleft()

    def forePlay(self):
        self.takePicture()
        self.firstPicture = self.getPicture()
        self.showPicture(self.firstPicture)

        for i in range(100):
            self.takePicture()
        self.play()

    def play(self):
        while True:
            if (cv.WaitKey(1) == ord('q')):
                print("finish")
                break
            self.takePicture()
            self.showPicture(self.getPicture())

if __name__ == "__main__":
    o = OpenCVTEST()
    o.forePlay()
