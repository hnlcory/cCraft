from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController 

class Voxel(Button):
    def __init__(self, position= (0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model= 'cube',
            origin_y=0.5,
            texture='white_cube',
            color= color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.gray)

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                voxel= Voxel(position = self.position + mouse.normal)
            if key == 'left mouse down':
                destroy(self)

app = Ursina()
window.title = 'cCraft Demo'

for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x,0,z))
player = FirstPersonController
player()

app.run()