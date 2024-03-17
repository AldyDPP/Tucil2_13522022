import os
import sys

stuffdirectory = os.path.abspath(os.path.join(os.path.dirname(__file__), 'stuff\\'))
sys.path.append(stuffdirectory)

from stuff.bezier_dividenconquer import nDegreeBezier
from stuff.inputoutput import *

def main() :

    # Initialize
    os.system("cls" if os.name == "nt" else "clear")
    points = []
    
    # Input
    choice = ui()
    if choice == 1:
        points = cliinput()
    elif choice == 2:
        points = txtinput()
    elif choice == 3:
        funfact()
    
    # Solve
    result = nDegreeBezier(points, 10)

    # Output
    showgraph(result, 50)
    
main()