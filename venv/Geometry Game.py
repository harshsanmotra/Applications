class Point:

    def __init__(self, x,y):
        self.x = x
        self.y = y
    def fall_in_rect(self,lowleft,upright):
        if lowleft[0] < self.x < upright[0]and lowleft[1] < self.y < upright[1]:



point1 = Point(10,20)

print(vars(point1))
print(type(point1))
