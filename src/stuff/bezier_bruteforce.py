from stuff.bezier_dividenconquer import Point
from math import comb

def nDegreeBruteForceBezier(points: list[Point]) :
    n = len(points) - 1
    t = 0.01
    ans = list()

    while t <= 0.99 :

        p = Point(0, 0)
        for i in range(n + 1) :
            p += (pow(t, i)) * (pow(1 - t, n - i)) * comb(n, i) * points[i]
        ans.append(p)
    
    return ans