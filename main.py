from graphics import Window, Line, Point, Cell, Maze

def main():
    win = Window(800,600)

    # point1 = Point(4,5)
    # point2 = Point(11,34)

    # point3 = Point(108,245)
    # point4 = Point(23,43)

    # line1 = Line(point1,point2)
    # line2 = Line(point3,point4)
    # line3 = Line(point2, point3)
    # line4 = Line(point4,point1)

    # win.draw_line(line2,"black")
    # win.draw_line(line3,"black")
    
    # cell1= Cell(10,30,10,30,win)
    # cell2= Cell(100,130,100,130,win,has_bottom_wall=False)
    # cell3= Cell(200,230,200,230,win,has_left_wall=False)
    # cell4= Cell(300,330,300,330,win,has_right_wall=False)

    # cell1.draw()
    # cell2.draw()
    # cell3.draw()
    # cell4.draw()

    # cell1.draw_move(cell2)
    # cell2.draw_move(cell3)
    # cell3.draw_move(cell4)
    # cell4.draw_move(cell2,undo=True)

    maze = Maze(0,0,10,10,60,60,win)


    win.wait_for_close()

main()