# Taka Kodani
# Bullet Dharma

import pygame
import random
import sys
from sprites import *
from screens import *
 
# Define colors
BLACK  = (   0,   0,   0)
WHITE  = ( 255, 255, 255)
RED    = ( 255,   0,   0)

class RunGame(object):
    """Runs actual game."""
    def __init__(self):
        """Initialize the game."""
        self.done = False
        self.cloud_pos = "right"
        self.boss_pos = "right"

        # Group object lists
        self.all_sprites_list = pygame.sprite.Group()
        self.cloud_list = pygame.sprite.Group()
        self.cloud_sprites_list = pygame.sprite.Group()
        self.health_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.enemy_list2 = pygame.sprite.Group() # Buddha
        self.enemy_list3 = pygame.sprite.Group() # Garuda
        self.enemy_list4 = pygame.sprite.Group() # Dragon
        self.enemy_list5 = pygame.sprite.Group() # Boss
        self.bullet_list = pygame.sprite.Group()
        self.enemy_bullet_list = pygame.sprite.Group()
        self.all_enemy_list = pygame.sprite.Group()

        # Create enemies
        for i in range(35):
            enemy = Enemy()

            enemy.rect.x = random.randrange(50, 450)
            enemy.rect.y = random.randrange(-3000, -100)

            self.enemy_list.add(enemy)
            self.all_sprites_list.add(enemy)
            self.all_enemy_list.add(enemy)

        # Create enemies
        for j in range(15):
            enemy = Gautama()

            enemy.rect.x = random.randrange(50, 450)
            enemy.rect.y = random.randrange(-3500, -500)

            self.enemy_list2.add(enemy)
            self.all_sprites_list.add(enemy)
            self.all_enemy_list.add(enemy)

        # Create enemies
        for k in range(7):
            enemy = Garuda()
            
            enemy.rect.x = random.randrange(50, 450)
            enemy.rect.y = random.randrange(-3500, -1000)

            self.enemy_list3.add(enemy)
            self.all_sprites_list.add(enemy)
            self.all_enemy_list.add(enemy)

        # Create enemies
        for l in range(5):
            enemy = Dragon()

            enemy.rect.x = random.randrange(50, 450)
            enemy.rect.y = random.randrange(-4000, -3000)

            self.enemy_list4.add(enemy)
            self.all_sprites_list.add(enemy)
            self.all_enemy_list.add(enemy)

        # Create boss
        self.boss = Asura()

        self.boss.rect.x = 70
        self.boss.rect.y = -1200

        self.enemy_list5.add(self.boss)
        self.all_sprites_list.add(self.boss)

        # Create clouds
        for c in range(40):
            cloud = Cloud()

            cloud.rect.x = random.randrange(-100, 500)
            cloud.rect.y = random.randrange(-1200, 700)

            self.cloud_list.add(cloud)
            self.cloud_sprites_list.add(cloud)

        # Create healthkit
        for h in range(1):
            health = Health()

            health.rect.x = 238
            health.rect.y = -300

            self.health_list.add(health)
            self.all_sprites_list.add(health)

        # Create player object
        self.player = Player()
        self.all_sprites_list.add(self.player)

        # Spread fire
        self.autofire = pygame.USEREVENT + 0
        pygame.time.set_timer(self.autofire, 1500)

        # Single shot
        self.autofire2 = pygame.USEREVENT + 1
        pygame.time.set_timer(self.autofire2, 1500)

        # Circular fire
        self.autofire3 = pygame.USEREVENT + 2
        pygame.time.set_timer(self.autofire3, 2000)

        # Spread fire 2
        self.autofire4 = pygame.USEREVENT + 3
        pygame.time.set_timer(self.autofire4, 1000)

        # Boss fire
        self.bossfire = pygame.USEREVENT + 4
        pygame.time.set_timer(self.bossfire, 500)

        # Cloud
        self.cloud_anim = pygame.USEREVENT + 5
        pygame.time.set_timer(self.cloud_anim, 1500)
        self.cloud_move = pygame.USEREVENT + 6
        pygame.time.set_timer(self.cloud_move, 50)

        # Boss music
        self.boss_music = pygame.USEREVENT + 7
        pygame.time.set_timer(self.boss_music, 74000)
        
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)

        # Background music
        self.bkgd_music = []
        self.bkgd_music.append(pygame.mixer.Sound("sounds/5so.wav"))
        self.bkgd_music.append(pygame.mixer.Sound("sounds/fx34.wav"))
        self.bkgd_music[0].play(-1)

        # Sound effects
        self.whoosh_sound = pygame.mixer.Sound("sounds/bright_whoosh.wav")
        self.expl_sound = pygame.mixer.Sound("sounds/explosion_sound.wav")
        self.pd_sound = pygame.mixer.Sound("sounds/power_down.wav")
        self.hit_sound = pygame.mixer.Sound("sounds/hit_sound.wav")
        self.pu_sound = pygame.mixer.Sound("sounds/power_up.wav")
        self.boss_expl = pygame.mixer.Sound("sounds/explosion_sound2.wav")

        # Player life icon image
        self.life_icon = pygame.image.load("images/dharma_wheel.png").convert()
        self.life_icon.set_colorkey(WHITE)

        # Boss health status bar
        self.health_bar = pygame.image.load("images/health_bar.png").convert()
        self.health_bar.set_colorkey(WHITE)
        self.boss_health = pygame.image.load("images/boss_health.png").convert()
        self.boss_health.set_colorkey(WHITE)
        
    def play(self):
        """Game play loop."""
        while not self.done:
            for event in pygame.event.get():
                # Quit game
                if event.type == pygame.QUIT:
                    really_done = True
                    return really_done
                # Player shoots bullet
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    bullet = Player_Bullet()
                    bullet.rect.x = self.player.rect.x + 12
                    bullet.rect.y = self.player.rect.y
                    self.all_sprites_list.add(bullet)
                    self.bullet_list.add(bullet)
                #Enemy auto fire
                elif event.type == self.autofire:
                    for enemy in self.enemy_list3:
                        bullets = [Enemy_Bullet(enemy.rect.x, enemy.rect.y) for bullet in range(5)]
                        numbers= [(-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2)]
                        for bullet in bullets:
                            bullet.set_move(numbers[0])
                            del numbers[0]
                        self.enemy_bullet_list.add(bullets)
                        self.all_sprites_list.add(bullets)
                # Enemy autofire
                elif event.type == self.autofire2:
                    for enemy in self.enemy_list:
                        bullets = Enemy_Bullet2(enemy.rect.x, enemy.rect.y)
                        self.enemy_bullet_list.add(bullets)
                        self.all_sprites_list.add(bullets)
                # Enemy autofire
                elif event.type == self.autofire3:
                    for enemy in self.enemy_list2:
                        bullets = [Enemy_Bullet3(enemy.rect.x, enemy.rect.y) for bullet in range(8)]
                        numbers = [(0, -2), (2, -2), (2, 0), (2, 2), (0, 2), (-2, 2),
                                   (-2, 0), (-2, -2)]
                        for bullet in bullets:
                            bullet.set_move(numbers[0])
                            del numbers[0]
                        self.enemy_bullet_list.add(bullets)
                        self.all_sprites_list.add(bullets)
                # Enemy autofire
                elif event.type == self.autofire4:
                    for enemy in self.enemy_list4:
                        bullets = [Enemy_Bullet(enemy.rect.x, enemy.rect.y) for bullet in range(11)]
                        numbers = [(-5, 2), (-4, 2), (-3, 2), (-2, 2), (-1, 2), (0, 2), (1, 2),
                                   (2, 2), (3, 2), (4, 2), (5, 2)]
                        for bullet in bullets:
                            bullet.set_move(numbers[0])
                            del numbers[0]
                        self.enemy_bullet_list.add(bullets)
                        self.all_sprites_list.add(bullets)
                    # Boss autofire
                    for boss in self.enemy_list5:
                        bullets = bullets = [Boss_Bullet(boss.rect.x, boss.rect.y) for bullet in range(11)]
                        numbers = [(-5, 2), (-4, 2), (-3, 2), (-2, 2), (-1, 2), (0, 2), (2, 2),
                                   (2, 2), (3, 2), (4, 2), (5, 2)]
                        for bullet in bullets:
                            bullet.set_move(numbers[0])
                            del numbers[0]
                        self.enemy_bullet_list.add(bullets)
                        self.all_sprites_list.add(bullets) 
                # Boss autofire
                elif event.type == self.bossfire:
                    for boss in self.enemy_list5:
                        bullets = [Boss_Bullet(boss.rect.x, boss.rect.y) for bullet in range(11)]
                        numbers = [(-5, 2), (-4, 2), (-3, 2), (-2, 2), (-1, 2), (0, 2), (1, 2),
                                   (2, 2), (3, 2), (4, 2), (5, 2)]
                        for bullet in bullets:
                            bullet.set_move(numbers[0])
                            del numbers[0]
                        self.enemy_bullet_list.add(bullets)
                        self.all_sprites_list.add(bullets)    
                # Animate cloud
                elif event.type == self.cloud_anim:
                    if self.cloud_pos == "right":
                        for cloud in self.cloud_list:
                            cloud.sway_right()
                            self.cloud_pos = "left"
                    elif self.cloud_pos == "left":
                         for cloud in self.cloud_list:
                            cloud.sway_left()
                            self.cloud_pos = "right"
                elif event.type == self.cloud_move:
                    for cloud in self.cloud_list:
                        cloud.move_down()
                elif event.type == self.boss_music:
                    self.change_music()

            screen.fill(WHITE)

            # Draw clouds
            self.cloud_sprites_list.draw(screen)

            # Hit collision detection between player and enemy bullet
            for bullet in self.enemy_bullet_list:
                player_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_bullet_list, False)

                for bullet in player_hit_list:
                    self.hit_sound.play()
                    self.enemy_bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                    self.player.hit_points -= 1 # Lose a life if hit
                    # Game over if lose all lives
                    if self.player.hit_points == 0:
                        self.expl_sound.play()
                        self.pd_sound.play()
                        self.clock.tick(0)
                        self.bkgd_music[0].stop()
                        self.bkgd_music[1].stop()
                        self.done = True
                        end = End()
                        really_done = end.game_over_screen(screen)
                        return really_done

                # Delete bullet sprite if off screen
                if bullet.rect.y < -10:
                    self.enemy_bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                if bullet.rect.y > 710:
                    self.enemy_bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                if bullet.rect.x < -10:
                    self.enemy_bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                if bullet.rect.x > 510:
                    self.enemy_bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)

            for enemy in self.all_enemy_list:
                # Move enemies down
                enemy.move_down()
                # Delete enemy if off screen 
                if enemy.rect.y > 730:
                    self.all_enemy_list.remove(enemy)
                    self.all_sprites_list.remove(enemy)
                    self.enemy_list.remove(enemy)
                    self.enemy_list2.remove(enemy)
                    self.enemy_list3.remove(enemy)
                    self.enemy_list4.remove(enemy)
                    
            # Hit collision detection between enemy and player bullet
            for bullet in self.bullet_list:
                enemy_hit_list = pygame.sprite.spritecollide(bullet, self.all_enemy_list, False)

                for enemy in enemy_hit_list:
                    enemy.hit_points -= 1 # Enemey loses a life if hit
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                    # Enemy recoils if hit
                    enemy.hit_anim()
                    # Enemy dies if loses all lives
                    if enemy.hit_points == 0:
                        self.whoosh_sound.play()
                        self.all_enemy_list.remove(enemy)
                        self.all_sprites_list.remove(enemy)
                        self.enemy_list.remove(enemy)
                        self.enemy_list2.remove(enemy)
                        self.enemy_list3.remove(enemy)
                        self.enemy_list4.remove(enemy)

                # Remove player bullet if off screen
                if bullet.rect.y < -10:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)

            # Hit collision detection between player and healthkit
            for h in self.health_list:
                health_grab = pygame.sprite.spritecollide(self.player, self.health_list, True)

                for health in health_grab:
                    self.pu_sound.play()
                    self.player.hit_points = 5

            # If all enemies are gone, make healthkit appear
            if len(self.all_enemy_list) <= 0:
                for h in self.health_list:
                    h.move_down()

            # If all enemies are gone, make boss appear
            if len(self.all_enemy_list) <= 0:
                for boss in self.enemy_list5:
                    boss.move_down()

            # Hit collision detection between boss and player bullet
            for bullet in self.bullet_list:
                boss_hit_list = pygame.sprite.spritecollide(bullet, self.enemy_list5, False)

                for boss in boss_hit_list:
                    boss.hit_points -= 1 # Boss loses a life if hit
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                    # Boss dies if loses all lives - player wins game
                    if boss.hit_points == 0:
                        self.boss_expl.play()
                        self.all_sprites_list.remove(boss)
                        self.enemy_list5.remove(boss)
                        self.clock.tick(0)
                        self.bkgd_music[0].stop()
                        self.bkgd_music[1].stop()
                        self.done = True
                        end = End()
                        really_done = end.you_win_screen(screen)
                        return really_done

            # Draw and update all sprites
            self.all_sprites_list.draw(screen)
            self.all_sprites_list.update()

            # Show boss health status
            if self.boss.rect.y >= -10:
                x = 100
                y = 11
                for life in range(self.boss.hit_points):
                    self.boss_health.set_alpha(100)
                    screen.blit(self.boss_health, [x, y])
                    x += 1
                self.health_bar.set_alpha(100)
                screen.blit(self.health_bar, [100, 10])

            # Display number of player HP left
            x = 20
            y = 648
            for life in range(self.player.hit_points):
                screen.blit(self.life_icon, [x, y])
                x += 37
                
            pygame.display.flip()
            self.clock.tick(60)

    def change_music(self):
        """Change to boss background music."""
        self.bkgd_music[0].fadeout(5000)
        self.bkgd_music[1].play(loops=-1, fade_ms=10000)

if __name__ == "__main__":
    pygame.init()
    size = [500, 700]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Bullet Dharma")
    start = Start()
    done = start.start_screen(screen)
    if done == 0:
        really_done = False
        while not really_done:
            game = RunGame()
            really_done = game.play()            
        pygame.quit()
    elif done == 1:
        pygame.quit()
