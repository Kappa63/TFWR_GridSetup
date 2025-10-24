PLANT_GROUND = {
	Entities.Grass: Grounds.Soil,
	Entities.Bush: Grounds.Soil,
	Entities.Carrot: Grounds.Soil,
	Entities.Pumpkin: Grounds.Soil,
	Entities.Tree: Grounds.Soil,
	Entities.Sunflower: Grounds.Soil,
	Entities.Cactus: Grounds.Soil
}

DIRECTIONS = [North, East, South, West]
VECTOR_DIR = {
	North: (0, 1),
	South: (0, -1),
	East: (1, 0),
	West: (-1, 0)
}
OPPOSITE_DIR = {
	North: South, 
	South: North, 
	East: West, 
	West: East
}