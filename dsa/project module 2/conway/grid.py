import pygame,random

class Grid:

    def __int__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.cols = width // cell_size
        self.cell_size = cell_size
        # list of list
        self.cells = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def draw(self,window):
        for row in range(self.rows):
            for col in range(self.cols):
                color = (0,255,0) if self.cells[row][col] else (55,55,55)
                pygame.draw.rect(window,color,(col*self.cell_size, row*self.cell_size, self.cell_size -1, self.cell_size-1))

    def fill_randoms(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col] = random.choice([1,0,0,0])


    def clear(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col] = 0

    def toggle_cell(self,row,col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.cells[row][col] = not self.cells[row][col]






