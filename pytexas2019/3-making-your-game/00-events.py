"""
System events are great!

But how about manipulating them ourselves?
"""
from dataclasses import dataclass

import ppb
import ppb.events

leader = None

class FastShip(ppb.BaseSprite):
    image = "../resources/ship.png"
    listen = False
    position = ppb.Vector(0, 3.5)
    leader = True

    def on_update(self, update, signal):
        """Let's speed up time."""
        # We need to just raise another Update
        ...
        # but only once per system event.
        ...
        self.position += ppb.Vector(0, -1).scale(update.time_delta)


# Making your own events is just dataclasses!


class TimeDilationShip(ppb.BaseSprite):
    image = "../resources/ship.png"
    source = False
    speed = .5
    accumulator = 0

    def on_update(self, update, signal):
        """We're going to change update into our TimeDilation event!"""
        ...

    def on_time_dilation(self, time_dilation, signal):
        self.position += ppb.Vector(0, -1).scale(time_dilation.time_delta)


def setup(scene):
    global leader
    leader = FastShip()
    scene.add(leader)
    scene.add(FastShip(leader=False, pos=ppb.Vector(4, 3.5)))
    scene.add(TimeDilationShip(speed=1, pos=ppb.Vector(-4, 3.5)))


ppb.run(setup=setup)

# How about extending events?

# with ppb.GameEngine(ppb.BaseScene, scene_kwargs={"set_up": setup}) as ge:
