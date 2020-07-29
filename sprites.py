import random
import pygame

# Define colors
WHITE   = ( 255, 255, 255)
RED     = ( 255,   0,   0)

pygame.init()

def load_image(filename):
    image = pygame.image.load(filename).convert()
    image.set_colorkey(WHITE)
    return image

class Cloud(pygame.sprite.Sprite):
    """Cloud sprite."""
    def __init__(self):
        # Initialize cloud image
        super().__init__()

        # Randomly select one from eight images
        self.image_list = ["images/cloud1.png",
                           "images/cloud2.png",
                           "images/cloud3.png",
                           "images/cloud4.png",
                           "images/cloud5.png",
                           "images/cloud6.png",
                           "images/cloud7.png",
                           "images/cloud8.png"]
        self.random_image = random.choice(self.image_list)

        self.image = pygame.image.load(self.random_image).convert()
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

    # Define cloud movement
    def move_down(self):
        self.rect.y += 1
    def sway_right(self):
        self.rect.x += 5
    def sway_left(self):
        self.rect.x -= 5

class Enemy(pygame.sprite.Sprite):
    """Enemy sprite."""
    def __init__(self):
        #Initialize enemy image.
        super().__init__()

        # Randomly select one from three images
        self.image_list = ["images/wtf.png",
                           "images/ganesha.png",
                           "images/ketu.png"]
        self.random_image = random.choice(self.image_list)
        
        self.image = load_image(self.random_image)
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

        self.hit_points = 2 # HP
        self.opacity = 255

    def move_down(self):
        # Move enemy down
        self.rect.y += 1

    def hit_anim(self):
        # Hit animation
        self.rect.y -= 5

        self.transp = 100
        self.image.set_alpha(self.opacity - self.transp)
        self.opacity -= self.transp

class Gautama(pygame.sprite.Sprite):
    def __init__(self):
        # Initialize enemy image.
        super().__init__()

        self.image = load_image("images/siddhartha.png")

        self.rect = self.image.get_rect()

        self.hit_points = 4
        self.opacity = 255

    def move_down(self):
        # Move enemy down
        self.rect.y += 1

    def hit_anim(self):
        # Hit animation
        self.rect.y -= 10

        self.transp = 50
        self.image.set_alpha(self.opacity - self.transp)
        self.opacity -= self.transp

class Garuda(pygame.sprite.Sprite):
    def __init__(self):
        #Initialize enemy image 
        super().__init__()

        self.image = load_image("images/garuda.png")

        self.rect = self.image.get_rect()

        self.hit_points = 5
        self.opacity = 255

        self.garuda_pos = random.choice(["right", "left"])

    def move_down(self):
        # Move enemy down
        if self.rect.y >= -60:
            self.rect.y += 1
            self.move_anim()
        else:
            self.rect.y += 1

    def move_anim(self):
        if self.garuda_pos == "right":
            self.rect.x += 1
            self.garuda_pos = "right"
            if self.rect.x >= 436:
                self.garuda_pos = "left"
        elif self.garuda_pos == "left":
            self.rect.x -= 1
            if self.rect.x <= 0:
                self.garuda_pos = "right"

    def hit_anim(self):
        # Hit animation
        self.rect.y -= 10

        self.transp = 40
        self.image.set_alpha(self.opacity - self.transp)
        self.opacity -= self.transp

class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        # Initialize enemy image
        super().__init__()

        self.image = load_image("images/dragon.png")

        self.rect = self.image.get_rect()

        self.hit_points = 10
        self.opacity = 255

    def move_down(self):
        # Move enemy down, stop at y >= 150
        if self.rect.y >= 150:
            self.rect.y += 0
        else:
            self.rect.y += 1

    def hit_anim(self):
        # Hit animation
        self.rect.y -= 10
        self.transp = 20
        self.image.set_alpha(self.opacity - self.transp)
        self.opacity -= self.transp

class Asura(pygame.sprite.Sprite):
    def __init__(self):
        #Initialize boss image
        super().__init__()

        self.image = load_image("images/asura.png")

        self.rect = self.image.get_rect()

        self.hit_points = 300

        self.boss_pos = random.choice(["right", "left"])

    def move_down(self):
        # Move enemy down, stop at y >= 10
        if self.rect.y >= 5:
            self.move_anim()
        else:
            self.rect.y += 1

    def hit_anim(self):
        pass

    def move_anim(self):
        if self.boss_pos == "right":
            self.rect.x += 2
            self.boss_pos = "right"
            if self.rect.x >= 291:
                self.boss_pos = "left"
        elif self.boss_pos == "left":
            self.rect.x -= 2
            if self.rect.x <= -150:
                self.boss_pos = "right"

class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Initialize player image
        super().__init__()

        self.image = load_image("images/plane.png")
        
        self.rect = self.image.get_rect()

        self.hit_points = 5

    def update(self):
        # Get mouse position for sprite location
        pos = pygame.mouse.get_pos()

        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.rect.topleft = self.rect.x, self.rect.y

class Player_Bullet(pygame.sprite.Sprite):
    def __init__(self):
        # Initialize player bullet graphic/location
        super().__init__()

        self.image = pygame.Surface([4, 10])
        self.image.fill(RED)

        self.rect = self.image.get_rect()

        self.hit_points = 3

    def update(self):
        # Speed/direction of bullet
        self.rect.y -= 12

class Enemy_Bullet(pygame.sprite.Sprite):
    def __init__(self, x , y):
        # Initialize enemy bullet image/location
        super().__init__()

        self.image = load_image("images/bullet.png")

        self.rect = self.image.get_rect()
        self.rect.x = x + 24
        self.rect.y = y + 50
        
    def update(self):
        # Speed/direction of bullet
        self.rect.x += self.move_x
        self.rect.y += self.move_y

    def set_move(self, num):
        self.move_x = num[0]
        self.move_y = num[1]

class Enemy_Bullet2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Initialize enemy bullet image/location
        super().__init__()

        self.image = load_image("images/bullet.png")

        self.rect = self.image.get_rect()
        self.rect.x = x + 7
        self.rect.y = y + 22

    def update(self):
        # Speed/direction of bullet
        self.rect.y += 2

class Enemy_Bullet3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Initialize enemy bullet image/location
        super().__init__()

        self.image = load_image("images/bullet.png")

        self.rect = self.image.get_rect()
        self.rect.x = x + 24
        self.rect.y = y + 40
        
    def update(self):
        # Speed/direction of bullet
        self.rect.x += self.move_x
        self.rect.y += self.move_y

    def set_move(self, num):
        self.move_x = num[0]
        self.move_y = num[1]

class Enemy_Bullet4(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Initialize enemy bullet image/location
        super().__init__()

        self.image = load_image("images/bullet.png")

        self.rect = self.image.get_rect()
        self.rect.x = x + 190
        self.rect.y = y + 150
        
    def update(self):
        # Speed/direction of bullet
        self.rect.x += self.move_x
        self.rect.y += self.move_y

    def set_move(self, num):
        self.move_x = num[0]
        self.move_y = num[1]

class Boss_Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Initialize enemy bullet image/location
        super().__init__()

        self.image = load_image("images/bullet2.png")

        self.rect = self.image.get_rect()
        self.rect.x = x + 175
        self.rect.y = y + 125

    def update(self):
        # Speed/direction of bullet
        self.rect.x += self.move_x
        self.rect.y += self.move_y

    def set_move(self, num):
        self.move_x = num[0]
        self.move_y = num[1]

class Health(pygame.sprite.Sprite):
    def __init__(self):
        # Initialize health kit image
        super().__init__()

        self.image = load_image("images/health.png")

        self.rect = self.image.get_rect()

    def move_down(self):
        # Move sprite
        self.rect.y += 1
