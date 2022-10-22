import math


class Distance :
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def compute_distance (self) :
        distane = math.dist([self.x1, self.x2], [self.y1, self.y2])
        return distane

testing = Distance(2, 5, -4, -9)
result = testing.compute_distance()
print(result)
