"""Captures video from the default camera, converts it to grayscale, and displays it in a window.
The video feed is displayed until the user presses the 'q' key.
"""
import cv2

video = cv2.VideoCapture(1)
while True:
    check, frame = video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video Capture", gray)
    key=cv2.waitKey(1)

    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
