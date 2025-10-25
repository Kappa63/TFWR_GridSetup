import Init
import Functions

gridSize = get_world_size()
gridCenter = gridSize//2

def quadrantI():
	subGridCenter = (gridCenter+1)//2
	toX, toY = gridCenter+gridCenter-1, gridCenter+gridCenter-1
	#excess = gridCenter%2
	def subAreaI():
		Init.mazeDrone(gridCenter, gridCenter, subGridCenter, 5)
	def subAreaII():
		Init.mazeDrone(gridCenter, gridCenter+subGridCenter, subGridCenter, 5)
	def subAreaIII():
		Init.mazeDrone(gridCenter+subGridCenter, gridCenter+subGridCenter, subGridCenter, 5)

	spawn_drone(subAreaI)
	spawn_drone(subAreaII)
	spawn_drone(subAreaIII)
	Init.mazeDrone(gridCenter+subGridCenter, gridCenter, subGridCenter, 5)

def quadrantII():
	subGridCenter = (gridCenter+1)//2
	toX, toY = gridCenter-1, gridCenter-1
	#excess = gridCenter%2
	def subAreaI():
		Init.carrotDrone(0, 0, toX-subGridCenter, toY-subGridCenter)
	def subAreaII():
		Init.hayDrone(0, subGridCenter, toX-subGridCenter, toY)
	def subAreaIII():
		Init.carrotDrone(subGridCenter, subGridCenter, toX, toY)
	def subAreaIV():
		Init.hayDrone(subGridCenter, 0, toX, toY-subGridCenter)
		
	spawn_drone(subAreaI)
	spawn_drone(subAreaII)
	spawn_drone(subAreaIII)
	spawn_drone(subAreaIV)
	Init.wateringDrone(0, 0, toX, toY)

def quadrantIII():
	subGridCenter = (gridCenter+1)//2
	toX, toY = gridCenter+gridCenter-1, gridCenter-1
	#excess = gridCenter%2
	def subAreaI():
		Init.cactusDrone(gridCenter, 0, toX-subGridCenter, toY-subGridCenter)
	def subAreaII():
		Init.pumpkinDrone(gridCenter, subGridCenter, toX-subGridCenter, toY)
	def subAreaIII():
		Init.cactusDrone(gridCenter+subGridCenter, subGridCenter, toX, toY)
	def subAreaIV():
		Init.pumpkinDrone(gridCenter+subGridCenter, 0, toX, toY-subGridCenter)
		
	spawn_drone(subAreaI)
	spawn_drone(subAreaII)
	spawn_drone(subAreaIII)
	spawn_drone(subAreaIV)
	Init.wateringDrone(gridCenter, 0, toX, toY)

def quadrantIV():
	subGridCenter = (gridCenter+1)//2
	toX, toY = gridCenter-1, gridCenter+gridCenter-1
	#excess = gridCenter%2
	def subAreaI():
		def subPathI():
			Init.treeDrone(0, gridCenter, toX-subGridCenter, toY-subGridCenter)
		spawn_drone(subPathI)
		Functions.droneSleep(1)
		Init.sunflowerDrone(0, gridCenter, toX-subGridCenter, toY-subGridCenter)
	def subAreaII():
		Init.pumpkinDrone(0, gridCenter+subGridCenter, toX-subGridCenter, toY)
	def subAreaIII():
		def subPathI():
			Init.treeDrone(subGridCenter, subGridCenter+gridCenter, toX, toY)
		spawn_drone(subPathI)
		Functions.droneSleep(1)
		Init.sunflowerDrone(subGridCenter, subGridCenter+gridCenter, toX, toY)
	def subAreaIV():
		Init.pumpkinDrone(subGridCenter, gridCenter, toX, toY-subGridCenter)
	spawn_drone(subAreaI)
	spawn_drone(subAreaII)
	spawn_drone(subAreaIII)
	spawn_drone(subAreaIV)
	Init.wateringDrone(0, gridCenter, toX, toY)

def supportI():
	Init.fertilizingDrone(0,0, gridCenter-1,gridCenter-1)

Functions.resetGrid()

spawn_drone(quadrantI)
spawn_drone(quadrantII)
spawn_drone(quadrantIII)
spawn_drone(quadrantIV)

Init.fertilizingDrone(0,0, gridCenter-1,gridCenter-1)