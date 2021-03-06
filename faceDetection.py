import cv2
import threading
import numpy as np
class FaceDetection(threading.Thread):
	def __init__(self, parent):
		threading.Thread.__init__(self)
		self.nom = "nom"
		self._stopevent = threading.Event( )
		self.parent = parent
	def run(self):
		while not self._stopevent.isSet():
			#try/catch
			try:
				faceDetect = np.copy(self.parent.im_thread)
				mask = np.zeros(faceDetect.shape,np.uint8)
				cascade = cv2.CascadeClassifier("haar/haarcascade_frontalface_alt.xml")

				faces = cascade.detectMultiScale(faceDetect)
				for face in faces:
					cv2.rectangle(mask, (face[0], face[1]), (face[0] + face[2], face[0] + face[3]), (255,255, 255), -1)	
				mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)		
				#val, mask = cv2.threshold(faceDetect, 245, 255, cv2.THRESH_BINARY_INV)
				#faceDetect = cv2.add(faceDetect,np.zeros(faceDetect.shape,np.uint8),mask = mask)
				self.parent.im_face = mask
				if self.parent.debugType == 'face':
					cv2.imshow('face detection',cv2.bitwise_not(mask))
			except Exception as detail:
				print "ERROR: face detection (", ")"
	def stop(self):
		self._stopevent.set()