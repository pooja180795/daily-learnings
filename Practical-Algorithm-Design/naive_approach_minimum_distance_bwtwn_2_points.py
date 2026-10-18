# time-complexity = O(n^2)

import math
def distance(p1, p2):
    d = 0
    for i in range(len(p1)):                            # not n but size of the points (2,3) so it can considered as constant
        d += (p1[i] - p2[i]) ** 2
    return math.sqrt(d)

def find_min_distance(points):
    n = len(points)
    min_distance = float("inf")
    for i in range(n):                                  # n
        for j in range(i+1, n):                         # n
            dis = distance(points[i], points[j])
            if dis < min_distance:
                min_distance = dis
    return min_distance

points = [[ -1, -2,6 ], [ 0, 0,6 ], [ 1, 2,3 ], [ 2, 3,5 ]]

dis = find_min_distance(points)

print(dis)



