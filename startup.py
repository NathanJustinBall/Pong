import time
import fade
import engine


def start(screen):
    color = 255, 255, 255
    fade.text_in(screen, "Pong", 0.03, (color), 'Calibri', 160)
    time.sleep(0.1)
    fade.text_out(screen, "Pong", 0.01, (color), 'Calibri', 160)

    time.sleep(0.2)

    app = engine.Main(screen)
    app.tick()

