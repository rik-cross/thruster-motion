import math

# set screen width and height
WIDTH = 800
HEIGHT = 800

spaceship = Actor('spaceship')
spaceship.center=(400, 400)
spaceship.x_speed = 0
spaceship.y_speed = 0

def update():

    if keyboard.left:
        spaceship.angle += 2

    if keyboard.right:
        spaceship.angle -= 2

    # NOTE: changing an actors image resets the sprite
    # to fix this, store the angle as 'a' temporarily
    # change the image and then reset the old value for the angle
    a = spaceship.angle
    if keyboard.up:
        spaceship.image = 'spaceship_thrust'
        # NOTE: as Pygame angles are backwards
        # (i.e. 0 - 360 anti-clockwise)
        # you need to subtact the speed (not add)
        spaceship.x_speed += math.sin(math.radians(a)) * 0.01 * -1
        spaceship.y_speed += math.cos(math.radians(a)) * 0.01 * -1
    else:
        spaceship.image = 'spaceship'
    spaceship.angle = a

    spaceship.x += spaceship.x_speed
    spaceship.y += spaceship.y_speed

def draw():
    screen.clear()
    spaceship.draw()

    using = math.radians(spaceship.angle)
    screen.draw.text('Angle (deg):',(10,10),color='white')
    screen.draw.text(str(round(spaceship.angle,2)),(10,25),color='white')
    screen.draw.text('Angle (rad):',(150,10),color='white')
    screen.draw.text(str(round(using,2)),(150,25),color='white')
    screen.draw.text('Sin/x:',(300,10),color='white')
    screen.draw.text(str(round(math.sin(using),2)),(300,25),color='white')
    screen.draw.text('Cos/y:',(450,10),color='white')
    screen.draw.text(str(round(math.cos(using),2)),(450,25),color='white')
