# Maze Solver
from tkinter import Tk, BOTH, Canvas
import time


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y
        

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, Canvas, fill="black"):
        Canvas.create_line(self.point1.x, self.point1.y, self.point2.x, 
                           self.point2.y, fill=fill, width=2)


class Cell:
    def __init__(self, instance_of_win): 
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = instance_of_win

    def draw(self, top_left, bottom_right):
        self.__x1 = top_left[0]
        self.__y1 = top_left[1]
        self.__x2 = bottom_right[0]
        self.__y2 = bottom_right[1]

        if self.has_left_wall:
            # make a point that is the top_left point
            point1 = Point(self.__x1, self.__y1)
            
            # make a point that is the bottom_left point
            point2 = Point(self.__x1, self.__y2)

            # pass those points into Line to make the line
            my_line = Line(point1, point2)

            # draw the line
            self.__win.draw_line(my_line, "black")

        if self.has_right_wall:
            point1 = Point(self.__x2, self.__y1)
            point2 = Point(self.__x2, self.__y2)
            my_line = Line(point1, point2)
            self.__win.draw_line(my_line, "black")

        if self.has_top_wall:
            point1 = Point(self.__x1, self.__y1)
            point2 = Point(self.__x2, self.__y1)
            my_line = Line(point1, point2)
            self.__win.draw_line(my_line, "black")

        if self.has_bottom_wall:
            point1 = Point(self.__x1, self.__y2)
            point2 = Point(self.__x2, self.__y2)
            my_line = Line(point1, point2)
            self.__win.draw_line(my_line, "black")

    # Draw Move function Ch2 L3
    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "gray"
        else:
            color = "red"
        center_x = (self.__x1 + self.__x2) // 2      # for self
        center_y = (self.__y1 + self.__y2) // 2

        center_to_x = (to_cell.__x1 + to_cell.__x2) // 2   # for to_cell
        center_to_y = (to_cell.__y1 + to_cell.__y2) // 2
        point1 = Point(center_x, center_y)
        point2 = Point(center_to_x, center_to_y)
        my_line = Line(point1, point2)
        self.__win.draw_line(my_line, color)

class Maze:

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []

        self.__create_cells()


    def __create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self.__cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.__cells[i][j].draw([x1, y1], [x2, y2])
        self.__animate()

    def __animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
        
    



def main():
    win = Window(800, 600)

    maze = Maze(
        x1 = 50,
        y1 = 50,
        num_rows = 10,
        num_cols = 10,
        cell_size_x = 50,
        cell_size_y = 50,
        win=win
    )
    maze._Maze__create_cells()
    

    win.wait_for_close()


main()