# TFWR Grid Setup
![Quadrant Grid](Assets/QuadrantGrid.png)
This project provides a grid setup for the game [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) on Steam. It is designed to help automate the farm using a drone by predefining the layout of different farm goals.

## Overview

This setup is made for 8 drones.
The farm grid is divided into four quadrants, each serving a specific purpose:

1. **Maze Quadrant (1 Drone)**  
   - Uses an oriented Depth-First Search (DFS) to generate a path that approaches the goal efficiently.

2. **Carrots & Hay Quadrant (2 Drones)**  
   - Split into two halves: one half for carrots, the other for hay.  

3. **Trees, Sunflowers & Cacti Quadrant (2 Drones)**  
   - Split into two halves: one for trees and sunflowers, the other for cacti.  

4. **Pumpkin & Cacti Quadrant (2 Drones)**  
   - Split into two halves: one for pumpkins, the other for cacti.
     
- **Watering Drone (1 Drone)**  
   - The 8th drone roams over the Carrots & Hay and Trees/Sunflowers & Cacti quadrants to water crops.

## Usage

Clone the repository and import into the game folder. Adjust the quadrants as needed to match your farm size or game objectives.

## Contributing

Feel free to submit pull requests for improved layouts, additional crop arrangements, or better pathfinding algorithms.
