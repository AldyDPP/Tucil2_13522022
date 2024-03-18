import os
import sys

stuffdirectory = os.path.abspath(os.path.join(os.path.dirname(__file__), 'stuff\\'))
testdirectory = os.path.abspath(os.path.join(os.path.curdir, os.path.pardir))
sys.path.append(stuffdirectory)

from stuff.bezier_bruteforce import nDegreeBruteForceBezier
from stuff.bezier_dividenconquer import nDegreeBezier, helper
from stuff.inputoutput import *

def cls() :
    os.system("cls" if os.name == "nt" else "clear")

def main() :

    # Initialize
    cls()
    points = []
    
    # Input
    choice = ui()
    if choice == 1:
        p,points,t,x1,x2,y1,y2 = txtinput()

    elif choice == 2:
        printhelp()

    elif choice == 3:
        funfact()
    
    # Solve
    result = nDegreeBezier(points = points, iterations = t)

    # For benchmarking the time taken for Brute force and DnC 
    # result = helper(points = points, iterations = t)
    # result = nDegreeBruteForceBezier(points, iterations = t)

    # Output
    print("Enjoy your Bezier Curve!")
    showgraph(result, x1,x2,y1,y2, controls=points)
    
main()