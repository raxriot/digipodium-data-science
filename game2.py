from random import randint
import pgzrun

WIDTH = 1000    
HEIGHT = 500

class Player(Actor):
    '''This is class Player, that inherits from Actor'''
    speed = 5

    def __init__(self, image):
        super().__init__(image)
        self.pos = (WIDTH/2, HEIGHT/2) 

    def movement(self):
        print('movement')
        '''This is method movement, that controls player movement'''
        if keyboard.left:
            self.x -= self.speed
        if keyboard.right:
            self.x += self.speed
        if keyboard.up:
            self.y -= self.speed
        if keyboard.down:
            self.y += self.speed
        if keyboard.space:
            self.angle += self.speed 

    def check_boundary(self):
        '''This is method check_boundary, that checks if player is within screen boundary'''
        if self.left < 0:
            self.left = 0
        if self.right > WIDTH:
            self.right = WIDTH
        if self.top < 0:
            self.top = 0
        if self.bottom > HEIGHT:
            self.bottom = HEIGHT
    
    def eat(self, fruit):
        global score
        if self.colliderect(fruit):
            fruit.relocate()
            sounds.clap.play()
            score += 10

    def update(self):
        '''This is method update, that updates player position'''
        self.movement()
        self.check_boundary()

class Enemy(Actor):
    speed = 2
    def __init__(self, image):
        super().__init__(image) # call parent class constructor
        self.pos = (-100, HEIGHT/2) # set initial position

    def tracking(self, p):
        # enemy tracks player
        if p.x > self.x:
            self.x += self.speed
        if p.x < self.x:
            self.x -= self.speed 
        if p.y > self.y:
            self.y += self.speed
        if p.y < self.y:
            self.y -= self.speed
        print(f'player {p.pos} enemy {self.pos}')
        if self.colliderect(p):
            exit()

class Fruit(Actor):
    
    def __init__(self, image):
        super().__init__(image)
        self.x = randint(50, WIDTH-50)
        self.y = randint(50, HEIGHT-50)

    def relocate(self):
        self.x = randint(50, WIDTH-50)
        self.y = randint(50, HEIGHT-50)

# game code start now

p = Player('hero')
e = Enemy('enemy')
c = Fruit('friut')  
score = 0

def draw():
    screen.clear()
    p.draw()
    e.draw()
    c.draw()
    screen.draw.text(f'Score: {score}', (10, 10), color='white')

def update():
    p.update()
    p.eat(c)
    e.tracking(p)

pgzrun.go()



