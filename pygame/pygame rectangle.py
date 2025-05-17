"""

How to draw rectangle in Pygame?
Last Updated : 23 Dec, 2022
Pygame is a Python library designed to develop video games. Pygame adds functionality on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in the python language.

Functions  Used:

pygame.display.set_mode(): This function is used to initialize a surface for display. This function takes the size of the display as a parameter.
pygame.display.flip(): This function is used to update the content of the entire display surface of the screen.
pygame.draw.rect(): This function is used to draw a rectangle. It takes the surface, color, and pygame Rect object as an input parameter and draws a rectangle on the surface.
Example 1: This example draws a rectangle that is filled with red color.




# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400,300))

# Initializing Color
color = (255,0,0)

# Drawing Rectangle
pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
pygame.display.flip()
Output:



Example 2: This example draws a rectangle with a red border and no color-filled inside.




# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400,300))

# Initializing Color
color = (255,0,0)

# Drawing Rectangle
pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60),  2)
pygame.display.flip()
"""










