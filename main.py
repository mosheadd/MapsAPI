import pygame


WIDTH, HEIGHT = 600, 600
WINDOW_NAME = "MapsAPI"
FULLSCREEN = False


class Programme:
    def __init__(self, width, height, window_name="NO_NAME", fullscreen=False):
        self.isWindowOpen = True
        self.width = width
        self.height = height
        pygame.init()
        if not fullscreen:
            pygame.display.set_mode((width, height))
        else:
            pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption(window_name)

    def loop(self):
        while self.isWindowOpen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isWindowOpen = False
            pygame.display.flip()


if __name__ == "__main__":
    window = Programme(WIDTH, HEIGHT, WINDOW_NAME, FULLSCREEN)
    window.loop()