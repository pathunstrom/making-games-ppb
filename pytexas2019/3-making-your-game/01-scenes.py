import time

import ppb


class SplashScreen(ppb.BaseScene):
    continued = False
    wait = 0.5
    background_color = (100, 50, 125)

    def on_update(self, update, signal):
        self.wait -= update.time_delta
        if self.wait < 0:
            # StartScene: Let's start the game.
            ...

    def on_scene_continued(self, event, signal):
        self.continued = True
        self.wait += 0.5


class GameScreen(ppb.BaseScene):
    wait = 0.5
    background_color = (50, 200, 40)
    start_time = None

    def on_scene_started(self, event, signal):
        self.start_time = time.monotonic()

    def on_update(self, event, signal):
        if self.start_time is not None and time.monotonic() - self.start_time >= self.wait:
            # ReplaceScene: And now, game's over.
            # Let's replace the game with the game over screen.
            ...

    def on_scene_stopped(self, event, signal):
        print(f"Game run time: {time.monotonic() - self.start_time}")


class GameOverScreen(ppb.BaseScene):
    background_color = (200, 50, 50)
    wait = 0.5

    def on_update(self, event, signal):
        self.wait -= event.time_delta
        if self.wait <= 0:
            # StopScene: This one is easy, we just need to stop it.
            ...


with ppb.GameEngine(SplashScreen) as ge:
    ge.run()
