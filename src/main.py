import os
import sys

stuffdirectory = os.path.abspath(os.path.join(os.path.dirname(__file__), 'stuff\\'))
sys.path.append(stuffdirectory)

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
    
    # Solve - if you want to display time taken to calculate, use helper isntead of nDegreeBezier
    result = nDegreeBezier(points = points, iterations = t)
    # result = helper(points = points, iterations = t)

    # Output
    print("Enjoy your Bezier Curve!")
    showgraph(result, x1,x2,y1,y2)
    
main()