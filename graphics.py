from tkinter import Tk, BOTH, Canvas
import time

class Window():

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Map Solver")
        self.__canvas = Canvas(self.__root,width= width,height= height)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW",self.close)

    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def draw_line(self,line,fill_color):
        line.draw(self.__canvas,fill_color)

    def get_canvas(self):
        return self.__canvas

    def close(self):
        self.__running = False


class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line():
    def __init__(self,point_1,point_2):
        if not isinstance(point_1, Point) or not isinstance(point_2, Point):
            raise TypeError("Both point_1 and point_2 must be instances of the Point class")
        self.point_1 = point_1
        self.point_2 = point_2
        self.x1 = self.point_1.x
        self.x2 = self.point_2.x
        self.y1 = self.point_1.y
        self.y2 = self.point_2.y     

    def  draw(self,canvas,fill_color):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2)


class Cell():
    def __init__(self,x1,x2,y1,y2,win=None,has_left_wall = True, has_right_wall = True, has_top_wall = True, has_bottom_wall = True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self,):
        if self._win:
            canvas = self._win.get_canvas()

            if self.has_left_wall:
                canvas.create_line(self._x1, self._y1,self._x1,self._y2,fill="black", width=2)
            if self.has_top_wall:
                canvas.create_line(self._x1, self._y2,self._x2,self._y2,fill="black", width=2)
            if self.has_right_wall:
                canvas.create_line(self._x2, self._y2,self._x2,self._y1,fill="black", width=2)
            if self.has_bottom_wall:
                canvas.create_line(self._x2, self._y1,self._x1,self._y1,fill="black", width=2)

    def draw_move(self,to_cell, undo = False):
        canvas = self._win.get_canvas()
        fill_color = "red"
        start_x = (self._x1+self._x2)/2
        start_y = (self._y1+self._y2)/2
        stop_x = (to_cell._x1+to_cell._x2)/2
        stop_y = (to_cell._y1+to_cell._y2)/2

        if undo:
            fill_color = "gray"
        
        canvas.create_line(start_x, start_y,stop_x,stop_y,fill=fill_color, width=2)



class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        starting_x = self._x1
        starting_y = self._y1

        for r in range(self._num_cols):
            self._cells.append([Cell(x1 = starting_x + (i * self._cell_size_x),x2 = starting_x + (i * self._cell_size_x) + self._cell_size_x,y1 = starting_y + (r * self._cell_size_y),y2 = starting_y + (r * self._cell_size_y) + self._cell_size_y,win=self._win) for i in range(self._num_rows)])
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i,j)
            

    def _draw_cell(self, i, j):
        if self._win:
            self._cells[i][j].draw()
            self._animate()

    def _animate(self):
        if self._win:
            self._win.redraw()
            time.sleep(0.05)

        


        



        







