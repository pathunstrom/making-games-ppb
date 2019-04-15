"""
Subsystems persist between scenes.

We will build an Achievement system to demonstrate.
"""
import ppb
import ppb.events
import ppb.keycodes
import ppb.systems


class Player(ppb.BaseSprite):
    image = "../resources/ship.png"
    position = ppb.Vector(0, 3.5)

    def on_key_pressed(self, event: ppb.events.KeyPressed, signal):
        if event.key == ppb.keycodes.Space:
            event.scene.add(Bullet(pos=self.top.center), tags=["friendly"])


class Bullet(ppb.BaseSprite):
    image = "../resources/bullet.png"
    size = 0.25
    speed = 4

    def on_update(self, event, signal):
        self.position += ppb.Vector(0, -1).scale(self.speed * event.time_delta)

    def collides_with(self, other):
        halfs = (self.size + other.size) / 2
        return abs(self.center.x - other.center.x) < halfs and abs(self.center.y - other.center.y) < halfs


class Enemy(ppb.BaseSprite):
    image = "../resources/enemy.png"
    speed = 2
    position = ppb.Vector(0, -5)

    def on_update(self, event, signal):
        self.position += ppb.Vector(0, 1).scale(self.speed * event.time_delta)
        for bullet in event.scene.get(kind=Bullet):
            if bullet.collides_with(self):
                event.scene.remove(self)
                event.scene.remove(bullet)
            break


class AchievementStar(ppb.BaseSprite):
    image = "../resources/achievement-star.png"
    position = ppb.Vector(-5, -4)
    lifetime = 1
    accumulator = 0

    def on_update(self, update, signal):
        self.accumulator += update.time_delta
        if self.accumulator >= self.lifetime:
            update.scene.remove(self)


class Game(ppb.BaseScene):
    spawn_rate = 1
    accumulator = 0
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add(Player())
    def on_update(self, event, signal):
        self.accumulator += event.time_delta
        if self.accumulator >= self.spawn_rate:
            self.add(Enemy())
            self.accumulator = 0

class Achievement(ppb.systems.System):

    def __init__(self, *args, **kwargs):
        self.count = 0
        self.goal = 10

    def on_acheivement_progress(self, event, signal):
        self.count += 1
        if self.go
with ppb.GameEngine(Game,
                    systems=[
                        ppb.systems.Updater,
                        ppb.systems.Renderer,
                        ppb.systems.pg.EventPoller
                    ]) as ge:
    ge.run()