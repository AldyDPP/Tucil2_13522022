from bezier_dividenconquer import Point
import matplotlib.pyplot as plt

def ui() -> str :

    print("-----------------------------------------")
    print("Hello, let's generate some Bezier Curves!")
    print("-----------------------------------------")
    print()
    print("Pick your method of input:")
    print("1. Direct (command line) input.")
    print("2. Text File input.")
    print("3. Give me a fun fact about Bezier Curves!")

    choice = input("(1/2/3): ")

    try :
        choice = int(choice)
        if choice not in [1,2,3] :
            raise ValueError
        else :
            return choice
    except ValueError: 
        print("Please input correctly.")

def cliinput() -> list[Point] :
    p = int(input("Input number of points: "))
    print("Point input format: x y")
    print("Example: 2.5 -6")
    print("---------------")

    try :
        points = list()
        for i in range(p) :
            x,y = map(float, input(f"Input point-{i+1}: ").split())
            points.append(Point(x,y))

        return points
    
    except ValueError :
        print("The x and y values for a point must be real numbers.")
        quit()

def txtinput() -> list[Point] :

    try :
        with open("input.txt", 'r') as f :

            points = list()
            
            t = f.readline().strip()

            if len(t) != 1 :
                raise IndexError
            
            t = int(t)

            for i in range(t) :

                line = f.readline().split()

                if len(line) != 2 :
                    raise IndexError
                
                x,y = map(int, line)
                points.append(Point(x,y))
            
            return points

    except ValueError :
        print("Failed to read from the txt file. Make sure the inputs are all real numbers!")
        quit()
    
    except IndexError :
        print("Failed to read from the txt file. Please recheck the input format.")
        quit()
    
    except FileNotFoundError :
        print("Couldn't find input.txt file. Perhaps you have moved/rename it?")
        quit()

def showgraph(points: list[Point], zf : int) -> None :

    xvals = [p.x for p in points]
    yvals = [p.y for p in points]
    plt.plot(xvals, yvals)
    plt.axis([-zf,zf,-zf,zf])
    plt.show()

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