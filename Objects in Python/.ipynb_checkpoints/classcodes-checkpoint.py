import math

class Point():
    
    def __init__(self,x=0,y=0):
        self.move(x,y)
    
    
    def reset(self):
        self.x = 0
        self.y = 0
        
    def move(self, x, y):
        '''Initialize the position of a new point. The x and y
        coordinates can be specified. If they are not, the
        point defaults to the origin.'''
        self.x = x
        self.y = y
   
    def calculate_distance(self, other_point):
        return math.sqrt(
        (self.x - other_point.x)**2 +
        (self.y - other_point.y)**2) 
    
def main():
    global point_mod
    point_mod = Point(10,6)
    print(point_mod.x, point_mod.y)
    
if __name__ == "__main__":
        main()
    
point_mod = None
