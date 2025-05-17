
"""
Pygame is a free and open-source, cross-platform Python library designed for creating multimedia applications
like video games. It's built on top of the Simple DirectMedia Layer (SDL) library, providing a high-level
interface to manage graphics, sound, and user input. Pygame abstracts away many low-level details, making
game development more accessible without needing extensive knowledge of C or lower-level programming.

To start using Pygame, it needs to be installed first. This can be done using pip, Python's package installer,
 with the command pip install pygame. After installing, a basic Pygame program typically involves initializing
  Pygame, creating a display window, handling events (like key presses or mouse clicks), and drawing elements
  on the screen. The main loop of the game continuously updates the display to reflect changes, creating the
  animation effect. Pygame focuses on 2D game development, utilizing shapes and sprites. While it doesn't have
  built-in UI or level design tools, it provides the necessary components to build them from scratch.

Pygame is a set of Python modules designed for writing video games. It adds functionality on top of the
excellent SDL library, enabling you to create fully-featured games and multimedia programs in the Python
language. It’s key benefits include:

Beginner-Friendly: Simple Python syntax makes it ideal for newcomers.
Active Community: Rich with tutorials, examples and global support.
Cross-Platform: Works on Windows, Mac and Linux.
Versatile: Suitable for games, simulations and interactive apps.
Free & Open Source: No cost, no restrictions.
Installing Pygame
Pygame requires Python 3.6.1 or later, as newer versions are more beginner-friendly and offer improved performance.
 If you don’t have Python installed, download it from python.org.

To install Pygame, use the following command:

python3 -m pip install -U pygame –user


After installation, verify if it works by running a built-in example:

python3 -m pygame.examples.aliens


If the game launches successfully, you are ready to start using Pygame!

Creating your first pygame program
Once Pygame is installed, let’s create a simple program that displays four squares on the screen.

Importing Pygame Modules
# Import the pygame module


import pygame





# Import constants for easier access to key events


from pygame.locals import *


Before using any Pygame functionality, we need to import its modules.

Understanding key pygame concepts
Sprite: A 2D object (like our square) displayed on the screen.
Surface: A canvas for drawing (even the screen is a Surface).
Rect: A rectangle object for positioning and collisions.
Implementation code:

import pygame
from pygame.locals import *

class Sq(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0, 200, 255))

pygame.init()  # Init Pygame
win = pygame.display.set_mode((800, 600)) # Game window 800x600

# Create 4 squares
s1, s2, s3, s4 = Sq(), Sq(), Sq(), Sq()

# Game loop
run = True
while run:
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_BACKSPACE):
            run = False

    # Draw squares in corners
    win.blit(s1.surf, (40, 40))
    win.blit(s2.surf, (40, 530))
    win.blit(s3.surf, (730, 40))
    win.blit(s4.surf, (730, 530))

    pygame.display.flip()
Output


Explanation:

Sq class creates a 25×25 light blue square sprite in Pygame by extending pygame.sprite.Sprite, initializing the
 parent class, and filling the surface with color (0, 200, 255).
pygame.event.get() handles all incoming events. If the event type is QUIT, the game exits when the window close
 button is clicked. Similarly, if a KEYDOWN event occurs and the Backspace key is pressed (e.key == pygame.K_BACKSPACE)
 , the game will exit.
win.blit(s1.surf, (40, 40)) draws square 1 at the top-left, s2 at the bottom-left, s3 at the top-right and s4 at
the bottom-right.
pygame.display.flip() updates the screen to show the drawn squares.
Catch the falling blocks mini game
Let’s create a simple, real game where a player-controlled paddle catches falling blocks. Its features include:

Move the paddle left/right using the arrow keys.
Catch falling blocks to earn points.
Game Over if a block hits the ground.

import pygame
import random
import sys

pygame.init() # Init pygame
W, H = 600, 600 # Screen setup

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Catch the Falling Blocks")

WHT, BLU, RED, BLK = (255, 255, 255), (0, 200, 255), (255, 0, 0), (0, 0, 0) # Colors

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Paddle and block
paddle = pygame.Rect(W // 2 - 60, H - 20, 120, 10)
block = pygame.Rect(random.randint(0, W - 20), 0, 20, 20)
b_speed = 5

score = 0 # Score

# Game loop
run = True
while run:
    screen.fill(BLK)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-8, 0)
    if keys[pygame.K_RIGHT] and paddle.right < W:
        paddle.move_ip(8, 0)

    # Move block
    block.y += b_speed

    # Block caught
    if block.colliderect(paddle):
        block.y = 0
        block.x = random.randint(0, W - 20)
        score += 1
        b_speed += 0.5  # Speed up

    # Block missed
    if block.y > H:
        game_over = font.render(f"Game Over! Final Score: {score}", True, RED)
        screen.blit(game_over, (W // 2 - 150, H // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        run = False

    # Draw objects
    pygame.draw.rect(screen, WHT, paddle)
    pygame.draw.rect(screen, BLU, block)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHT)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
Output

Output
Catching falling blocks game

Explanation:

pygame.Rect(…) used to define rectangular shapes like the paddle and block. The first two values are the
top-left (x, y) position, followed by width and height.
paddle.move_ip(x, y) moves the paddle in-place by given values.
block.colliderect(paddle) checks for collision between block and paddle. If True, the block is “caught”.
score & b_speed score is increased by 1 on each catch and the block speed increases, making the game
progressively harder.
pygame.display.flip() updates the entire screen with any changes made e.g., moving paddle or falling block.
clock.tick(60) keeps the game running at 60 frames per second for smooth movement

"""
"""
Pygame – Drawing Objects and Shapes
Last Updated : 31 Oct, 2021
In this article, we are going to see how to draw an object using Pygame. There can be two versions for drawing any shape, it can be a solid one or just an outline of it.

Drawing Objects and Shapes in PyGame
You can easily draw basic shapes in pygame using the draw method of pygame. 

Drawing Rectangle shape: 
To draw a rectangle in your pygame project you can use draw.rect() function.



Syntax: pygame.draw.rect(surface, color, rect, width)





Parameters:



surface :- Here we can pass the surface on which we want to draw our rectangle. In the above example, we created a surface object named ‘window’.
color :- Here we can pass the color for our rectangle. We are using blue color in our example.
rect :- Here we can pass the rectangle, position, and dimensions.
width :- Here we can pass the line thickness. we can also create a solid rectangle by changing the value of this width parameter. So let’s look at that.
First, import the required module and initialize pygame. Now, Create the surface object of a specific dimension using the display.set_mode() method of pygame. Fill the background of the surface object with white color using the fill() function of pygame. Create a rectangle using the draw.rect() method of pygame. Update the Surface object.

Example 1: Drawing outlined rectangle using pygame.

 
# Importing pygame module
import pygame
from pygame.locals import *
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
 
# Fill the scree with white color
window.fill((255, 255, 255))
 
# Using draw.rect module of
# pygame to draw the outlined rectangle
pygame.draw.rect(window, (0, 0, 255), 
                 [100, 100, 400, 100], 2)
 
# Draws the surface object to the screen.
pygame.display.update()
Output :


We can create a solid rectangle by setting the width parameter equal to 0 and the rest of the approach remains the same.

Example 2: Drawing a solid rectangle.

 
# Importing pygame module
import pygame
from pygame.locals import *
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
 
# Fill the scree with white color
window.fill((255, 255, 255))
 
# Using draw.rect module of
# pygame to draw the solid rectangle
pygame.draw.rect(window, (0,   0, 255),
                 [100, 100, 400, 100], 0)
 
# Draws the surface object to the screen.
pygame.display.update()
Output :


Drawing Circle Shape:
To draw a circle in your pygame project you can use draw.circle() function. The entire approach is the same as above only the function and parameters are changed accordingly.



Syntax : pygame.draw.circle(surface, color, center, radius, width)





Parameters :



surface :- Here we can pass the surface on which we want to draw our circle. In the above example, we created a surface object named ‘window’.
color :- Here we can pass the color for our circle. We are using green color in our example.
center :- Here we can pass the ( x, y ) coordinates for the center of the circle.
radius :- Here we can pass the radius of our circle.
width :- Here we can pass the line thickness. we can also create a solid circle by changing the value of this width parameter. So let’s look at that.
Example 1: Drawing a hollow circle.

 
# Importing pygame module
import pygame
from pygame.locals import *
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
 
# Fill the scree with white color
window.fill((255, 255, 255))
 
# Using draw.rect module of
# pygame to draw the solid circle
pygame.draw.circle(window, (0, 255, 0), 
                   [300, 300], 170, 3)
 
# Draws the surface object to the screen.
pygame.display.update()
Output :


We can create a solid circle by setting the width parameter equal to 0. 

Example 2: drawing a solid circle

 
# Importing pygame module
import pygame
from pygame.locals import *
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
 
# Fill the scree with white color
window.fill((255, 255, 255))
 
# Using draw.rect module of
# pygame to draw the solid circle
pygame.draw.circle(window, (0, 255, 0),
                   [300, 300], 170, 0)
 
# Draws the surface object to the screen.
pygame.display.update()
Output :


Similarly, you can draw other basic shapes using the draw module of pygame. 

Drawing Polygon Shape:
The desired polygon can be drawn using polygon() function. 



Syntax: polygon(surface, color, points, width)



Again the approach remains the same only the function and the parameters change.

Example 1: drawing a solid polygon

 
# Importing pygame module
import pygame
from pygame.locals import *
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
 
# Fill the scree with white color
window.fill((255, 255, 255))
 
# Using draw.rect module of
# pygame to draw the outlined polygon
pygame.draw.polygon(window, (255, 0, 0), 
                    [[300, 300], [100, 400],
                     [100, 300]])
 
# Draws the surface object to the screen.
pygame.display.update()
Output :


Example 2: Drawing a hollow polygon

 
# Importing pygame module
import pygame
from pygame.locals import *
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
 
# Fill the scree with white color
window.fill((255, 255, 255))
 
# Using draw.rect module of
# pygame to draw the outlined polygon
pygame.draw.polygon(window, (255, 0, 0), 
                    [[300, 300], [100, 400],
                     [100, 300]], 5)
 
# Draws the surface object to the screen.
pygame.display.update()
Output:


Drawing Line Shape:
A line is the most basic drawing entity and can be drawn in pygame using line() function.



Syntax : pygame.draw.line(surface, color, start_pos, end_pos, width)



Example 1: drawing a line

 
# Importing pygame module
import pygame
from pygame.locals import *
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
 
# Fill the scree with white color
window.fill((255, 255, 255))
 
# Using draw.rect module of
# pygame to draw the line
pygame.draw.line(window, (0, 0, 0), 
                 [100, 300], 
                 [500, 300], 5)
 
# Draws the surface object to the screen.
pygame.display.update()
Output:


Draw Multiple Shapes:
You can draw multiple shapes on the same surface object. For that, the first required modules are imported and pygame is initialized. Now, create the surface object of a specific dimension using the display.set_mode() method of pygame. Fill the background of the surface object with white color using the fill() function of pygame. Create required shapes are described above. Update the Surface object

Example 1: Drawing a circle inside a rectangle.

 
# Importing pygame module
import pygame
from pygame.locals import *
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
 
# Fill the scree with white color
window.fill((255, 255, 255))
 
# Using draw.rect module of
# pygame to draw the rectangle
pygame.draw.rect(window, (0, 0, 255),
                 [50, 200, 500, 200])
 
# Using draw.rect module of
# pygame to draw the circle inside the rectangle
pygame.draw.circle(window, (0, 255, 0),
                   [300, 300], 100)
 
# Draws the surface object to the screen.
pygame.display.update()
Output:


Example 2: Drawing rectangles inside one another.

 
# Importing pygame module
import pygame
from pygame.locals import *
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
 
# Fill the scree with white color
window.fill((255, 255, 255))
 
# Creating a list of different rects
rectangle_list = [pygame.Rect(50, 100, 500, 200),
                  pygame.Rect(70, 120, 460, 160),
                  pygame.Rect(90, 140, 420, 120),
                  pygame.Rect(110, 160, 380, 80),
                  pygame.Rect(130, 180, 340, 40)
                  ]
 
# Creating list of different colors
color_list = [(0,   0,   0),
              (255, 255, 255),
              (0,   0, 255),
              (0, 255,   0),
              (255,   0,   0)
              ]
 
# Creating a variable which we will use
# to iterate over the color_list
color_var = 0
 
# Iterating over the rectangle_list using
# for loop
for rectangle in rectangle_list:
 
    # Drawing the rectangle 
    # using the draw.rect() method
    pygame.draw.rect(window, color_list[color_var],
                     rectangle)
 
    # Increasing the value of color_var
    # by 1 after every iteration
    color_var += 1
 
# Draws the surface object to the screen.
pygame.display.update()
Output :


Writing your own drawing functions:
You can easily create your own specialized drawing functions in pygame. 

This can be done by following the given procedure. Create a drawing function that will take starting position, width, and height as parameters. Draw required shapes are described above. Call the drawfunction()

 
# Importing pygame module
import pygame
from pygame.locals import *
 
# Creating Drawing function
 
 
def drawingfunction(x, y, width, height):
 
    # Creating rectangle using the draw.rect() method
    pygame.draw.rect(window, (0, 0, 255), [x, y, width, height])
 
    # Calculation the center of the circle
    circle_x = width/2 + x
    circle_y = height/2 + y
 
    # Calculating the radius of the circle
    if height < width:
        radius = height/2
    else:
        radius = width/2
 
    # Drawing the circle
    pygame.draw.circle(window, (0, 255, 0), [circle_x, circle_y], radius)
 
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
 
# Fill the scree with white color
window.fill((255, 255, 255))
 
# Calling the drawing function
drawingfunction(50, 200, 500, 200)
 
# Draws the surface object to the screen.
pygame.display.update()
Output:


Drawing shapes with the mouse:
Now let’s see how we can create shapes whenever the user clicks the mouse. We are going to create circles in the next example but you can create any shape you want.

Create a list to store the position of the shape to be drawn. Create a variable to store the color of the shape. Create a variable which we will use to run the while loop and Create a while loop. Iterate over all the events received from pygame.event.get(). If the type of the event is quit then setting the run variable to false. If the type of the event is MOUSEBUTTONDOWN ( this event occurs when a user presses the mouse button) then getting the current position in a variable then appending that position in our circle_positions list. Iterate over all the positions in of the array created using a for a loop. Keep drawing the shape. Update the surface object.

 
# Importing pygame module
import pygame
from pygame.locals import *
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
 
# Fill the scree with white color
window.fill((255, 255, 255))
 
# creating list in which we will store
# the position of the circle
circle_positions = []
 
# radius of the circle
circle_radius = 60
 
# Color of the circle
color = (0, 0, 255)
 
# Creating a variable which we will use
# to run the while loop
run = True
 
# Creating a while loop
while run:
 
    # Iterating over all the events received from
    # pygame.event.get()
    for event in pygame.event.get():
 
        # If the type of the event is quit
        # then setting the run variable to false
        if event.type == QUIT:
            run = False
 
        # if the type of the event is MOUSEBUTTONDOWN
        # then storing the current position
        elif event.type == MOUSEBUTTONDOWN:
            position = event.pos
            circle_positions.append(position)
             
    # Using for loop to iterate
    # over the circle_positions
    # list
    for position in circle_positions:
 
        # Drawing the circle
        pygame.draw.circle(window, color, position,
                           circle_radius)
 
    # Draws the surface object to the screen.
    pygame.display.update()

"""
"""

Python | Drawing different shapes on PyGame window
Last Updated : 14 Jan, 2019
Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language. Now, it’s up to the imagination or necessity of developer, what type of game he/she wants to develop using this toolkit.

Command to install pygame :

pip install pygame
There are four basic steps to displaying images on the pygame window :

Create a display surface object using display.set_mode() method of pygame.
Completely fill the surface object with white using fill() method of pygame display surface object.
Drawing different shapes onto a surface object using Primitive Drawing Functions of pygame.
Show the display surface object on the pygame window using display.update() method of pygame.
Below is the implementation:




# import pygame module in this program 
import pygame 
  
# activate the pygame library . 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init() 
  
# define the RGB value 
# for white, green, 
# blue, black, red 
# colour respectively. 
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
black = (0, 0, 0) 
red = (255, 0, 0) 
  
# assigning values to X and Y variable 
X = 400
Y = 400
  
# create the display surface object 
# of specific dimension..e(X,Y). 
display_surface = pygame.display.set_mode((X, Y )) 
  
# set the pygame window name 
pygame.display.set_caption('Drawing') 
  
# completely fill the surface object  
# with white colour  
display_surface.fill(white) 
  
# draw a polygon using draw.polygon() 
# method of pygame. 
# pygame.draw.polygon(surface, color, pointlist, thickness) 
# thickness of line parameter is optional. 
pygame.draw.polygon(display_surface, blue, 
                    [(146, 0), (291, 106), 
                    (236, 277), (56, 277), (0, 106)]) 
                      
# draw a line using draw.line() 
# method of pygame. 
# pygame.draw.line(surface, color, 
# start point, end point, thickness)  
pygame.draw.line(display_surface, green, 
                (60, 300), (120, 300), 4) 
  
# draw a circle using draw.circle() 
# method of pygame. 
# pygame.draw.circle(surface, color, 
# center point, radius, thickness)  
pygame.draw.circle(display_surface, 
           green, (300, 50), 20, 0) 
  
# draw a ellipse using draw.ellipse() 
# method of pygame. 
# pygame.draw.ellipse(surface, color, 
# bounding rectangle, thickness)  
pygame.draw.ellipse(display_surface, black, 
                    (300, 250, 40, 80), 1) 
  
# draw a rectangle using draw.rect() 
# method of pygame. 
# pygame.draw.rect(surface, color, 
# rectangle tuple, thickness) 
# thickness of line parameter is optional. 
pygame.draw.rect(display_surface, black, 
                    (150, 300, 100, 50)) 
  
# infinite loop 
while True : 
      
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get() : 
  
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
  
            # deactivates the pygame library 
            pygame.quit() 
  
            # quit the program. 
            quit() 
  
        # Draws the surface object to the screen.  
        pygame.display.update()  

"""


"""

Pygame – surface.blit() function
Last Updated : 23 May, 2021
surface.blit() function draws a source Surface onto this Surface. The draw can be positioned with the dest 
argument. The dest argument can either be a pair of coordinates representing the position of the upper left
 corner of the blit or a Rect, where the upper left corner of the rectangle will be used as the position for
  the blit. The size of the destination rectangle does not affect the blit.



Syntax : blit(source, dest, area=None, special_flags=0) -> Rect





Parameters:



Source – Draws a source Surface onto this Surface
dest – The draw can be positioned with the dest argument.
area -A Rect can also be passed as the destination and the topleft corner of the rectangle will be used as 
the position for the blit
 
# import pygame module 
import  pygame 
  
pygame.init() 
  
# width 
width = 680
  
# height 
height = 480
  
#store he screen size 
z = [width,height] 
  
# store the color 
white = (255, 255, 255) 
screen_display = pygame.display 
  
# Set caption of screen 
screen_display.set_caption('GEEKSFORGEEKS') 
  
# setting the size of the window 
surface = screen_display.set_mode(z) 
  
# set the image which to be displayed on screen 
python = pygame.image.load('bg.jpg') 
  
# set window true 
window = True
while window: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            window = False
              
            # display white on screen other than image 
    surface.fill(white) 
      
# draw on image onto another 
    surface.blit(python,(50, 50)) 
    screen_display.update() 
  
pygame.quit() 
"""
"""
Pygame – Control Sprites
Last Updated : 31 Jan, 2022
In this article, we will discuss how to control the sprite, like moving forward, backward, slow, or accelerate, and some of the properties that sprite should have. We will be adding event handlers to our program to respond to keystroke events, when the player uses the arrow keys on the keyboard we will call our pure methods to move the object on the screen.

Functions Used
moveRight(): This method takes argument pixels, which means how many pixels an object should be moved in the right direction. It is basically adding pixels to the current x coordinate of the object.
moveLeft(): This method takes argument pixels, which means how many pixels an object should be moved in the left direction. It is basically subtracting pixels to the current x coordinate of the object.
moveForward(): This method takes an argument speed, which means by how many factors the speed will increase. It is basically increasing speed with the factor of n in the y-direction of the object.
moveBackward(): This method takes an argument speed, which means by how many factors the speed will decrease. It is basically decreasing speed with the factor of n in the y-direction of the object.
Let us first look at the implementation of a Sprite class, which helps us create an object on our PyGame surface, and along with added 4 methods that will help us move forward, backward, right, and left.

Example: Sprite class

 
import pygame
 
# GLOBAL VARIABLES
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500
 
# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)
 
        pygame.draw.rect(self.image,
                         color,
                         pygame.Rect(0, 0, width, height))
 
        self.rect = self.image.get_rect()
 
    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
 
    def moveForward(self, speed):
        self.rect.y += speed * speed/10
 
    def moveBack(self, speed):
        self.rect.y -= speed * speed/10
Now we will see how we have control of our main program loop to handle the sprites. The first part of the loop will respond to the events such as interactions when the user uses the mouse or the keyboard. Later, on above methods for event handling on our object will be taken care of. Each event handler will call the relevant method from the Sprite class.

In this piece of code, we have control of our object, i.e., our object is an object as per our given directions, if we press the right arrow key, it will move in that direction and the same with all the arrow keys. Here, we use pygame.KEYDOWN method to initialize the method to use the arrow keys for controlling the objects, later on, we have to control the respective method to trigger the specific key to perform the certain action.

For instance, if we have a right arrow key, we have to call pygame.K_RIGHT method to move towards right in the direction of the object, and similar for pygame.K_DOWN method which is used for the move up in the direction of the object.

Example: Controlling sprite 

 
import random
import pygame
 
# Global Variables
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500
 
# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)
 
        pygame.draw.rect(self.image,
                         color,
                         pygame.Rect(0, 0, width, height))
 
        self.rect = self.image.get_rect()
 
    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
 
    def moveForward(self, speed):
        self.rect.y += speed * speed/10
 
    def moveBack(self, speed):
        self.rect.y -= speed * speed/10
 
 
pygame.init()
 
 
RED = (255, 0, 0)
 
 
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")
 
 
all_sprites_list = pygame.sprite.Group()
 
playerCar = Sprite(RED, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300
 
 
all_sprites_list.add(playerCar)
 
exit = True
clock = pygame.time.Clock()
 
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(10)
    if keys[pygame.K_DOWN]:
        playerCar.moveForward(10)
    if keys[pygame.K_UP]:
        playerCar.moveBack(10)
 
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()

"""


"""
Pygame – Creating Sprites
Last Updated : 28 Jul, 2021
Sprites are objects, with different properties like height, width, color, etc., and methods like moving right, left, up and down, jump, etc. In this article, we are looking to create an object in which users can control that object and move it forward, backward, up, and down using arrow keys.

Let first look at our first-class i.e., the class in which our sprite is defined, we will call that class Sprite. This Sprite class defines its positions(x and y coordinates), dimension of an object, color, etc. First, we will be calling our __init__() method. It is called a constructor for a class.

Example: Creating Sprite class

 
import pygame 
  
# GLOBAL VARIABLES 
COLOR = (255, 100, 98) 
SURFACE_COLOR = (167, 255, 100) 
WIDTH = 500
HEIGHT = 500
  
# Object class 
class Sprite(pygame.sprite.Sprite): 
    def __init__(self, color, height, width): 
        super().__init__() 
  
        self.image = pygame.Surface([width, height]) 
        self.image.fill(SURFACE_COLOR) 
        self.image.set_colorkey(COLOR) 
  
        pygame.draw.rect(self.image, 
                         color, 
                         pygame.Rect(0, 0, width, height)) 
  
        self.rect = self.image.get_rect() 
Now, that the class has been created, we can create objects from the class. It enables us to create as many objects as we need using the same class. Now we will create an object using our Class Sprite. 

Syntax:



object = Sprite(RED,WIDTH,HEIGHT)



By default, the object will be on position (0,0) i.e., top-left of the screen. We can change the x and y properties of the object.

Syntax:



object.rect.x = value





object.rect.y = value



We can define n of sprites that we want to create, but for the purpose of understanding, let’s simplify. Here we have created a rectangle sprite of certain dimensions, on which we can perform different operations to perform on sprites like move forward, backward, jump, slow, accelerate, etc. 

Example: Creating sprite

 
import pygame 
import random 
  
# GLOBAL VARIABLES 
COLOR = (255, 100, 98) 
SURFACE_COLOR = (167, 255, 100) 
WIDTH = 500
HEIGHT = 500
  
# Object class 
class Sprite(pygame.sprite.Sprite): 
    def __init__(self, color, height, width): 
        super().__init__() 
  
        self.image = pygame.Surface([width, height]) 
        self.image.fill(SURFACE_COLOR) 
        self.image.set_colorkey(COLOR) 
  
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height)) 
  
        self.rect = self.image.get_rect() 
  
  
pygame.init() 
  
RED = (255, 0, 0) 
  
size = (WIDTH, HEIGHT) 
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Creating Sprite") 
  
all_sprites_list = pygame.sprite.Group() 
  
object_ = Sprite(RED, 20, 30) 
object_.rect.x = 200
object_.rect.y = 300
  
all_sprites_list.add(object_) 
  
exit = True
clock = pygame.time.Clock() 
  
while exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = False
  
    all_sprites_list.update() 
    screen.fill(SURFACE_COLOR) 
    all_sprites_list.draw(screen) 
    pygame.display.flip() 
    clock.tick(60) 
  
pygame.quit() 

"""

"""
Moving an object in PyGame – Python
Last Updated : 11 Apr, 2025
To make a game or animation in Python using PyGame, moving an object on the screen is one of the first things to learn. We will see how to move an object such that it moves horizontally when pressing the right arrow key or left arrow key on the keyboard and it moves vertically when pressing up arrow key or down arrow key. We’ll create a game window, draw an object and update its position based on user input.

Change in Co-ordinates for respective keys pressed:


Left arrow key: Decrement in x co-ordinate
Right arrow key: Increment in x co-ordinate
Up arrow key: Decrement in y co-ordinate
Down arrow key: Increment in y co-ordinate


Setting Up PyGame
Before starting, make sure PyGame is installed. We can install it using:


pip install pygame


Example: Moving a Rectangle
In this code, we create a window using PyGame and draw a rectangle on the screen. The rectangle can be moved using the arrow keys and its position updates as we press the keys. This helps in learning how to handle movement and user input in PyGame.

[GFGTABS]
Python


import pygame 
pygame.init() 

win = pygame.display.set_mode((500, 500)) 
pygame.display.set_caption("Moving rectangle") 

x = 200
y = 200

width = 20
height = 20

vel = 10
run = True

# infinite loop 
while run: 
	pygame.time.delay(10) 
	
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			run = False
	keys = pygame.key.get_pressed() 
	
	if keys[pygame.K_LEFT] and x>0: 
		x -= vel 
		
	if keys[pygame.K_RIGHT] and x<500-width: 
		x += vel 
		
	if keys[pygame.K_UP] and y>0: 
		y -= vel 
		
	if keys[pygame.K_DOWN] and y<500-height: 
		y += vel 
		
	win.fill((0, 0, 0)) 
	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) 
	pygame.display.update() 

pygame.quit() 

[/GFGTABS]

Output

Explanation: This code –

Imports and initializes Pygame to use its features.
Creates a 500×500 game window and sets the title.
Defines rectangle position (x, y), size and speed.
Runs a loop to keep the window active until closed.
Uses pygame.event.get() to detect the quit event.
Uses pygame.key.get_pressed() to detect arrow key presses.
Updates the rectangle’s position based on key input.
Clears the screen and redraws the rectangle every frame.
Refreshes the display using pygame.display.update().
Exits Pygame when the loop ends.


"""

"""
Python | Making an object jump in PyGame
Last Updated : 19 Feb, 2020
Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language. Now, it’s up to the imagination or necessity of developer, what type of game he/she wants to develop using this toolkit.
So, in this article, we will learn how to make an object jump using PyGame library in Python.

There is basic formula from classical mechanics to make an object jump.

F = 1/2 * m * v^2 
Where F is the force up/down, m is the mass of the object and v is the velocity. The velocity goes down over time because when the object jumps the velocity will not increase more in this simulation. When object reaches the ground, the jump ends. If isjump variable is True or False it indicates object is jumping or not. If isjump is True, object position will be updated according to the above formula.

Below is the implementation:



# import pygame module in this program  
import pygame 
   
# activate the pygame library .  
# initiate pygame and give permission  
# to use pygame's functionality.  
pygame.init() 
   
# create the display surface object  
# of specific dimension..e(500, 500).  
win = pygame.display.set_mode((500, 500)) 
   
# set the pygame window name  
pygame.display.set_caption("Jump Game") 
   
# object current co-ordinates 
x = 200
y = 200
   
# dimensions of the object 
width = 30
height = 40
   
# Stores if player is jumping or not 
isjump = False
   
# Force (v) up and mass m. 
v = 5
m = 1
   
# Indicates pygame is running 
run = True
   
# infinite loop 
while run: 
   
    # completely fill the surface object  
    # with black colour  
    win.fill((0, 0, 0)) 
   
    # drawing object on screen which is rectangle here  
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) 
       
    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method.  
    for event in pygame.event.get(): 
           
        # if event object type is QUIT  
        # then quitting the pygame  
        # and program both.  
        if event.type == pygame.QUIT: 
               
            # it will make exit the while loop 
            run = False
    # stores keys pressed 
    keys = pygame.key.get_pressed() 
        
    if isjump == False: 
   
        # if space bar is pressed 
        if keys[pygame.K_SPACE]: 
                  
            # make isjump equal to True 
            isjump = True
               
    if isjump : 
        # calculate force (F). F = 1 / 2 * mass * velocity ^ 2. 
        F =(1 / 2)*m*(v**2) 
           
        # change in the y co-ordinate 
        y-= F 
           
        # decreasing velocity while going up and become negative while coming down 
        v = v-1
           
        # object reached its maximum height 
        if v<0: 
               
            # negative sign is added to counter negative velocity 
            m =-1
   
        # objected reaches its original state 
        if v ==-6: 
   
            # making isjump equal to false  
            isjump = False
  
     
            # setting original values to v and m 
            v = 5
            m = 1
       
    # creates time delay of 10ms 
    pygame.time.delay(10) 
   
    # it refreshes the window 
    pygame.display.update()  
# closes the pygame window     
pygame.quit() 

"""







