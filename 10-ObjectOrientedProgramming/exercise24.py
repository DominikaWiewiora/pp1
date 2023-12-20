class C:
    def __init__(self, points):
        self.points = points

    def m(self, n):
        count = 0
        for point in self.points:
            if point[0] > 0 and point[1] > 0:
                count += 1
                if count >= n:
                    return True
        return False

points = [[2, 3], [1, 8], [-6, 4], [3, -7]]
obj = C(points)
print(obj.m(2))  
print(obj.m(3))  
