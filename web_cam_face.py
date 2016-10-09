# -*- coding: utf-8 -*-

import cv2

#path for cascades
casc_path_face=' enter cascade path here' #copy the location of face cascade as string eg(C:\opencv\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml)

#creating cascades
face_cascade=cv2.CascadeClassifier(casc_path_face)
print type(face_cascade)

#creating video object
video_capture=cv2.VideoCapture(0)


while(True):
	
		
	ret,image=video_capture.read()
	print"frame read"
		
		
	#coverting to grey
	gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	print" converted to gray \n"

		#fuctions returns a list with (x cordinate,y cordinate,width,height) as each element 
	faces=face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(30,30),flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
		
	print"faces list created"
		
	#draw rectangle 
	for (x,y,w,h) in faces:
					cv2.rectangle(image,(x,y),(x+w,y+h),(1,256,0),2)
		
		
	print "faces found {0} ".format(len(faces))	
	cv2.imshow("gray",gray)
	cv2.imshow("q to quit",image)
	if cv2.waitKey(1)==ord('q'):
				break
					
					
video_capture.release()
cv2.destroyAllWindows()
