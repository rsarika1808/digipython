import keyword
from random import randint
from turtle import Screen
from urllib.parse import parse_qs
import pgzrun

WIDTH =800
HEIGHT =500

#all the class logic
class Player(Actor):
    speed =5

    def __init__(self, image,speed =5): 
        pos =ri(0,WIDTH),ri(0,HEIGHT) # generate a random x,y coordinte
        super()._init_(image,pos) #call the parent class constructor and pass image and pos
        self.speed =speed #add a new instance variable
         
        def move(self):
            if keyword.w:
                self.y-=self.speed
             
            if keyword.s:
                self.y +=self.speed

            elif keyword.A:
                self.x -= self.speed
                self.angle =+10
                
            elif keyword.D:
                self.x += self.speed
                self.angle =-10
            elif keyword.E:
                self.x +=self,speed
                self.y -+self.speed
            else:
                self.angle=0
           
        def check_boundary(self):
            if p.x <0: #agar player left side se bahar ja rha h
              p.x =WIDTH #to  right side pe dikhne lage
        if p.x > WIDTH:#vice versa
              p.x =0
        if p.y<0:
          p.y =HEIGHT
        if p.y> HEIGHT:
            p.y =0



#main game code
p= Player('ironman')
print(dir(p))
def draw():
    Screen.fill('black')
    p.draw()

def update():
    p.move()
    p.check_boundary()

pgzrun. go()


