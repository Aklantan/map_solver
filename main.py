from graphics import Window, Line, Point

def main():
    win = Window(800,600)

    point1 = Point(4,5)
    point2 = Point(11,34)

    point3 = Point(108,245)
    point4 = Point(23,43)

    line1 = Line(point1,point2)
    line2 = Line(point3,point4)
    line3 = Line(point2, point3)
    line4 = Line(point4,point1)

    win.draw_line(line2,"black")
    win.draw_line(line3,"black")

    win.wait_for_close()

main()