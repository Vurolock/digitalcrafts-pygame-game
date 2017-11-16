import pygame
import random

class Hero(object):
    def __init__(self):
        self.image = pygame.image.load('images/hero.png')

    def draw(self, screen):
        screen.blit(self.image, (240, 224))

class Monster(object):
    def __init__(self):
        self.image = pygame.image.load('images/monster.png')
        self.x = 53
        self.y = 50
        self.speed = 4 
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
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
    timer_count = 120
    while not stop_game:
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        if monster.x > 472:
            monster.x = 20
        if monster.x < 20:
            monster.x = 472
        if monster.y > 460:
            monster.y = 20
        if monster.y < 20:
            monster.y = 460
        # Draw background
        screen.blit(background_image, (0, 0))

        # Game display
        hero.draw(screen)
        monster.draw(screen)
        pygame.display.update()
        
        # Monster movement
        clock.tick(60)
        timer_count = timer_count + 1
        print timer_count
        monster.x += monster.speed
        monster.y += monster.speed
        if timer_count > 120:
            
            timer_count = 0
            random_direction = random.random()
            
            if random_direction < 0.25:
                pass
            elif 0.25 <= random_direction < 0.50:
                monster.speed = -(monster.speed)
            
            elif 0.50 <= random_direction < 0.75:
                pass
            else:
                monster.speed = -(monster.speed)




    pygame.quit()

if __name__ == '__main__':
    main()
