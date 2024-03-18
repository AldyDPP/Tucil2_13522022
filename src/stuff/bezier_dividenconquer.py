from dataclasses import dataclass
from func_timing import timethis

@dataclass
class Point :

    x : float
    y : float

    def __add__(self, other) :
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other) :
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, k: float) :
        return Point(self.x * k, self.y * k)
    
    def __truediv__(self, k: float) :
        return Point(self.x / k, self.y / k)
    
    def __str__(self) :
        return f"({self.x}, {self.y})"

def midpoint(p1: Point, p2: Point) -> Point :
    return (p1 + p2) / 2

def weightedpoint(p1: Point, p2: Point, t: float) -> Point :
    return (p1 * t) + (p2 * (1 - t))


""" Main Alg """
def quadraticBezier(p0, p2, p1, iterations: int) -> list[Point]:
    # p2 is control point

    if iterations == 0 :
        return [p0,p2,p1]
    
    elif iterations == 1 : 
        q0 = midpoint(p0, p2)
        q1 = midpoint(p2, p1)
        r0 = midpoint(q0, q1)
        return [p0,r0,p1]

    else :
        p02 = midpoint(p0, p2)
        p21 = midpoint(p2, p1)
        r0 = midpoint(p02, p21)
        
        # divide and conquer
        l = (quadraticBezier(p0, p02, r0, iterations - 1))[:-1]
        m = [r0]
        r = (quadraticBezier(r0, p21, p1, iterations - 1))[1:]
        
        return l + m + r

def nDegreeBezier(points: list[Point], iterations: int) -> list[Point] :

    if iterations == 0 :
        return points
    
    elif iterations == 1 :

        prev_points = points.copy()
        for i in range(len(points) - 1) :
            new_points = list()
            for j in range(1, len(prev_points)) :
                new_points.append(midpoint(prev_points[j], prev_points[j-1]))
            prev_points = new_points

        p0 = points[0]
        r0 = prev_points[0]
        p1 = points[-1]

        return [p0,r0,p1]
    
    else :

        p0 = points[0]
        p1 = points[-1]

        left_points = [p0]
        right_points = [p1]

        # Process all bezier points up to nth degree
        prev_points = points.copy()
        for i in range(len(points) - 1) :
            new_points = list()
            for j in range(1, len(prev_points)) :
                new_points.append(midpoint(prev_points[j], prev_points[j-1]))

            left_points.append(new_points[0])
            right_points.append(new_points[-1])
            
            prev_points = new_points

        right_points.reverse()
        r0 = prev_points[0]
        
        # divide and conquer
        l = nDegreeBezier(left_points, iterations - 1)[:-1]
        m = [r0]
        r = nDegreeBezier(right_points, iterations - 1)[1:]
        
        return l + m + r

# Because nDegreeBezier is a recursive function, a helper is needed to time it from start to end
@timethis
def helper(points: list[Point], iterations: int) :
    return nDegreeBezier(points, iterations)