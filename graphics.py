from tkinter import Tk, BOTH, Canvas
import time
import random

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
        self._visited = False

    def draw(self,):
        if self._win:
            canvas = self._win.get_canvas()

            if self.has_left_wall:
                canvas.create_line(self._x1, self._y1,self._x1,self._y2,fill="black", width=2)
            else:
                canvas.create_line(self._x1, self._y1,self._x1,self._y2,fill="white", width=2)

            if self.has_bottom_wall:
                canvas.create_line(self._x1, self._y2,self._x2,self._y2,fill="black", width=2)
            else:
                canvas.create_line(self._x1, self._y2,self._x2,self._y2,fill="white", width=2)

            if self.has_right_wall:
                canvas.create_line(self._x2, self._y2,self._x2,self._y1,fill="black", width=2)
            else:
                canvas.create_line(self._x2, self._y2,self._x2,self._y1,fill="white", width=2)

            if self.has_top_wall:
                canvas.create_line(self._x2, self._y1,self._x1,self._y1,fill="black", width=2)
            else:
                canvas.create_line(self._x2, self._y1,self._x1,self._y1,fill="white", width=2)

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
        seed = None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._reset_cells_visited()
        

    def _create_cells(self):
        starting_x = self._x1
        starting_y = self._y1

        for r in range(self._num_cols):
            self._cells.append([Cell(x1 = starting_x + (i * self._cell_size_x),x2 = starting_x + (i * self._cell_size_x) + self._cell_size_x,y1 = starting_y + (r * self._cell_size_y),y2 = starting_y + (r * self._cell_size_y) + self._cell_size_y,win=self._win) for i in range(self._num_rows)])
        self._break_walls()
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)
        self._animate()
            

    def _draw_cell(self, i, j):
        #if i == self._num_cols-1 and j == self._num_rows-1:
        #   print("Exit cell processed at:", time.time())
        if self._win:
            self._cells[i][j].draw()
            

    def _animate(self):
        if self._win:
            self._win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall= False
        self._cells[0][0].draw()
        self._cells[-1][-1].has_bottom_wall= False
        self._cells[-1][-1].draw()

    def _break_walls_r(self,i,j):
        self._cells[i][j]._visited = True
        while True:
            visited = []
            if self._validate_cell(i-1,j) and self._cells[i-1][j]._visited == False:
                visited.append((i-1,j))
            if self._validate_cell(i,j+1) and self._cells[i][j+1]._visited == False:
                visited.append((i,j+1))
            if self._validate_cell(i+1,j) and self._cells[i+1][j]._visited == False:
                visited.append((i+1,j))
            if self._validate_cell(i,j-1) and self._cells[i][j-1]._visited == False:
                visited.append((i,j-1))
            if not visited:
                 self._cells[i][j].draw()
                 return
            new_direction = random.randrange(len(visited))
            movement = ""
            if visited[new_direction][0] != i:
                if visited[new_direction][0] < i:
                    movement = "up"
                else:
                    movement = "down"
            if visited[new_direction][1] != j:
                if visited[new_direction][1] < j:
                    movement = "left"
                else:
                    movement = "right"
            
            #print(f"At cell ({i},{j}), moving {movement}, breaking walls")

            match movement:
                case "up":
                    # break current cell's top wall
                    self._cells[i][j].has_top_wall = False
                    # break new cell's bottom wall
                    self._cells[i-1][j].has_bottom_wall = False
                case "down":
                    # break current cell's bottom wall
                    self._cells[i][j].has_bottom_wall = False
                    # break new cell's top wall
                    self._cells[i+1][j].has_top_wall = False
                case "left":
                    # break current cell's left wall
                    self._cells[i][j].has_left_wall = False
                    # break new cell's right wall
                    self._cells[i][j-1].has_right_wall = False
                case "right":
                    # break current cell's right wall
                    self._cells[i][j].has_right_wall = False
                    # break new cell's left wall
                    self._cells[i][j+1].has_left_wall = False

            self._break_walls_r(visited[new_direction][0],visited[new_direction][1])

    
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):


        self._animate()

        # vist the current cell
        self._cells[i][j]._visited = True

        # if we are at the end cell, we are done!
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # move left if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i][j-1]._visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j -1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # move right if there is no wall and it hasn't been visited
        if (
            j < self._num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i][j + 1]._visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j +1])
            if self._solve_r(i, j+ 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)



        # move up if there is no wall and it hasn't been visited
        if (
            i > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i-1][j]._visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # move down if there is no wall and it hasn't been visited
        if (
            i < self._num_cols - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i + 1][j]._visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # we went the wrong way let the previous cell know by returning False

        return False

    # create the moves for the solution using a depth first search
    def solve(self):

        return self._solve_r(0, 0)
        

             
    def _break_walls(self):
        self._break_walls_r(0, 0)
        
        # Debug: count visited cells
        visited_count = sum(cell._visited for row in self._cells for cell in row)
        total_cells = self._num_cols * self._num_rows
        #print(f"Visited {visited_count} out of {total_cells} cells")
                
            

    def _validate_cell(self, i,j):
        return 0 <= i < self._num_cols and 0 <= j < self._num_rows
        
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j]._visited = False






        


        



        







