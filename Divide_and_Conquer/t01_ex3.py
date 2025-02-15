# CLOSEST PAIR OF POINTS

import random
import matplotlib.pyplot as plt

def visualize_points(points):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.scatter(x, y)

def visualize_line(line, color='blue', linestyle='-'):
    x = [point[0] for point in line]
    y = [point[1] for point in line]
    plt.plot(x, y, color=color, linestyle=linestyle)

def euclidean_distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def manhattan_distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def brute_force(points, s, e):
    min_dist = float('inf')
    for i in range(s, e):
        for j in range(i+1, e+1):
            dist = distance_func(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_points = (points[i], points[j])
    return min_dist, closest_points

def merge_sort_by_y(points, s, mid, e):
    left = points[s:mid+1]
    right = points[mid+1:e+1]
    i = j = 0
    k = s
    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            points[k] = left[i]
            i += 1
        else:
            points[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        points[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        points[k] = right[j]
        j += 1
        k += 1

    del left, right, i, j, k
        

def _find_closest_points(points, s, e): # simultaneously sort by y using merge sort
    if e-s+1 <= 3:
        # O(1)
        points[s:e+1] = sorted(points[s:e+1], key=lambda point: point[1])
        return brute_force(points, s, e)
    
    mid = (s + e) // 2
    left_min_dist, left_closest_points = _find_closest_points(points, s, mid)
    right_min_dist, right_closest_points = _find_closest_points(points, mid+1, e)
    assert len(left_closest_points) == 2 and len(right_closest_points) == 2

    min_dist = min(left_min_dist, right_min_dist)
    closest_points = left_closest_points if left_min_dist < right_min_dist else right_closest_points

    # find the points that are x-wise within min_dist from the middle line wrt. points from s to e
    middle_x = (points[mid][0] + points[mid+1][0]) / 2
    # O(n) since it will iterate through all the points from s to e
    middle_points = [point for point in points[s:e+1] if abs(point[0] - middle_x) < min_dist]
    
    # MERGE STEP - sort by y - we know that the points are already sorted by y from s to mid and mid+1 to e (Merge Sort)
    merge_sort_by_y(points, s, mid, e)
    
    # O(1) since the first if statement will break the loop if the y difference is greater than min_dist
    # This will happen
    for i, point1 in enumerate(middle_points):
        for j, point2 in enumerate(middle_points[i+1:], start=i+1):
            if point2[1] - point1[1] >= min_dist: # if the y difference is greater than min_dist, break because the rest will be greater since it's sorted by y
                break
            dist = distance_func(point1, point2)
            if dist < min_dist:
                min_dist = dist
                closest_points = (point1, point2)
    
    return min_dist, closest_points
    
def find_closest_points(points, s, e):
    # sort by x - O(nlogn)
    points.sort(key=lambda point: point[0])
    print(points)
    return _find_closest_points(points, s, e)

if __name__ == "__main__":
    points = [(random.randint(-100, 100), random.randint(-100, 100)) for _ in range(10)]
    visualize_points(points)

    distance_func = euclidean_distance
    min_dist, closest_points = find_closest_points(points, 0, len(points)-1) # side effect: points will be sorted by y

    visualize_line(closest_points, color='red', linestyle='-')
    
    plt.show()