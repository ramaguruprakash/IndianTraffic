#! /users/guruprakash.r/miniconda2/bin/python
from random import randint

class Vehicle:
		def __init__(self, cl, route, startTime, positionUpdater):
			self.cl = cl
			self.route = route
			self.positionUpdater = positionUpdater
			self.curX = -1
			self.curY = -1
			self.startTime = startTime
			self.track = []
			self.speed = randint(1, 5)
			self.numberOfEdgesCompleted = 0

		def move(self, timestamp, grid, vehicles):
			if (timestamp < self.startTime):
				self.track.append((-1, -1))
				return
			self.numberOfEdgesCompleted, x, y = self.positionUpdater.updatePos(grid, self, vehicles)
			print self.cl + " " + str(x) + " " + str(y)
			if self.numberOfEdgesCompleted == -1:
				self.curX = -1
				self.curY = -1
				return

			if self.numberOfEdgesCompleted != len(self.route.edges):
				self.curX = x
				self.curY = y
				self.track.append((x,y))

		def __str__(self):
			return self.cl + " Route:-\n" + str(self.route) + " Pos:- (" + str(self.curX) + ", " + str(self.curY) + ") " + str(self.startTime) + "\n"

		def __repr__(self):
			return self.cl + " " + str(self.route) + " (" + str(self.curX) + "," + str(self.curY) + ") " + str(self.startTime) + "\n"
