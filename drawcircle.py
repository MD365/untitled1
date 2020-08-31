import math
import turtle
def drawCircleTurtle(x,y,r):
    turtle.up()#提笔
    turtle.setpos(x+r,y)#定位笔的位置
    turtle.down()#落笔


    for i in range(0, 365, 5):  #以5位步长递增
        a = math.radians(i)  #从度转化为弧度
        turtle.setpos(x + r* math.cos(a), y + r*math.sin(a))



drawCircleTurtle(100,100,50)
turtle.mainloop()