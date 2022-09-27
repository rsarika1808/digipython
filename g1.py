
import pgzrun

WIDTH =500
HEIGHT =400

P =Actor('ironman',(200,200))

def draw():
    screen.fill('black')
    P.draw()

    def update():
        if keyboard.left:
            P.x -=2

        elif keyboard.right:
            P.y-=2

        elif keyboard.down:

            P.y+= (2)
pgzrun.go()



