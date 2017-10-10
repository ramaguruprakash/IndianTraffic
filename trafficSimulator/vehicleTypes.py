#! /users/guruprakash.r/miniconda2/bin/python
from random import randint

class VehicleTypes:
	def __init__(self):
		self.classes = ['CAR', 'MOTORBIKE', 'VAN', 'TRUCK', 'BUS']

	def getIndex(self, vehicleType):
		return self.classes.index(vehicleType)

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
		print cl
		encoding = self.oneHotEncoding(self.classes[cl])
		return self.classes[cl], encoding
		
