from bezier_dividenconquer import plt,Point,quadraticBezier

p0 = Point(-30, 100)
p2 = Point(200, -200)
p1 = Point(150, 30)
ans = (quadraticBezier(p0, p2, p1, iterations = 15))
xvals = [p.x for p in ans]
yvals = [p.y for p in ans]
plt.plot(xvals, yvals)
plt.axis([
    -200, 
    200, 
    -200, 
    200
])
plt.show()