from bezier_dividenconquer import plt,Point,quadraticBezier,nDegreeBezier

p0 = Point(0, 0)
p2 = Point(50, 200)
p3 = Point(100, 60)
p4 = Point(150, 150)
p5 = Point(200, 100)
p1 = Point(150, 60)
# ans = (quadraticBezier(p0, p2, p1, iterations = 1))
ans = (nDegreeBezier([p0, p2, p3, p4, p1], iterations = 5))
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