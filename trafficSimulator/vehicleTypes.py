#! /users/guruprakash.r/miniconda2/bin/python
from random import randint

class VehicleTypes:
	def __init__(self):
		self.classes = ['CAR', 'MOTORBIKE', 'VAN', 'TRUCK', 'BUS']
		self.sizes = [(6,12), (4,10), (8,16), (10,20), (15,30)]

	def getIndex(self, vehicleType):
		return self.classes.index(vehicleType)

	def getSize(self, vehicleType):
		index = self.classes.index(vehicleType)
		return self.sizes[index]

	def listVehilceTypes(self):
		for ty in self.classes:
			print ty

	def oneHotEncoding(self, vehicleType):
		index =	self.getIndex(vehicleType)
		size = len(self.classes)
		encoding = [0]*size
		encoding[index] = 1
		return encoding

	def sample(self):
		cl = randint(0, len(self.classes)-1)
		encoding = self.oneHotEncoding(self.classes[cl])
		return self.classes[cl], encoding

if __name__=="__main__":
	import cv2
	import numpy as np
	vehicleTypes = VehicleTypes()
	t = 100
	while(t):
		img = np.zeros((1000,1000,3), np.uint8)
		vehi , _ = vehicleTypes.sample()
		vehi_size = vehicleTypes.getSize(vehi)
		print vehi, vehi_size, 500-vehi_size[0]/2, 500-vehi_size[1]/2, 500+vehi_size[0]/2, 500+vehi_size[1]/2
		cv2.rectangle(img,(500-vehi_size[0]/2,500-vehi_size[1]/2), (500+vehi_size[0]/2,500+vehi_size[1]/2), (0,255,0), 1)
		cv2.imshow("rect", img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		t -= 1
