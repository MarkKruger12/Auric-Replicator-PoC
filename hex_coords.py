# Replicator Magnet Coordinates
# Part of the Digital Trail for USPTO 19/556,532
# Geometry: 7-Magnet Hexagonal Array (N52 Discs)

import numpy as np

def get_coords():
    # Central Eye Radius = 1.0 inch (25.4 mm)
    r = 25.4 
    
    # Coordinates in [x, y] format (mm)
    # 0 is the center magnet, 1-6 are the outer ring
    coords = [
        [0.0, 0.0],          # Center Magnet
        [25.4, 0.0],         # Magnet 1 (0°)
        [12.7, 22.0],        # Magnet 2 (60°)
        [-12.7, 22.0],       # Magnet 3 (120°)
        [-25.4, 0.0],        # Magnet 4 (180°)
        [-12.7, -22.0],      # Magnet 5 (240°)
        [12.7, -22.0]        # Magnet 6 (300°)
    ]
    return coords

if __name__ == "__main__":
    points = get_coords()
    print("Replicator Hexagonal Array Loaded:")
    for i, p in enumerate(points):
        print(f"Position {i}: {p}")
