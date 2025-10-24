# TFWR Grid Setup

This project provides a grid setup for the game [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) on Steam. It is designed to help automate the farm using a drone by predefining the layout of different farm goals.

## Overview

The farm grid is divided into four quadrants, each serving a specific purpose:

1. **Maze Quadrant**  
   - Uses an oriented Depth-First Search (DFS) to generate a path that approaches the goal efficiently.

2. **Carrots & Hay Quadrant**  
   - Split into two halves: one half for carrots, the other for hay.  

3. **Trees, Sunflowers & Cacti Quadrant**  
   - Split into two halves: one for trees and sunflowers, the other for cacti.  

4. **Pumpkin & Cacti Quadrant**  
   - Split into two halves: one for pumpkins, the other for cacti.  


## Usage

Clone the repository and import into the game folder. Adjust the quadrants as needed to match your farm size or game objectives.

## Contributing

Feel free to submit pull requests for improved layouts, additional crop arrangements, or better pathfinding algorithms.
