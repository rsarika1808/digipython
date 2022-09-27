
import pgzrun

HEIGHT =600
WIDTH =1000

C=Actor('chick',(100,100))
W =Actor('walrus',(400,400))
cookie =Actor('cookie',(100,900,))
score =0 #variable(global)
speed =5#variable(global)
def draw():
    # screen.blit('big',pos =(0,0))
    C.draw()
    W.draw()
    cookie.draw()
    screen.draw.text("A Chicken Story",(10,10),color ='red')
    screen.draw.text(f"score:{score}",(900,10),color ='red')
    
    def update():
        if 'keyboard'.W:
            C.y-=speed
        elif 'keyboard'.S:
            C.y+=speed
        elif 'keyboard'.A:
            C.x-=speed         
        elif 'keyboard'.D:
            C.x+=speed
        if C.colliderect(cookie):
            score+=1
            cookie.pos =(randint(100,900),randint(100,500))

pgzrun.go(),
 







    