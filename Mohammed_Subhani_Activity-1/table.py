from turtle import Screen, Turtle



def draw_table(table_length, table_color,pen):
    pen.pencolor(table_color)  
    pen.begin_fill()
    pen.fillcolor(table_color)
    pen.teleport(0,2)
    pen.fd(table_length/2)
    pen.right(90)
    pen.fd(10)
    pen.right(90)
    pen.fd(table_length)
    pen.right(90)
    pen.fd(10)
    pen.right(90)
    pen.fd(table_length/2)
    pen.end_fill()

def draw_leg1(table_length,table_color,pen):
    pen.teleport((-table_length/2)+table_length*0.05,2)
    pen.pencolor(table_color)
    pen.fillcolor(table_color)
    pen.begin_fill()
    pen.right(90)
    pen.fd(125)
    pen.left(90)
    pen.fd(10)
    pen.left(90)
    pen.fd(125)
    pen.left(90)
    pen.fd(10)
    pen.right(180)
    pen.end_fill()
    pen.teleport(0,0)
    
def draw_leg2(table_length,table_color,pen):
    pen.teleport((table_length/2)-table_length*0.05,2)
    pen.pencolor(table_color)
    pen.fillcolor(table_color)
    pen.begin_fill()
    pen.right(90)
    pen.fd(125)
    pen.right(90)
    pen.fd(10)
    pen.right(90)
    pen.fd(125)
    pen.right(90)
    pen.fd(10)
    pen.end_fill()

def draw_leg3(table_length, table_color,pen):
    pen.teleport((-table_length/2)+table_length*0.15,2)
    pen.pencolor(table_color)
    pen.fillcolor(table_color)
    pen.begin_fill()
    pen.right(90)
    pen.fd(75)
    pen.left(90)
    pen.fd(10)
    pen.left(90)
    pen.fd(75)
    pen.left(90)
    pen.fd(10)
    pen.right(180)
    pen.end_fill()
    pen.teleport(0,0)

def draw_leg4(table_length,table_color,pen):
     pen.teleport((table_length/2)-table_length*0.15,2)
     pen.pencolor(table_color)
     pen.fillcolor(table_color)
     pen.begin_fill()
     pen.right(90)
     pen.fd(75)
     pen.right(90)
     pen.fd(10)
     pen.right(90)
     pen.fd(75)
     pen.right(90)
     pen.fd(10)
     pen.end_fill()
    




def table_build(table_length,table_color,pen):
    '''
    DOCSTRING:
    this function draws a table using the functions  draw_table, draw_leg1, draw_leg2, draw_leg3, draw_leg4 '''
    draw_table(table_length,table_color,pen)
    draw_leg1(table_length,table_color,pen)
    draw_leg2(table_length,table_color,pen)
    draw_leg3(table_length,table_color,pen)
    draw_leg4(table_length,table_color,pen)
    




