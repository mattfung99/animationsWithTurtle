# \*********************************************************\

# To access drawing function, use 'turtle' library
import turtle 

# Let 'star' be the variable that manipulates the turtle pen
star = turtle.Pen() 

# \*********************************************************\

# Define functions

def forwardbackward():
    star.forward(150)
    star.backward(150)

def drawStar():
    star.forward(200)
    star.left(198)
    forwardbackward()
    star.right(36)
    forwardbackward()
    star.left(198)
    star.backward(200)
    star.forward(200)
    star.right(198)
    star.forward(150)
    star.right(72)
    star.forward(150)
    star.right(18)
    star.backward(200)

# \*********************************************************\

# \********************** Draw STAR3 ***********************\

# INITIALIZE
star.left(90)

# LOOP FOR STAR
for i in range(5):
    drawStar()

# \************************ End ****************************\

# \*********************************************************\
