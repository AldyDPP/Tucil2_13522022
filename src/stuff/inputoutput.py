from bezier_dividenconquer import Point
import matplotlib.pyplot as plt

def ui() -> str :

    print("-------------------------------------------")
    print("Hello, this program is about Bezier Curves!")
    print("-------------------------------------------")
    print()
    print("What would you like to do?")
    print("1. Generate a Bezier Curve from input file.")
    print("2. Help.")
    print("3. Give me a fun fact about Bezier Curves!")

    choice = input("(1/2/3): ")
    if not choice : return 1

    try :
        choice = int(choice)
        if choice not in [1,2,3] :
            raise ValueError
        else :
            return choice
        
    except ValueError: 
        print("Please input correctly.")
        quit()

def txtinput() -> list[Point] :

    filename = input("Input filename (you can leave this blank to default to \"input.txt\"): ")
    filename = filename if filename else "input.txt"
    error = ""
    try :
        with open(filename, 'r') as f :

            points = list()
            
            p = f.readline().split()

            if len(p) != 1 :
                error = "Wrong format at line 1. Make sure the amount of points is a positive integer larger than 1."
                raise ValueError
            
            try :
                p = int(p[0])
            except ValueError :
                error = "Wrong format at line 1. Make sure you have put in an integer."
                raise ValueError

            for i in range(p) :

                line = f.readline().split()

                if len(line) != 2 :
                    error = f"Wrong format at line {2 + i}. Make sure you put in exactly two real numbers for each point."
                    raise ValueError
                
                try :
                    x,y = map(float, line)
                    points.append(Point(x,y))
                except ValueError :
                    error =  f"Wrong format at line {2 + i}. Make sure you have put in real values."
                    raise ValueError
            
            t = f.readline().split()
            if len(t) != 1 :
                error = f"Wrong format at line {p + 2}. Make sure the iteration count is a non negative integer."
                raise ValueError
            
            try :
                t = int(t[0])
            except ValueError :
                error = f"Wrong format at line {p + 2}. Make sure you have put in a non negative integer."
                raise ValueError

            x1,x2,y1,y2 = 0,0,0,0
            try :
                x1,x2,y1,y2 = map(float, f.readline().split())
                if x1 >= x2 or y1 >= y2 :
                    raise ValueError
                
            except ValueError:
                error = f"Wrong format at line {p + 3}. Make sure the last line contains 4 real numbers x1 x2 y1 y2, where x1 < x2 and y1 < y2"
                raise ValueError

            return p,points,t,x1,x2,y1,y2
        
    except ValueError :
        print("Failed to read from input file.")
        print(error)
        print()
        quit()
    
    except FileNotFoundError :
        error = "Couldn't find the file. Perhaps you have moved/renamed it?"
        print(error)
        print()
        quit()

def showgraph(points, x1,x2,y1,y2, controls) :

    x = [p.x for p in points]
    y = [p.y for p in points]
    
    plt.plot(x, y)
    plt.axis([x1,x2,y1,y2])

    x = [p.x for p in controls]
    y = [p.y for p in controls]
    plt.scatter(x,y, color = "red")

    plt.show()

def printhelp() :
    print("Refer to the following link on how to use this program.")
    print("https://github.com/AldyDPP/Tucil2_13522022#How-To-Use")
    print()
    quit()

def funfact() -> None :

    facts = [

        "Bezier is a French name, the correct pronunciation is beh-zee-ay.",

        "Pierre Bezier was not the first to invent them, though he did discover them on his own.",

        "Bezier Curves can be used to model the speed-time relationship of an object. This can, for example, allow animators to easily control the movement speed of that object.",

        "Bezier Curves use only (for the most part) highschool level math.",

        "Pierre Bezier was imprisoned during World War II.",

        "Bezier Curves, along with Bezier Surfaces and Coons Patches, were some of the most major breakthroughs in Computer Aided Geometric Design (CAGD or CAD). CAGD became a discipline in its own right after the 1974 conference at the University of Utah.",

        "You can get a \"Bezier Award\" from the Solid Modelling Association (SMA) if you make long lasting contributions to Solid, Geometric, or Physical Modeling in their Applications.",

        "I was going to put the formula for finding the length of a quadratic Bezier Curve as a fun fact. I changed my mind because it was too long and I was lazy...",

        "There is a study in 2018 by Walter Fierz that discusses the applications of Bezier Curves for calculating likelihood ratios for Alzheimer's Disease.",

        "These fun facts were sponsored by Raid Bezier Legends. Use code \"DIVIDENCONQUER\" on the special link in the ReadMe to get 50,000 silver and a free epic Bezier Surface as part of the new player program! (this is a joke)",

        "Bezier Curves are used for designing custom slider objects in the popular rhythm game Osu!", 

        "There are various studies that use Bezier Curves to model fruits, such as apples, lemons, and oranges. These can apparently be used to design post-harvest equipment (among other things).",

        "Have you ever used the curved line tool in Microsoft Paint? Spoilers: it's a Bezier Curve!",
        
    ]

    i = 0
    with open("stuff\\index.txt", 'r') as f :
        i = int(f.read())

    with open("stuff\\index.txt", 'w') as f :
        f.write(str((i + 1) % 13))
    
    print()
    print(facts[i])
    print()

    """
    Sources.

    https://pomax.github.io/bezierinfo/#catmullconv (general info)
    http://solidmodeling.org/awards/bezier-award/ (Bezier award)
    https://www.conceptcarz.com/view/makehistory/127%2C0/Renault_History.aspx (more on Pierre Bezier)
    https://github.com/ppy/osu/issues/5845 (bezier curves in osu!)

    "Curves and Surfaces for Computer Aided Geometric Design A Practical Guide Third Edition" by Gerald Farin

    "Application of Bézier Curves for Calculating Likelihood Ratios for Plasma Amyloid-β Biomarkers for Alzheimer's Disease" by Walfer Fierz

    "Geometric Modeling of the Valencia Orange (Citrus sinensis L.) by Applying Bézier Curves and an Image-Based CAD Approach" by Hector A. Tinoco, Daniel R. Barco, Olga Ocampo, and Jaime Buitrago-Osorio

    """
    
    quit()