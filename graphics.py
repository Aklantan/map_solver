from tkinter import Tk, BOTH, Canvas

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



