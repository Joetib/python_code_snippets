# We can use the brute force approach to find the closest pair of points in a list of coordinates.
# The brute force approach compares the distance between each pair of points and keeps track of the minimum distance found so far.

import math

def distance(p1, p2):
    # Calculate the Euclidean distance between two points
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def closest_pair(points):
    min_distance = float('inf')
    closest_points = None
    
    # Compare the distance between each pair of points
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_points = (points[i], points[j])
    
    return closest_points

# Example usage
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
closest = closest_pair(points)
print(closest)

# Output
# >> ((3, 4), (5, 6))
# Please Like and Subscribe