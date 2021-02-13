from ursina import *

def update():
    test_square.x -= 1 * time.dt

app = Ursina()

test_square = Entity(model= 'quad', color = color.red, scale=(1,4), position=(1,5))


app.run()