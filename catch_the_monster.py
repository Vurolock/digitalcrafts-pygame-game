import pygame

class Hero(object):
    def __init__(self):
        self.image = pygame.image.load('images/hero.png')

    def draw(self, screen):
        screen.blit(self.image, (240, 224))

class Monster(object):
    def __init__(self):
        self.image = pygame.image.load('images/monster.png')
    
    def draw(self, screen):
        screen.blit(self.image, (53, 50))
    
def main():
    width = 512
    height = 480
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load('images/background.png').convert_alpha()
    pygame.display.set_caption('Catch the Monster!')
    clock = pygame.time.Clock()

    # Game initialization
    hero = Hero()
    monster = Monster()

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background

        screen.blit(background_image, (0, 0))

        # Game display
        hero.draw(screen)
        monster.draw(screen)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
