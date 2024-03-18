from bezier_dividenconquer import Point
from inputoutput import showgraph
from math import comb
from func_timing import timethis

@timethis

def nDegreeBruteForceBezier(points: list[Point], iterations) :
    n = len(points) - 1
    diff = 1 / (2 ** iterations)
    t = 0
    ans = list()

    while t <= 0.999 :

        p = Point(0, 0)
        for i in range(n + 1) :

            p += points[i] * (pow(t, i)) * (pow(1 - t, n - i)) * comb(n, i)
            
        ans.append(p)

        t += diff
    
    return ans

if __name__ == "__main__" :
    p0 = Point(0,0)
    p2 = Point(20,30)
    p3 = Point(0,30)
    p1 = Point(30,0)
    points = [p0,p2,p3,p1]
    points = nDegreeBruteForceBezier(points)
    showgraph(points, zf = 30)