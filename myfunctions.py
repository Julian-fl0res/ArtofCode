import turtle

bob = turtle.Turtle()

def draw_rectangle(bob,width,height,color):
    bob.color(color)
    bob.fillcolor(color)
    bob.begin_fill()

    for times in range(2):
        bob.forward(width)
        bob.left(90)
        bob.forward(height)
        bob.left(90)
    bob.end_fill()

def draw_star(bob,size,color):
    bob.color(red)
    bob.fillcolor(red)
    bob.begin_fill()
    for times in range(5):
        bob.forward(size)
        bob.right(144)
    bob.end_fill()

def set_random_rainbow_color(bob):
    red = random.random()
    green = random.random()
    blue = random.random()
    bob.color(red,green,blue)

def tree(x,y):
    jump(x,y)
    polygon(3,100,"green")
    bob.forward(40)
    bob.right(90)
    polygon(4,25,"brown")
    bob.left(90)

def polygon(sides,distance):
  bob.color("red")
  angle = 360 / sides
  bob.begin_fill
  for times in range(sides):
    bob.forward(distance)
    bob.left(angle)
  bob.end_fill()

def comet(size, angle ,amt):
  for times in range(amt):
    bob.width(times)
    bob.forward(distance)
    bob.left(amt)

def jump(x,y):
  bob.penup()
  bob.goto(x,y)

  bob.pendown()

def square( size ):
    for times in range( 4 ):
        bob.forward( 100 )
        bob.left( 90 )

def pentagons( size ):
    for times in range( 5 ):
        bob.forward( size )
        bob.left( 72 )

def drawsquare( sizeS, sizeC ):
    for times in range(4):
        bob.forward( sizeS )
        bob.right( 90 )
        bob.circle( sizeC )


