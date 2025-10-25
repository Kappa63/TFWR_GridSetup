import env
import Calculate

def droneTo(toX, toY, wrapped=True):
	gridSize = get_world_size()
	posX, posY = get_pos_x(), get_pos_y()

	if wrapped:
		diffX = (toX - posX + gridSize) % gridSize
		diffY = (toY - posY + gridSize) % gridSize
		if (diffX <= gridSize // 2):
			stepsX = diffX
		else:
			stepsX = diffX - gridSize
		
		if (diffY <= gridSize // 2):
			stepsY = diffY
		else:
			stepsY = diffY - gridSize
	else:
		stepsX = toX- posX
		stepsY = toY - posY

	if stepsX > 0:
		for _ in range(stepsX):
			if not move(East):
				return False
	elif stepsX < 0:
		for _ in range(-stepsX):
			if not move(West):
				return False
				
	if stepsY > 0:
		for _ in range(stepsY):
			if not move(North):
				return False
	elif stepsY < 0:
		for _ in range(-stepsY):
			if not move(South):
				return False

	return True

def perfectHarvest(seed):
	toReplant = get_entity_type()
	if (toReplant == Entities.Apple):
		return
	if (can_harvest()):
		harvest()
		plant(toReplant)
	elif (toReplant == None or toReplant == Entities.Dead_Pumpkin):
		plant(seed)
		
def resetGrid():
	droneTo(0, 0)
	harvest()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, Calculate.neededWeirdSubstance(get_world_size()))
	harvest()

def droneSleep(time):
	for _ in range(time):
		do_a_flip()
		
def perfectPlant(seed):
	perfectTill(env.PLANT_GROUND[seed])
	plant(seed)

def perfectTill(ground):
	if (get_ground_type() != ground):
		till()
		
def perfectWater(_):
	if (get_water() <= 0.65):
		use_item(Items.Water)
		
def coverAreaSpiral(posX, posY, toX, toY, fn, arg, start=0, every=1):
	droneTo(posX, posY)
	curPosX, curPosY = posX, posY
	i = 0
	started = False
	while posX <= toX and posY <= toY:
		while curPosX < toX:
			if (not started and i >= start):
				started = True
				i = 0
			if (started and not i%every):
				fn(arg)
			move(East)
			i += 1
			curPosX += 1
		posY += 1
		
		while curPosY < toY:
			if (not started and i >= start):
				started = True
				i = 0
			if (started and not i%every):
				fn(arg)
			move(North)
			i += 1
			curPosY += 1
		toX -= 1
		
		if posY <= toY:
			while curPosX > posX:
				if (not started and i >= start):
					started = True
					i = 0
				if (started and not i%every):
					fn(arg)
				move(West)
				i += 1
				curPosX -= 1
			toY -= 1

		if posX <= toX:
			while curPosY > posY:
				if (not started and i >= start):
					started = True
					i = 0
				if (started and not i%every):
					fn(arg)
				move(South)
				i += 1
				curPosY -= 1
			posX += 1
	if (not started and i >= start):
		started = True
		i = 0
	if (started and not i%every):
		fn(arg)


def sortCacti(posX, posY, toX, toY):
	droneTo(posX, posY)
	for p in range(toY-posY+1):
		for i in range(toX-posX-1):
			for _ in range(toX-posX-i):
				if measure(East) < measure():
					swap(East)
				move(East)

			for _ in range(toX-posX-i):
				move(West)
		if (p != toY-posY):
			move(North)
	droneTo(posX, posY)
	for p in range(toX-posX+1):
		for i in range(toY-posY-1):
			for _ in range(toY-posY-i):
				if measure(North) < measure():
					swap(North)
				move(North)

			for _ in range(toY-posY-i):
				move(South)
		if (p != toX-posX):
			move(East)