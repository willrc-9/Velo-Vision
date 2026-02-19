import cv2
import threading
import os
import time

class ThreadedGoPro:
    def __init__(self, url):
        # Configure OpenCV for network streams
        os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'timeout;5000'

        # Initialize the stream
        self.stream = cv2.VideoCapture(url, cv2.CAP_FFMPEG)
        self.stream.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        # Read the first frame to establish the connection
        self.grabbed, self.frame = self.stream.read()
        self.stopped = False

        # Start the background thread
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.daemon = True  # Ensures thread closes when main program exits
        self.thread.start()

    def update(self):
        # This loops infinitely in the background
        while not self.stopped:
            self.grabbed, self.frame = self.stream.read()

            if not self.grabbed:
                print("Network stutter. Waiting for next frame...")
                time.sleep(1)  # Adds a 1-second pause so it doesn't nuke your console

    def read(self):
        # The main loop calls this to get the newest frame instantly
        return self.frame

    def stop(self):
        # Safely shut down the thread and release the camera
        self.stopped = True
        self.thread.join(timeout=1)
        self.stream.release()