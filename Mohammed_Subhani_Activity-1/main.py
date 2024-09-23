from candle import draw_candle,draw_circle,draw_rectangle
from cake import cake_layers, cherry_on_top
from turtle import Screen, Turtle
from table import table_build



def main():
    '''
    DOCSTRING:
    This function takes inputs and draws the table, cake and the decorations accordingly
    table_length: length of the table
    table_color: color of the table
    cake_length: length of the cake
    no_cake_layer: no. of layers in the cake
    sc: screen object
    pen: turtle object'''
    x_0 = 0
    y_0 = 0
    table_length = int(input('Enter table length: '))
    table_color = input('Enter table colour: ')
    cake_length = int(input("Enter the length of your Cake (Should be less than table length): "))
    no_cake_layer = int(input("Enter the No. of layers in your Cake: "))
    sc = Screen()
    sc.bgcolor('deep sky blue')
    sc.tracer(0,0)
    pen = Turtle()
    pen.hideturtle()
    table_build(table_length,table_color,pen)
    cake_height=cake_layers(x_0,y_0,cake_length,no_cake_layer,pen)
    cherry_on_top(cake_height,pen)
    draw_candle(cake_height,pen)
    sc.update()
    sc.exitonclick()

if __name__ == "__main__":
    main()