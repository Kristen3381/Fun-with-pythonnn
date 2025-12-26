import turtle


t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("#020d1f") 
t.speed(0)
t.left(90)
t.up()
t.backward(200)
t.down()
t.color("forest green")

def draw_tree(branch_len, t):
    if branch_len > 5:
        
        t.pensize(branch_len / 10)
        t.forward(branch_len)
        
        
        t.right(25)
        draw_tree(branch_len - 15, t)
        
       
        t.left(50)
        draw_tree(branch_len - 15, t)
        
        
        t.right(25)
        t.up()
        t.backward(branch_len)
        t.down()
        
       
        if branch_len < 20:
            t.color("red")
            t.begin_fill()
            t.circle(3)
            t.end_fill()
            t.color("forest green")

draw_tree(100, t)

t.up()
t.goto(-10, 110)
t.down()
t.color("yellow")
t.begin_fill()
for _ in range(5):
    t.forward(20)
    t.right(144)
t.end_fill()

t.hideturtle()
turtle.done()