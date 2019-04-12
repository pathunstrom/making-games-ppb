# So, a sprite on its own isn't much fun: Let's make them interact.
import ppb

# Parameters
class FollowTheLeader(ppb.BaseSprite):
    # Sprites are declarative, so we can put leader=None here.
    # Then when we instantiate them, pass in a leader parameter as needed.
    leader = None

    def on_update(self, update, signal):
        if self.leader:
            target = self.leader.position
        else:
            # We can also use Scene.get to find what we're looking for.
            target = ppb.Vector(0, 0)
        self.position += (target - self.position).scale(2 * update.time_delta)

    # We can also use the messaging system!


class Player(ppb.BaseSprite):
    target = ppb.Vector(0, 0)

    def on_update(self, update, signal):
        self.position += (self.target - self.position).scale(3 * update.time_delta)

    def on_mouse_motion(self, mouse, signal):
        self.target = mouse.position

# Just use messaging!



def setup(scene):
    # ppb.Vector(5, 4)
    # ppb.Vector(-5, 4)
    # ppb.Vector(5, -4)
    ...

ppb.run(setup)