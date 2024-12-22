import math

def distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair(points):
    # Sort the points by their x-coordinates
    points.sort(key=lambda point: point[0])
    
    def brute_force_closest_pair(p):
        """Find the closest pair in a small set of points using brute force."""
        min_dist = float('inf')
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                dist = distance(p[i], p[j])
                if dist < min_dist:
                    min_dist = dist
        return min_dist
    
    def closest_pair_recursive(left, right):
        """Recursively find the closest pair using divide and conquer."""
        if right - left <= 3:  # Base case for brute force
            return brute_force_closest_pair(points[left:right + 1])
        
        mid = (left + right) // 2
        mid_point = points[mid]
        
        # Recursively find the closest pair in each half
        min_dist_left = closest_pair_recursive(left, mid)
        min_dist_right = closest_pair_recursive(mid + 1, right)
        
        # Determine the minimum distance from both halves
        min_dist = min(min_dist_left, min_dist_right)
        
        # Points within the strip around the dividing line
        strip_points = [points[i] for i in range(left, right + 1) if abs(points[i][0] - mid_point[0]) < min_dist]
        
        # Check pairs in the strip
        for i in range(len(strip_points)):
            for j in range(i + 1, len(strip_points)):
                dist = distance(strip_points[i], strip_points[j])
                if dist < min_dist:
                    min_dist = dist
        
        return min_dist
    
    n = len(points)
    
    # Find the closest pair
    min_distance = closest_pair_recursive(0, n - 1)
    
    return min_distance

# Example usage
if __name__ == "__main__":
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    closest_distance = closest_pair(points)
    print("Closest pair distance:", closest_distance)
