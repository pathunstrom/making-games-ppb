# What are events, anyway?

# Things like:
#   * Mouse motion
#   * window close
#   * key presses

import ppb
import ppb.events as event
import ppb.keycodes as key


class MyGameObject(ppb.BaseSprite):

    def on_key_pressed(self, event: event.KeyPressed, signal):
        if event.key == key.Space:
            self.size += 0.25

def setup(scene):
    scene.add(MyGameObject())


ppb.run(setup=setup)
