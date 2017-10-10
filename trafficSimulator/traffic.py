#! /users/guruprakash.r/miniconda2/bin/python

from roadNetwork import RoadNetwork
from vehicle import Vehicle
import numpy as np
import cv2
import time

class Traffic:
	def __init__(self, roadNetwork, vehicles, size, totalTime):
		self.roadNetwork = roadNetwork
		self.vehicles = vehicles
		self.size = size
		self.totalTime = totalTime
		print size
		self.grid = np.zeros(size)
		self.drawNetwork()
		self.drawVehicles()

	def drawNetwork(self):
		edges = self.roadNetwork.edges
		nodes = self.roadNetwork.nodes
		for edge in edges:
			nodeI = edge.node1
			nodeJ = edge.node2
			width = edge.width
			### Prastutaniki angle em ledhu, only straight lines
			cv2.line(self.grid, (int(nodeI.x-width/2), nodeI.y), (int(nodeI.x-width/2), nodeJ.y), (255,0,0),1)
			cv2.line(self.grid, (int(nodeI.x+width/2), nodeI.y), (int(nodeI.x+width/2), nodeJ.y), (255,0,0),1)

	def drawVehicles(self):
		for vehicle in self.vehicles:
			if vehicle.curX == -1 and vehicle.curY == -1:
				continue
			self.grid[vehicle.curY, vehicle.curX] = [255,0,0]

	def updateGrid(self):
		self.grid = np.zeros(self.size)
		self.drawNetwork()
		self.drawVehicles()

	def simulateAndVisualize(self):
		t = 0
		while(t < self.totalTime):
			for vehicle in self.vehicles:
				vehicle.move(t, self.grid)
			self.updateGrid()
			t += 1
			cv2.imshow("sim", self.grid)
			if cv2.waitKey(33) == 27:
				break
			#cv2.waitKey(0)
		cv2.destroyAllWindows()

	def simulateAndExport(self):
		t = 0
		while(t < self.totalTime):
			for vehicle in self.vehicles:
				vehicle.move(t, self.grid)
			self.updateGrid()
			t += 1
		self.export()


	def export(self):
		exportFileName = "traffic_" + str(len(self.roadNetwork.edges)) + "_" + str(len(self.vehicles)) + "_" + str(time.time()) + ".txt"
		fp = open(exportFileName, "w")
		trafficSummary = str(self.grid.shape[0]) + " " + str(self.grid.shape[1]) + " " + str(self.totalTime) + "\n"
		fp.write(trafficSummary)

		fp.write(str(len(self.roadNetwork.edges)) + "\n")
		for edge in self.roadNetwork.edges:
			fp.write(str(edge.node1.x) + " " + str(edge.node1.y) + " " + str(edge.node2.x) + " " + str(edge.node2.y) + " " + str(edge.width) + "\n")

		fp.write(str(len(self.vehicles)) + "\n")
		for vehicle in self.vehicles:
			fp.write(vehicle.cl + "\n")
			tracklen = len(vehicle.track)
			for t in range(self.totalTime):
				if t >= tracklen:
					fp.write(str(t) + " " + str(-1) + " " + str(-1) + "\n")
					continue
				fp.write(str(t) + " " + str(vehicle.track[t][0]) + " " + str(vehicle.track[t][1]) + "\n")
		fp.close()
