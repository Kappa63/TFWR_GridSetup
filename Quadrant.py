import Init
import Functions

gridSize = get_world_size()
gridCenter = gridSize//2

def quadrantI():
	Init.mazeDrone(gridCenter, gridCenter, gridCenter, 1)

def quadrantII():
	subGridCenter = (gridCenter+1)//2
	toX, toY = gridCenter-1, gridCenter-1
	excess = gridCenter%2
	def subQuadrantI():
		Init.carrotDrone(0, 0, toX-subGridCenter+excess, toY)
		
	spawn_drone(subQuadrantI)
	Init.hayDrone(subGridCenter, 0, toX, toY)

def quadrantIII():
	subGridCenter = (gridCenter+1)//2
	toX, toY = gridCenter+gridCenter-1, gridCenter-1
	excess = gridCenter%2
	def subQuadrantI():
		Init.pumpkinDrone(gridCenter, 0, toX, toY-subGridCenter+excess)
		
	spawn_drone(subQuadrantI)
	Init.cactusDrone(gridCenter, subGridCenter, toX, toY)

def quadrantIV():
	subGridCenter = (gridCenter+1)//2
	toX, toY = gridCenter-1, gridCenter+gridCenter-1
	excess = gridCenter%2
	def subQuadrantI():
		Init.treeAndSunflowerDrone(0, gridCenter, toX, toY-subGridCenter+excess)
		
	spawn_drone(subQuadrantI)
	Init.cactusDrone(0, gridCenter+subGridCenter, toX, toY)

Functions.resetGrid()

spawn_drone(quadrantI)
spawn_drone(quadrantII)
spawn_drone(quadrantIII)
spawn_drone(quadrantIV)

Init.wateringDrone(0,0, gridCenter-1,gridSize-1)
