import math

def orientation(p, q, r):
    """
    To find the orientation of (p, q, r).
    The function returns:
      0 : Colinear
      1 : Clockwise
      2 : Counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def dist_sq(p, q):
    """
    To find the squared distance between two points.
    """
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2

def dist(p, q):
    """
    To find the distance between two points.
    """
    return ((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2) ** 0.5

def graham_scan(points):
    """
    Implementation of Graham Scan algorithm to find the convex hull.
    """
    if len(points) < 3:
        return points
    
    # Find the bottommost point
    ymin = min(points, key=lambda p: (p[1], -p[0]))  # Also handles duplicates by x-coordinates
    points.sort(key=lambda p: (math.atan2(p[1] - ymin[1], p[0] - ymin[0]), dist(ymin, p)))
    
    stack = [ymin, points[0], points[1]]
    
    for i in range(2, len(points)):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], points[i]) != 2:
            stack.pop()
        stack.append(points[i])
    
    return stack

# Example usage
points = [(1, 1), (2, 5), (3, 3), (5, 3), (3, 2), (2, 2)]
hull = graham_scan(points)
print("Convex Hull Points:", hull)
