import subprocess
import detect
import cv2
import cv2.cv as cv
import time

BRIGHTNESS = "40"

def checkUser(img):
	gray = cv2.cvtColor(img, cv.CV_RGB2GRAY)
	gray = cv2.equalizeHist(gray)
	eyes = detect.detect(gray)
	if len(eyes) <= 0:
		return 0
	else:
		return 1

vc = cv2.VideoCapture(0)

ret, frame = vc.read()
conti_count = 0

while ret:
	flag = checkUser(frame)
	if flag == 1:
		conti_count = 0
		subprocess.call("xbacklight -set " + BRIGHTNESS, shell = True)
		time.sleep(10)
	else:
		conti_count += 1
		if conti_count > 5:
			subprocess.call("xbacklight -set 3 -time 100", shell = True)
		time.sleep(2)
	ret, frame = vc.read()
	key = cv2.waitKey(20)
	if key == 27:
		break

cv2.destroyAllWindows()