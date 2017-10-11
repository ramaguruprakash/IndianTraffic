#! /users/guruprakash.r/miniconda2/bin/python
from roadNetwork import RoadNetwork
from vehicle import Vehicle
from node import Node
from edge import Edge
from yvehicleMover import YvehicleMover
from traffic import Traffic
import random
from vehicleTypes import VehicleTypes
from simpleLaneMovement import SimpleLaneMovement
from edgeWithLanes import EdgeWithLanes
import pdb

def getSingleLaneNetwork(x1,y1,x2,y2,w):
	node1 = Node(x1,y1)
	node2 = Node(x2,y2)
	nodeList  = [node1, node2]
	edge = EdgeWithLanes(node1, node2, w, 4)
	edgeList = [edge]
	return RoadNetwork(nodeList, edgeList)

def getVehicles(noOfvehicles, route):
	vehicleList = []
	vehicleTypes = VehicleTypes()
	for i in range(noOfvehicles):
		vehicleType , _ = vehicleTypes.sample()
		#vehicle = Vehicle(vehicleType, route, int(10*random.random()), YvehicleMover())
		vehicle = Vehicle(vehicleType, route, int(10*random.random()), SimpleLaneMovement())
		vehicleList.append(vehicle)
	return vehicleList

if __name__ == "__main__":
	network = getSingleLaneNetwork(100, 100, 100, 300, 200)
	print network
	numberOfTracks = 1000
	numberOfPointsPerTrack = 100
	numberOfVehicles = 10
	for i in range(0, numberOfTracks, numberOfVehicles):
		vehicles = getVehicles(numberOfVehicles, network)
		traffic = Traffic(network, vehicles, (500,500,3), 300)
	traffic.simulateAndVisualize()
	traffic.export()
		#traffic.simulateAndExport()
