import env

def manhattanDistance(droneX, droneY, goalX, goalY):
	return abs(droneX - goalX) + abs(droneY - goalY)

def isBound(row, col, gridSize):
	return (row >= 0) and (row < gridSize) and (col >= 0) and (col < gridSize)
	
# def sortWithFunction(l, fn):
# 	lCopy = l[:]
# 	n = len(l)
# 	for i in range(n):
# 		for j in range(0, n - i - 1):
# 			if fn(lCopy[j]) > fn(lCopy[j + 1]):
# 				lCopy[j], lCopy[j + 1] = lCopy[j + 1], lCopy[j]
# 	return lCopy
	
def sortWithFunction(l, fn):
	def quicksort(arr):
		if len(arr) <= 1:
			return arr

		pivot = arr[len(arr) // 2]
		left, middle, right = [], [], []

		for x in arr:
			val = fn(x)
			pivot_val = fn(pivot)
			if val < pivot_val:
				left.append(x)
			elif val == pivot_val:
				middle.append(x)
			else:
				right.append(x)

		return quicksort(left) + middle + quicksort(right)

	return quicksort(l[:])


def mazeSolveDFS(droneX, droneY, goalX, goalY, visited = None):
	if (visited == None):
		visited = set()
	
	if ((droneX, droneY) == (goalX, goalY)):
		return True
	
	visited.add((droneX, droneY))
	
	def nearest(dir):
		vectorDir = env.VECTOR_DIR[dir]
		return manhattanDistance(droneX + vectorDir[0], 
								 droneY + vectorDir[1],
								 goalX, goalY)
	
	nearestDirs = sortWithFunction(env.DIRECTIONS, nearest)
	
	for dir in nearestDirs:
		vX, vY = env.VECTOR_DIR[dir]
		moveToX, moveToY = droneX + vX, droneY + vY
		
		if (moveToX, moveToY) in visited:
			continue
			
		if move(dir):
			if (mazeSolveDFS(moveToX, moveToY, goalX, goalY, visited)):
				return True
			move(env.OPPOSITE_DIR[dir])
		
	return False