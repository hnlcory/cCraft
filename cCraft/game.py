from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController 


app = Ursina()
grassTexture = load_texture('dirt.png')
skyTexture = load_texture('assets/test.jpg')
armTexture = load_texture('arm_texture.png')
punchSound = Audio('assets/break.wav',loop=False,autoplay=False)
placeSound = Audio('ha.wav',loop=False,autoplay=False)

class testText(TextField):
    def  __init__(self):
        super().__init__(
          text_entity = Text('Poop')
        )  

class Hand(Entity):
     def  __init__(self):
            super().__init__(
                parent = camera.ui,
                model = 'arm',
                texture = armTexture,
                scale = 0.2,
                rotation = Vec3(150,-10,0),
                position = Vec2(0.4,-0.6)
            )

class Sky(Entity):
     def  __init__(self):
            super().__init__(
         parent = scene,
         model= 'sphere',
         texture = skyTexture,
         scale=150,
         double_sided=True,
        )

class Voxel(Button):
    def __init__(self, position= (0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model= 'cube',
            origin_y=0.5,
            #texture=grassTexture,
            color= color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.gray)

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                placeSound.play()
                voxel= Voxel(position = self.position + mouse.normal)
            if key == 'left mouse down':
                punchSound.play()
                destroy(self)
            

window.title = 'cCraft Demo'

for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x,0,z))



player = FirstPersonController
player()
sky=Sky()
hand = Hand()

app.run()