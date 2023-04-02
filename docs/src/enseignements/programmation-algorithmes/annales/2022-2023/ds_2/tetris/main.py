import pyglet

from tetris import Tetris


window = Tetris()
print(window.get_size())

pyglet.app.run()
print("c'est fini !")