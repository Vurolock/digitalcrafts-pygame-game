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
        self.base_speed = 3
        self.speed_x = 0
        self.speed_y = 0
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
    timer_count = 119
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
        if monster.y > 450:
            monster.y = 20
        if monster.y < 20:
            monster.y = 450
        # Draw background
        screen.blit(background_image, (0, 0))

        # Game display
        hero.draw(screen)
        monster.draw(screen)
        pygame.display.update()
        
        # Monster movement
        clock.tick(60)
        timer_count = timer_count + 1
        #print timer_count
        monster.x += monster.speed_x
        monster.y += monster.speed_y

        if timer_count >= 120:
            timer_count = 0
            random_direction = random.random()
            
            if random_direction < 0.25:
                monster.speed_x = -monster.base_speed
                monster.speed_y = 0
            
            elif 0.25 <= random_direction < 0.50:
                monster.speed_x = monster.base_speed
                monster.speed_y = 0
            
            elif 0.50 <= random_direction < 0.75:
                monster.speed_y = -monster.base_speed
                monster.speed_x = 0
            
            else:
                monster.speed_y = monster.base_speed
                monster.speed_x = 0




    pygame.quit()

if __name__ == '__main__':
    main()
