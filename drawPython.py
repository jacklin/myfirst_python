import turtle
def drawLine(rad,angle,len, neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300, 800, 0 ,0)
    turtle.pensize(30)
    turtle.pencolor("red")
    turtle.seth(-40)
    drawLine(40,80,5,15)
main()

input("33333")