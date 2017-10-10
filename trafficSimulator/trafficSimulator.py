#! /users/guruprakash.r/miniconda2/bin/python
from roadNetwork import RoadNetwork
from vehicle import Vehicle
from node import Node
from edge import Edge
from yvehicleMover import YvehicleMover
from traffic import Traffic
import random
from vehicleTypes import VehicleTypes 

def getSingleLaneNetwork(x1,y1,x2,y2,w):
	node1 = Node(x1,y1)
	node2 = Node(x2,y2)
	nodeList  = [node1, node2]
	edge = Edge(node1, node2, w)
	edgeList = [edge]
	return RoadNetwork(nodeList, edgeList)

def getVehicles(noOfvehicles, route):
	vehicleList = []
	vehicleTypes = VehicleTypes()
	for i in range(noOfvehicles):
		vehicleType , _ = vehicleTypes.sample()
		vehicle = Vehicle(vehicleType, route, int(10*random.random()), YvehicleMover())
		vehicleList.append(vehicle)
	return vehicleList

if __name__ == "__main__":
	network = getSingleLaneNetwork(100, 100, 100, 300, 200)
	print network
	numberOfTracks = 1000
	numberOfPointsPerTrack = 100
	numberOfVehicles = 100
	for i in range(0, numberOfTracks, numberOfVehicles):
		vehicles = getVehicles(numberOfVehicles, network)
		print vehicles
		traffic = Traffic(network, vehicles, (500,500,3), 200)
	#traffic.simulateAndVisualize()
	#traffic.export()
		traffic.simulateAndExport()
