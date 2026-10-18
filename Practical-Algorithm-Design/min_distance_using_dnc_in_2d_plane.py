#O(nlogn)
import math

def euclidean_dis(p1, p2):
    dis = 0
    for i in range(len(p1)):
        dis += (p1[i] - p2[i]) ** 2
    return math.sqrt(dis)

def brute_force(points):   #it looks O(n^2)  but its O(n/3)
    n = len(points)
    min_dis = float("inf")
    for i in range(n):
        for j in range(i+1, n):
            dis  = euclidean_dis(points[i], points[j])
            if dis < min_dis:
                min_dis = dis

    return min_dis

def strip_closest(strip, d):      #O(n)
    min_dist = d
    strip.sort(key=lambda p:p[1])               #O(n logn)

    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if strip[j][1] - strip[i][1] >= d:
                break
            min_dist = min(min_dist, euclidean_dis(strip[i], strip[j]))
    return min_dist

def devide(points):             # O(nlogn)
    n = len(points)

    if n <= 3:
        return brute_force(points)

    mid = n // 2
    mid_point = points[mid]

    dl = devide(points[:mid])
    dr = devide(points[mid:])

    d = min(dl, dr)

    strip = []
    for p in points:
        if abs(p[0] - mid_point[0] < d):
            strip.append(p)

    return min(d, strip_closest(strip, d))

def closest(points):
    points.sort()               #O(n logn)
    return devide(points)


points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]



min_dis = closest(points)

print(min_dis)

