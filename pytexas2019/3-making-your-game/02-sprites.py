# So, a sprite on its own isn't much fun: Let's make them interact.
from dataclasses import dataclass
import ppb

@dataclass
class TargetMoved:
    position: ppb.Vector


# Parameters
class FollowTheLeader(ppb.BaseSprite):
    # Sprites are declarative, so we can put leader=None here.
    # Then when we instantiate them, pass in a leader parameter as needed.
    leader = None
    target = ppb.Vector(0, 0)

    def on_update(self, update, signal):
        if self.leader:
            target = self.target
        else:
            for player in update.scene.get(tag="player"):
                signal(TargetMoved(player.position))
                target = player.position
        self.position += (target - self.position).scale(2 * update.time_delta)

    # We can also use the messaging system!
    def on_target_moved(self, event, signal):
        if self.leader:
            self.target = event.position


class Player(ppb.BaseSprite):
    target = ppb.Vector(0, 0)

    def on_update(self, update, signal):
        self.position += (self.target - self.position).scale(3 * update.time_delta)

    def on_mouse_motion(self, mouse, signal):
        self.target = mouse.position

# Just use messaging!



def setup(scene):
    leader = FollowTheLeader(pos=ppb.Vector(5, 4))
    scene.add(leader)
    scene.add(FollowTheLeader(pos=ppb.Vector(-5, 4), leader=leader))
    scene.add(FollowTheLeader(pos=ppb.Vector(5, -4), leader=leader))
    scene.add(Player(), tags=["player"])

ppb.run(setup)