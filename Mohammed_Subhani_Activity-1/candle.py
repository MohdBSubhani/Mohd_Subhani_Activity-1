def draw_rectangle(width, height, color,pen):
    pen.fillcolor(color)
    pen.begin_fill()
    pen.fd (width/2)
    pen.left(90)
    pen.fd (height)
    pen.left(90)
    pen.fd(width)
    pen.left(90)
    pen.fd (height)
    pen.left(90)
    pen.fd (width/2)
    pen.end_fill()

def draw_circle(radius, color,pen):
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def draw_candle(cake_height,pen):
    '''
    DOCSTRING:
    this function draws a candle using the functions draw_rectangle and draw_circle'''
    pen.penup()
    pen.goto(0,cake_height)
    pen.pendown()
    pen.pencolor('white')
    draw_rectangle(cake_height / 15, cake_height / 3, 'white',pen)  
    pen.penup()
    pen.goto(0, cake_height / 3 + cake_height)
    pen.pendown()
    pen.pencolor('orange')
    draw_circle(cake_height / 20, 'orange',pen)
    draw_circle(cake_height / 30, 'dark orange',pen)
    draw_circle(cake_height / 35, 'red',pen)  

