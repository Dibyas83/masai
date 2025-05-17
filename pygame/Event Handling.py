
"""

Pygame – Event Handling
Last Updated : 21 Feb, 2022
An event is an action that is performed by the user in order to get the desired result. For instance, if a user clicks a button then it is known as a click event. Now, all the events that are performed by the user are inserted into a queue known as an event queue. Since it is a queue, it follows the First In First Out rule i.e. element inserted first will come out first. In this case, when an event is created it is added to the back of the queue and when the event is processed then it comes out from the front. Every element in this queue is associated with an attribute which is nothing but an integer that represents what type of event it is.  Let us learn a few important attributes of the common event types.

SR No.	Event	Attributes
1.	KEYDOWN 	 key, mod, unicode
2.	KEYUP	key, mod
3.	MOUSEBUTTONUP 	pos, button
4.	MOUSEBUTTONDOWN	pos, button
5.	MOUSEMOTION	 pos, rel, buttons
6.	QUIT	          –
Owing to the fact that you have understood what an event in pygame is now let us dive deep into this topic. It is essential to know that the processing of an event must be done within the main function. This is because if in case if it is done, then there is a chance of having an input lag which can result in a poor user experience. The processing is done using pygame.event.get(). This is a function that will return the list of events that can be processed one after another.

Types of Events
1) Keyboard event:
As mentioned above, an event is an action conducted by the user. So let us wonder, what actions can be performed on the keyboard? The simple answer is either pressing the key or releasing it. Pressing the key is known as KEYDOWN and releasing it is known as KEYUP. The attribute associated with these events is known as the key of type integer. Its use is to represent the key of the keyboard. The common keys are represented by a pre-defined integer constant which is a capital K. This K is followed by an underscore and then the name of the key is written. For example K_s, K_F7.

The fact of the matter is that capital letters do not have an integer constant. The solution to this problem is something known as a modifier also known as a mod which is the modifier such as for shift, alt, ctrl, etc. that are being pressed simultaneously as the key.  The integer value of mod is stored in something known as KMOD_  which is followed by the name of the key. For example KMOD_RSHIFT, KMOD_CTRL, etc. Let us revise the concepts that we have learned in the keyboard event topic with the help of a small code.


for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            print("Move the character forwards")
        elif event.key == pygame.K_s:
            print("Move the character backwards")
        elif event.key == pygame.K_a:
            print("Move the character left")
        elif event.key == pygame.K_d:
            print("Move the character right")
2) Mouse events
Let us now understand the different types of mouse events. The first two are MOUSEBUTTONDOWN and MOUSEBUTTONUP which are similar to KEYDOWN and KEYUP except for the fact that here we are using a mouse. In addition to them, there is another mouse event known as MOUSEMOTION. Let us understand all 3 mouse events in detail.

i) MOUSEBUTTONDOWN: The MOUSEBUTTONDOWN event occurs when the user presses the mouse button. It has a couple of attributes which are as follows :

button:  It is an integer that represents the button that has been pressed.  The left button of the mouse is represented by 1, for mouse-wheel the integer is 2, and integer 3 is when the right button of the mouse is pressed.
pos: It is the absolute position of the mouse (x, y) when the user presses the mouse button.
ii) MOUSEBUTTONUP: The MOUSEBUTTONUP event occurs when the user releases the mouse button. It has the same button and pos attributes that the MOUSEBUTTONDOWN has which have been mentioned above.

iii) MOUSEMOTION: This event occurs when the user moves his mouse in the display window. It has the attributes buttons, pos, and rel.

buttons: It is a tuple that represents whether the mouse buttons (left, mouse-wheel, right) are pressed or not.
pos: It is the absolute position (x, y) of the cursor in pixels.
rel: It represents the relative position to the previous position (rel_x, rel_y) in pixels.
Let us revise the values for every mouse button attribute with the help of the following table:

SR No.	Button	Value
1.	Left mouse button 	1
2.	Mouse wheel button	2
3.	Right mouse button 	3
4.	Mouse wheel scroll up	4
5.	Mouse wheel scroll down	5
Let us revise the concepts that we have learned in the mouse event topic with the help of a small code.


for event in pygame. event.get():
    if event.type == pygame.QUIT:
        raise SystemExit
    elif event.type == pygame.MOUSEMOTION:
        if event.rel[0] > 0:
            print("Mouse moving to the right")
        elif event.rel[1] > 0:
            print("Mouse moving down")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 3:
            print("Right mouse button pressed")
    elif event.type == pygame.MOUSEBUTTONUP:
        print("Mouse button has been released")
Let us now have a look at a couple of pygame programs related to event handling.

Example 1:

 The following program will check whether we have pressed the left key or the right key and display output accordingly.


import pygame
pygame.init()

# Creating window
gameWindow = pygame.display.set_mode((800, 300))
pygame.display.set_caption("Event Handling")


exit_game = False
game_over = False

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():  # For Loop
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right arrow key")
            elif event.key == pygame.K_LEFT:
                print("You have pressed left arrow key")

pygame.quit()
quit()
Output:


Example 2:

The following program will check whether we are moving the mouse or pressing the mouse button or releasing it and display output accordingly.


import pygame
pygame.init()

# Creating window
gameWindow = pygame.display.set_mode((800, 300))
pygame.display.set_caption("Event Handling")


exit_game = False
game_over = False

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.MOUSEMOTION:
            if event.rel[0] > 0:
                print("Mouse moving to the right")
            elif event.rel[1] > 0:
                print("Mouse moving down")
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Click event
            if event.button == 3:
                print("Right mouse button pressed")
        elif event.type == pygame.MOUSEBUTTONUP:  # Mouse released
            print("Mouse button has been released")

pygame.quit()
quit()
"""
"""
How to add Custom Events in Pygame?
Last Updated : 17 Jun, 2021
In this article, we will see how to add custom events in PyGame. 

Installation
PyGame library can be installed using the below command:

pip install pygame
Although PyGame comes with a set of events (Eg: KEYDOWN and KEYUP), it allows us to create our own additional custom events according to the requirements of our game. Custom events increase the control and flexibility we have over our game. A custom event is the same as creating a User-defined event.

Syntax:



<event_name> = pygame.USEREVENT + 1



Example:



# Here ADDITION and SUBTRACTION is the event name





ADDITION = pygame.USEREVENT + 1 





SUBTRACTION = pygame.USEREVENT + 2



Now, how do we publish our custom events once they are created? This can be done in two ways:

Using pygame.event.post() method.
Using pygame.time.set_timer() method.
Using pygame.event.post() method
We can directly post our events using pygame.event.post() method. This method adds our event to the end of the events on the queue. In order to execute this, we need to convert our event to Pygame’s event type inorder to match the attributes of the post method and avoid errors.

Syntax:



# Step 1 – Convert event into event datatype of pygame 





ADD_event = pygame.event.Event(event)





# Step 2 – Post the event





pygame.event.post(ADD_event)    # event_name as parameter



Using pygame.time.set_timer() method
Broadcasting the event periodically by using PyGame timers. Here, we’ll be using another method to publish the event by using set_timer() function, which takes two parameters, a user event name and time interval in milliseconds.

Syntax:



# event_name, time in ms





pygame.time.set_timer(event, duration)   



Note: In this, we don’t need to convert the user-defined event into PyGame event datatype.

Now to create a plot with custom events firstly the attributes for the screen should be set as per requirement. Then create an event and convert it to PyGame event datatype. Now add code for your operations that will generate a custom event.

In the given implementation both of the approaches have been handled.

Program : 

 
# Python program to add Custom Events 
import pygame 
  
  
pygame.init() 
  
# Setting up the screen and timer 
screen = pygame.display.set_mode((500, 500)) 
timer = pygame.time.Clock() 
  
# set title 
pygame.display.set_caption('Custom Events') 
  
# defining colours 
WHITE = (255, 255, 255) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
  
# Keep a track of active variable 
bg_active_color = WHITE 
screen.fill(WHITE) 
  
# custom user event to change color 
CHANGE_COLOR = pygame.USEREVENT + 1
  
# custom user event to inflate defalte 
# box 
ON_BOX = pygame.USEREVENT + 2
  
# creating Rectangle 
box = pygame.Rect((225, 225, 50, 50)) 
grow = True
  
# posting a event to switch color after  
# every 500ms 
pygame.time.set_timer(CHANGE_COLOR, 500) 
  
running = True
while running: 
    
    # checks which all events are posted 
    # and based on that perform required 
    # operations 
    for event in pygame.event.get(): 
        
        # switching colours after every 
        # 500ms 
        if event.type == CHANGE_COLOR: 
            if bg_active_color == GREEN: 
                screen.fill(GREEN) 
                bg_active_color = WHITE 
            elif bg_active_color == WHITE: 
                screen.fill(WHITE) 
                bg_active_color = GREEN 
  
        if event.type == ON_BOX: 
            
            # to inflate and deflate box 
            if grow: 
                box.inflate_ip(3, 3) 
                grow = box.width < 75
            else: 
                box.inflate_ip(-3, -3) 
                grow = box.width < 50
  
        if event.type == pygame.QUIT: 
            
            # for quitting the program 
            running = False
  
    # Posting event when the cursor is on top  
    # of the box 
    if box.collidepoint(pygame.mouse.get_pos()): 
        pygame.event.post(pygame.event.Event(ON_BOX)) 
  
    # Drawing rectangle on the screen 
    pygame.draw.rect(screen, RED, box) 
  
    # Updating Screen 
    pygame.display.update() 
      
    # Setting Frames per Second 
    timer.tick(30) 
  
pygame.quit() 

"""

"""
Pygame – Input Handling
Last Updated : 03 Mar, 2022
Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.

The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter.

Handling Keyboards Inputs
Basic steps to handle keyboard input:

Import required libraries.
Create a display surface object using display.set_mode() method of pygame.
Load the image/object.
Create a click event i.e., KEYDOWN
Define all the events keys and perform task.
Create a pause event i.e., KEYUP
Copying the Text surface object to the display surface object using blit() method of pygame display surface object.
Show the display surface object on the pygame window using the display.update() method of pygame.
Example:

 
# importing all the required libraries
import pygame
from pygame.locals import *
from sys import exit
 
# initiating pygame library to use it's 
# functions
pygame.init()
 
# declaring windows/surface width and height
size = width, height = 740, 480
screen = pygame.display.set_mode(size)
 
# loads a new image from a file and convert()
# will create a copy of image on surface
img = pygame.image.load("char.png").convert()
 
# declaring value to variables
x, y = 0, 0
move_x, move_y = 0, 0
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame.QUIT deactivates pygame
            exit()
            # exit() is sys function used to 
            # kill the program
             
     # KEYDOWN event will be triggered everytime 
    # we press a button
    if event.type == KEYDOWN:  
       
        if event.key == K_LEFT:  
            move_x = -0.3  # object moves -0.3 towards x axis
            print("pressed LEFT")
        elif event.key == K_RIGHT:  
            move_x = +0.3  # object moves 0.3 towards x axis
            print("pressed RIGHT")
        elif event.key == K_UP: 
            move_y = -0.3  # object moves -0.3 towards y axis
            print("pressed UP")
        elif event.key == K_DOWN: 
            move_y = +0.3  # object moves 0.3 towards y axis
            print("pressed DOWN")
             
        # K_LCTRL event will be triggered everytime we
        # press left CTRL button
        elif event.key == K_LCTRL:
           
            # declaring new image file to update image
            # everytime left CTRL is pressed
            img = pygame.image.load("char1.png")
            pygame.display.update()  # update image
        elif event.key == K_BACKSPACE:
           
            # this the default file we declared in start 
            # and it will restore it everytime we press
            # backspace
            img = pygame.image.load("char.png")
            pygame.display.update()  # update image
             
     # it will get triggered when left key is released
    if event.type == KEYUP:
        if event.key == K_LEFT:
            move_x = 0  # movement stops
        elif event.key == K_RIGHT:  
            move_x = 0  # movement stops
        elif event.key == K_UP: 
            move_y = 0  # movement stops
        elif event.key == K_DOWN:  
            move_y = 0  # movement stops
            """KEYUP event will be triggered when the release the keys
            and x,y coordinates will not change anymore"""
 
    x += move_x
    y += move_y
    # updating coordinate values of x,y
    screen.fill((255, 255, 255))
     
    # the function will fill the background with white color
    screen.blit(img, (x, y))
     
    # blit() function will copy image file to x,y coordinates.
    pygame.display.update()
    # draw the objects on screen
Output:

Video Player

00:00
00:10


Handling Mouse Inputs:
Basic steps to handle mouse input:

Import required libraries.
Create a display surface object using display.set_mode() method of pygame.
Load the image/object.
Create a click event i.e., MOUSEBUTTONDOWN.
Define all the events keys and perform task.
Create a pause event i.e., MOUSEBUTTONUP.
Copying the Text surface object to the display surface object using blit() method of pygame display surface object.
Show the display surface object on the pygame window using the display.update() method of pygame.
Example:

 
# importing all the required libraries
import pygame
from pygame.locals import *
from sys import exit
 
# initiating pygame library to use it's functions
pygame.init()
 
# declaring windows/surface width and height
size = width, height = 740, 480
screen = pygame.display.set_mode(size)
 
 
# loads a new image from a file and convert() 
# will create a copy of image on surface
img = pygame.image.load("char.png").convert()
 
# declaring value to variables
clicking = False
right_clicking = False
middle_click = False
 
while True:
    mx, my = pygame.mouse.get_pos()  # gets mouse x,y coordinates
    location = [mx, my]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           
            # pygame.QUIT deactivates pygame
            exit()
            # exit() is sys function used to kill the program
 
    # MOUSEBUTTONDOWN event is triggered when a button is pressed
    if event.type == MOUSEBUTTONDOWN:
       
        # returns true when mouse left button is clicked
        if event.button == 1:  
            clicking = True
             
            # declaring new image file to update image
            # everytime left button clicking is true
            img = pygame.image.load("char1.png")
            pygame.display.update()  # update image
         
        # returns true when mouse right button is clicked
        if event.button == 3:  
            right_clicking = True
             
            # declaring new image file to update image
            # everytime right button is clicked
            img = pygame.image.load("char.png")
            pygame.display.update()  # update image
             
        # returns true when mouse middle button is clicked
        if event.button == 2:  
            middle_click = middle_click
             
            # rescale image when middle button clicking is true
            img = pygame.transform.scale(img, (100, 100))
            pygame.display.update()  # update image
 
    # MOUSEBUTTONUP is triggered when mouse button 
    # is released(not clicked)
    if event.type == MOUSEBUTTONUP:
        if event.button == 1:
            clicking = False
 
    screen.fill((255, 255, 255))
     
    # the function will fill the background
    # with white color
    screen.blit(img, (location[0], location[1]))
     
    # blit() function will copy image file 
    # to x,y coordinates.
    pygame.display.update()
    # draw the objects on screen
"""

"""
How to get keyboard input in PyGame ?
Last Updated : 08 Jun, 2022
While using pygame module of Python, we sometimes need to use the keyboard input for various operations such as moving a character in a certain direction. To achieve this, we have to see all the events happening. Pygame keeps track of events that occur, which we can see with the events.get() function. In this article, we are going to discuss how we can get and use various keyboard inputs in pygame.

Detecting if a key is pressed:
Whenever a key is pressed or released, pygame.event() queue methods pygame.KEYDOWN and pygame.KEYUP events respectively.

For example, if we want to detect if a key was pressed, we will track if any event of pygame.KEYDOWN occurred or not and, accordingly, we will get to know if any key was pressed or not. The code for detecting if any key was pressed or not can be written as:

 
# importing pygame module
import pygame
 
# importing sys module
import sys
 
# initialising pygame
pygame.init()
 
# creating display
display = pygame.display.set_mode((300, 300))
 
# creating a running loop
while True:
       
    # creating a loop to check events that
    # are occurring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:
           
            # if keydown event happened
            # than printing a string to output
            print("A key has been pressed")
 
 

Output:




 

After running this code, it is seen that whenever a key has pressed a string “A key has been pressed” is printed on the terminal

Detecting which key was pressed:
To know which key was pressed, we have to check the event.key variable corresponds to which pygame keys. For example, the pygame key for the letter “A” is “K_a” then we will compare event.Key with K a and if it comes to be same that means the key “A” was pressed.


 

The various keyboard key and corresponding pygame keys are:

pygamekey	Description
K_BACKSPACE	backspace
K_TAB	tab
K_CLEAR	clear
K_RETURN	return
K_PAUSE	pause
K_ESCAPE	escape
K_SPACE	space
K_EXCLAIM	exclaim
K_HASH	hash
K_QUOTEDBL	quotedbl
K_DOLLAR	dollar
K_AMPERSAND	ampersand
K_QUOTE	quote
K_LEFTPAREN	left parenthesis
K_RIGHTPAREN	right parenthesis
K_ASTERISK	asterisk
K_PLUS	plus sign
K_COMMA	comma
K_MINUS	 minus sign
K_PERIOD 	period
K_SLASH	forward slash
K_0 	0
K_1	1
K_2	2
K_3	3
K_4	4
K_5	5
K_6	6
K_7	7
K_8	8
K_9	9
K_COLON	colon
K_SEMICOLON	semicolon
K_LESS	less-than sign
K_EQUALS	equals sign
K_GREATER	greater-than sign
K_QUESTION 	question mark
K_AT	at
K_LEFTBRACKET	left bracket
K_BACKSLASH 	backslash
K_RIGHTBRACKET  	right bracket
K_CARET	caret
K_UNDERSCORE	underscore
K_BACKQUOTE	grave
K_a,b,c…….z	A to Z Alphabet
K_DELETE	delete
K_KP0, K_KP1, K_KP2….K_KP9	keypad 0 to 9
K_KP_PERIOD	keypad period
K_KP_DIVIDE	keypad divide
K_KP_MULTIPLY	keypad multiply
K_KP_MINUS	keypad minus
K_KP_PLUS  	keypad plus
K_KP_ENTER	keypad enter
K_KP_EQUALS	keypad equals
K_UP	up arrow
K_DOWN	down arrow
K_RIGHT 	right arrow
K_LEFT  	Left arrow
K_INSERT	Insert
K_HOME	Home
K_END	End
K_PAGEUP 	Page Up
K_PAGEDOWN  	Page Down
K_F1, K_F2, K_F3……K_F15	F1 to F15
K_NUMLOCK	Numlock
K_CAPSLOCK	Capsloack
K_SCROLLOCK	Scrollock
K_RSHIFT	Right shift
K_LSHIFT	Left shift
K_RCTRL	right control
K_LCTRL	Left control
K_RALT 	Right alt
K_LALT 	Left alt
K_RMETA	right meta
K_LMETA 	left meta
K_LSUPER	left Windows key
K_RSUPER 	right Windows key
K_MODE	mode shift
K_HELP	Help
K_PRINT	Print Screen
K_SYSREQ	sysrq
K_BREAK	Break
K_MENU	Menu
K_POWER	Power
K_EURO	Euro

 

For example, let’s create a code to check if key “A” or “J” or “P” or “M” was pressed or not. The code for checking will be: 

 
# importing pygame module
import pygame
 
# importing sys module
import sys
 
# initialising pygame
pygame.init()
 
# creating display
display = pygame.display.set_mode((300, 300))
 
# creating a running loop
while True:
       
    # creating a loop to check events that 
    # are occurring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:
               
            # checking if key "A" was pressed
            if event.key == pygame.K_a:
                print("Key A has been pressed")
               
            # checking if key "J" was pressed
            if event.key == pygame.K_j:
                print("Key J has been pressed")
               
            # checking if key "P" was pressed
            if event.key == pygame.K_p:
                print("Key P has been pressed")
             
            # checking if key "M" was pressed
            if event.key == pygame.K_m:
                print("Key M has been pressed")
Output:



When we run this code and press the given keys the corresponding strings will be printed on the terminal.

"""





