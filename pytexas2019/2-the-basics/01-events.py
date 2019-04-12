# What are events, anyway?

# Things like:
#   * Mouse motion
#   * window close
#   * key presses

import ppb
import ppb.events as event
import ppb.keycodes as key


class MyGameObject(ppb.BaseSprite):
    pass


def setup(scene):
    scene.add(MyGameObject())


ppb.run(setup=setup)
