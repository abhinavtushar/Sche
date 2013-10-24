import subprocess
import detect
import cv2
import cv2.cv as cv
import time

def checkUser(img):
	gray = cv2.cvtColor(img, cv.CV_RGB2GRAY)
	gray = cv2.equalizeHist(gray)
	eyes = detect.detect(gray)
	print eyes
	if len(eyes) <= 0:
		return 0
	else:
		return 1

vc = cv2.VideoCapture(0)

ret, frame = vc.read()

while ret:
	flag = checkUser(frame)
	if flag == 1:
		print "Eyes Open"
	else:
		print "Eyes Closed"
		#subprocess.call("nircmdx64 monitor off", shell = True)
	ret, frame = vc.read()
	key = cv2.waitKey(20)
	if key == 27:
		break

cv2.destroyAllWindows()