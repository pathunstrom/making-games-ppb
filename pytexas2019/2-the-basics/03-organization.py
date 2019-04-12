from pprint import pprint

import ppb
import ppb.events


def setup(scene):
    scene.add(ppb.BaseSprite())


# At the top of the tree is an engine.
with ppb.GameEngine(ppb.BaseScene, scene_kwargs={"set_up": setup}) as ge:

    # Normally, we would call:
    # ge.run()
    # but for now, we want to poke things.

    # Inside the engine are subsystems:
    # pprint(ge.systems)
    # Those systems are where we get specific engine behavior.

    # Once we start the engine, we also have scenes:
    # ge.start()
    # pprint(ge.scenes)

    # We keep them in a list, and use it as a stack.

    # pprint(ge.current_scene)

    # They're a container. And iterable:
    # pprint(list(ge.current_scene))

    # The engine uses events to manage them. We'll cover in detail later.

    # Sprites are data bags with event handlers attached.
    # def on_update(self, event, signal):
    #     print("I heard an update!")

    # ppb.BaseSprite.on_update = on_update

    # The engine is how we publish events.
    # ge.signal(ppb.events.Update)
    # pprint(ge.events)
    # ge.publish()
    pass