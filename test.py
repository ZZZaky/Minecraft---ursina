from ursina import *
from ursina import texture



class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3(45, 45, 0)
        )

class Test_button(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'cube',
            texture = 'brick',
            color = color.blue,
            highlight_color = color.red,
            pressed_color = color.lime
        )
    
    def input(self, key):
        if self.hovered and key == 'left mouse down':
            print('button')

# def update():
#     if held_keys['a']:
#         test_square.x -= 4 * time.dt
#     elif held_keys['d']:
#         test_square.x += 4 * time.dt
#     elif held_keys['w']:
#         test_square.y += 4 * time.dt
#     elif held_keys['s']:
#         test_square.y -= 4 * time.dt

app = Ursina()

grass_texture = load_texture('assets/Grass.png')



# test_square = Entity(model = 'quad', color = color.blue, scale = (2, 2), position = (5, 4))
# grass = Entity(model = 'quad', texture = grass_texture)

test_cube = Test_button()

window.fullscreen = False
app.run()