x_0 = 0
y_0 = 0
def cake_layers(x,y,cake_length,no_cake_layer,pen):
    '''
    DOCSTRING:
    This function draws a cake through turtle while taking the following inputs:
    no_cake_layer: no of layers in the cake
    layer_color: color of the layer in the cake
    layer_height: height of the layer in the cake'''
    for i in range(no_cake_layer):
        no = i+1
        layer_color = input(f"Enter the color of Layer {no}: ")
        layer_height = int(input(f"Enter the height of Layer {no}: "))
        pen.teleport(x,y)
        pen.pencolor(layer_color)
        pen.fillcolor(layer_color)
        pen.begin_fill()
        pen.fd(cake_length/2)
        pen.left(90)
        pen.fd(layer_height)
        pen.left(90)
        pen.fd(cake_length)
        pen.left(90)
        pen.fd(layer_height)
        pen.left(90)
        pen.fd(cake_length/2)
        pen.end_fill()
        y += (layer_height)
    return y
    pen.teleport(x,y)
    

def cherry_on_top(cake_height,pen):
    pen.teleport(cake_height/15,cake_height)
    pen.pencolor('red')
    pen.fillcolor('red')
    pen.begin_fill()
    pen.circle(cake_height/30)
    pen.end_fill()
    pen.teleport(-cake_height/15,cake_height)
    pen.pencolor('red')
    pen.fillcolor('red')
    pen.begin_fill()
    pen.circle(cake_height/30)
    pen.end_fill()
    


