import pgzrun
from random import randint

#SCREEN SIZE
WIDTH =1000
HEIGHT =500

#objects
p = Actor('hero')
e = Actor('enemy')
c = Actor('friut')

#config
c.x = randint(50, WIDTH-50)
c.Y = randint(50,HEIGHT-50)
p.pos = (WIDTH/2, HEIGHT/2)
e.pos = (-100, HEIGHT/2)
score = 0

#drawing on screen
def draw():
    screen.clear()
    p.draw()
    e.draw()
    c.draw()
    screen.draw.text(f'Score:{score}', (10, 10), color='white')

def player_control():
        #player control
    global score
    if keyboard.left:
        p.x -= 5
    if keyboard.right:
        p.x += 5
    if keyboard.up:
        p.y -= 5
    if keyboard.down:
        p.y += 5
    if keyboard.space:
        p.angle -=5

def enemy_tracking():
    

    #enemy tracking player
    if p.x > e.x:
        e.x +=1
    if p.x < e.x:
        e.x -=1
    if p.y > e.y:
        e.y +=1
    if p.y < e.y:
        e.y -=1
    if e.colliderect(p):
        exit()

def fruit_collider():
        global score
    #fruit collision
        if p.colliderect(c):
            c.x = randint(50, WIDTH-50)
            c.Y = randint(50,HEIGHT-50)
            score +=10
            sounds.clap.play()


def update(dt): #ye update karne ke lie
    fruit_collider()
    enemy_tracking()
    player_control()

#game loop
pgzrun.go()
