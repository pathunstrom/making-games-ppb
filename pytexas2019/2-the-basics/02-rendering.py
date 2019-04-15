# Raster graphics are based on pixel arrays
# We also call them bitmap graphics.

# We mostly let our libraries handle that:
import ppb
import ppb.events as event
import ppb.keycodes as key


class ImageSprite(ppb.BaseSprite):
    image = "../resources/ship.png"


class ResizedSprite(ImageSprite):
    size = 1.5


class RotatedSprite(ImageSprite):
    _rotation = 180


class AllTheThings(ResizedSprite, RotatedSprite):
    pass


def setup(scene):
    scene.add(ppb.BaseSprite(pos=ppb.Vector(-4, 0)))
    scene.add(ImageSprite(pos=ppb.Vector(-2, 0)))
    scene.add(ResizedSprite(pos=ppb.Vector(0, 0)))
    scene.add(RotatedSprite(pos=ppb.Vector(2, 0)))
    scene.add(AllTheThings(pos=ppb.Vector(4, 0)))


ppb.run(setup=setup)
