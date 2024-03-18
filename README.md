# Tucil2_13522022
Tugas Kecil 2 Mata Kuliah IF2211 Strategi Algoritma

## Project Description
This small project is an assignment for the course IF2211 "Strategi Algoritma" of ITB. The program is a Command Line Input (CLI) based program that allows the user to generate a Bezier Curve based on parameters that they can put in an input file. The program also aims to entertain the user with a dozen fun facts about Bezier Curves.

## Requirements
This program only requires `matplotlib` to display the Bezier Curve, so if you do not have it installed yet...
```
pip install matplotlib
```

## How To Run

Make sure to navigate to src folder, then just run with Python:

```
python3 main.py
```

## How To Use

1. When running the program, you are given 3 input options. Enter 1 to generate a Bezier Curve based on the input file. Enter 2 to get a link to  this help menu. Enter 3 to display a random fun fact about Bezier Curves. You can also not enter anything, which will by default move you to option 1.

2. In option 1, you will be prompted to enter a file name. You can leave this blank, in which case "input.txt" will be used by default. A Bezier Curve will be generated based on the parameters that you provide in the input file that you use. The input file must be directly inside either the `src` folder or the `test` folder

3. The following is the format for the input file. 
- The first line contains a single integer `p` which is the amount of _control points_ the Bezier Curve will have. 
- The following `p` lines each contain two real numbers x<sub>i</sub> and y<sub>i</sub> which are the x and y values of the i'th point.
- The next line contains a single integer `t` which describes how many _iterations_ will be calculated for the Bezier Curve. 
- The last line consists of 4 real numbers x<sub>1</sub>, x<sub>2</sub>, y<sub>1</sub>, and y<sub>2</sub>. These will be the parameters for displaying the graph. The graph will display the cartesian plane for the x axis in the range [x<sub>1</sub>, x<sub>2</sub>] and the y axis in the range [y<sub>1</sub>, y<sub>2</sub>].

4. Below is an example of the input file format. If the input file is not formatted accordingly, the program will display an error message and close.
```
4
-180 -200
-150 120
150 -160
180 200
12
-300 300 -300 300
```

5. The constraints for the input file are: p must be an integer larger than 1, x<sub>i</sub> and y<sub>i</sub> are real numbers, t must be a non negative integer, x<sub>1</sub> < x<sub>2</sub> and y<sub>1</sub> < y<sub>2</sub>. Inputs that do not fit these constraints will also cause the program to display an error message and close.
6. The first and last points will be the start and endpoints of the Bezier Curve respectively.
7. Make sure you check out all the fun facts about Bezier Curves!