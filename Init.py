import Functions
import Algorithms
import Calculate

def mazeDrone(posX, posY, subGridSize, freq):
	change_hat(Hats.Green_Hat)
	Functions.droneTo(posX, posY)
	Functions.droneSleep(2)

	center = subGridSize//2
	centerX, centerY = posX + center, posY + center
	while True:
		Functions.droneTo(centerX, centerY)
		plant(Entities.Bush)
		mazeSubstance = Calculate.neededWeirdSubstance(subGridSize)
		for _ in range(freq):
			use_item(Items.Weird_Substance, mazeSubstance)
	
			goalX, goalY = measure()
		
			Algorithms.mazeSolveDFS(centerX, centerY, goalX, goalY, None)
	
		harvest()
		
def standbyDrone(posX, posY):
	Functions.droneTo(posX, posY)
	Functions.droneSleep(2)
		
	mid = get_world_size() // 2

	Functions.droneTo(mid, mid)

	while True:
		for hat in Hats:
			if (num_unlocked(hat)):
				change_hat(hat)
			do_a_flip()
			pet_the_piggy()

def wateringDrone(posX, posY, toX, toY):
	change_hat(Hats.Traffic_Cone)
	Functions.droneTo(posX, posY)
	Functions.droneSleep(2)
	
	while True:
		Functions.coverAreaSpiral(posX, posY, toX, toY, use_item, Items.Water)
				
def pumpkinDrone(posX, posY, toX, toY):
	change_hat(Hats.Pumpkin_Hat)
	Functions.droneTo(posX, posY)
	Functions.droneSleep(2)
	
	Functions.coverAreaSpiral(posX, posY, toX, toY, Functions.perfectPlant, Entities.Pumpkin)
	while True:
		Functions.coverAreaSpiral(posX, posY, toX, toY, Functions.perfectHarvest, Entities.Pumpkin)
		
def bushDrone(posX, posY, subGridSize):
	Functions.droneTo(posX, posY)
	Functions.droneSleep(2)
	
	Functions.coverAreaSpiral(posX, posY, posX+subGridSize-1, posY+subGridSize-1, Functions.perfectPlant, Entities.Bush)
	while True:
		Functions.coverAreaSpiral(posX, posY, posX+subGridSize-1, posY+subGridSize-1, Functions.perfectHarvest, Entities.Bush)
	
def carrotDrone(posX, posY, toX, toY):
	change_hat(Hats.Carrot_Hat)
	Functions.droneTo(posX, posY)
	Functions.droneSleep(2)
		
	Functions.coverAreaSpiral(posX, posY, toX, toY, Functions.perfectPlant, Entities.Carrot)
	while True:
		Functions.coverAreaSpiral(posX, posY, toX, toY, Functions.perfectHarvest, Entities.Carrot)

def hayDrone(posX, posY, toX, toY):
	change_hat(Hats.Straw_Hat)
	Functions.droneTo(posX, posY)
	Functions.droneSleep(2)
	
	Functions.coverAreaSpiral(posX, posY, toX, toY, Functions.perfectPlant, Entities.Grass)
	while True:
		Functions.coverAreaSpiral(posX, posY, toX, toY, Functions.perfectHarvest, Entities.Grass)

def cactusDrone(posX, posY, ToX, toY):
	change_hat(Hats.Cactus_Hat)
	Functions.droneTo(posX, posY)
	Functions.droneSleep(2)
	
	while True:
		Functions.coverAreaSpiral(posX,posY, ToX,toY, Functions.perfectPlant, Entities.Cactus)
		Functions.sortCacti(posX,posY, ToX,toY)
		harvest()
	
def treeAndSunflowerDrone(posX, posY, toX, toY):
	change_hat(Hats.Sunflower_Hat)
	Functions.droneTo(posX, posY)
	Functions.droneSleep(2)
	
	Functions.coverAreaSpiral(posX, posY, toX, toY, Functions.perfectPlant, Entities.Sunflower, 0, 2)
	Functions.coverAreaSpiral(posX, posY, toX, toY, Functions.perfectPlant, Entities.Tree, 1, 2)
	
	while True:
		Functions.coverAreaSpiral(posX, posY, toX, toY, Functions.perfectHarvest, Entities.Sunflower)
	
def dinoDrone(posX, posY, toX, toY): # Currently Failing. Under Construction
	Functions.droneTo(posX, posY)
	Functions.droneSleep(2)
	
	def _rotateHat():
		change_hat(Hats.Brown_Hat)
		Functions.droneTo(posX, posY)
		change_hat(Hats.Dinosaur_Hat)
	
	Functions.coverAreaSpiral(posX, posY, toX, toY, Functions.perfectTill, Grounds.Soil)
	Functions.droneSleep(10)
	change_hat(Hats.Dinosaur_Hat)
	while (get_entity_type() != Entities.Apple):
		continue
	while True:
		if(get_entity_type() != Entities.Apple):
			_rotateHat()
		next = measure()
		if (next == None):
			_rotateHat()
		nextX, nextY = next
		if (not Functions.droneTo(nextX, nextY)):
			_rotateHat()
