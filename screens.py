import pygame
import random
 
# Define colors
BLACK  = (   0,   0,   0)
WHITE  = ( 255, 255, 255)

class Start(object):
    """Start screen."""
    def __init__(self):
        """Initialize start screen."""
        self.start = True
        self.my_font = pygame.font.SysFont("Arial Bold", 32)
        self.title_font = pygame.font.SysFont("Arial Bold", 50)
        self.label = self.my_font.render("Click anywhere to start", 1, WHITE)
        self.label2 = self.title_font.render("BULLET DHARMA", 1, WHITE)
        
    def start_screen(self, screen):
        """Display start screen."""
        while self.start:
            for event in pygame.event.get():
                # Quit game
                if event.type == pygame.QUIT:
                    done = 1
                    return done
                    self.start = False
                # Play game
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    done = 0
                    return done
                    self.start = False
            screen.fill(BLACK)
            screen.blit(self.label2, (90, 250))
            screen.blit(self.label, (115, 300))
            pygame.display.flip()

class End(object):
    """End screens."""
    def __init__(self):
        """Initialize end screen."""
        self.end = True
        self.go_font = pygame.font.SysFont("Arial Bold", 48)
        self.ta_font = pygame.font.SysFont("Arial Bold", 28)
        self.game_over_label = self.go_font.render("GAME OVER", 1, WHITE)
        self.try_again_label = self.ta_font.render("Press SPACE to try again", 1, WHITE)
        self.you_win_label = self.go_font.render("YOU WIN", 1, WHITE)
        
    def game_over_screen(self, screen):
        """Display game over screen."""
        while self.end:
            for event in pygame.event.get():
                # Quit game
                if event.type == pygame.QUIT:
                    self.end = False
                    really_done = True
                    return really_done
                # Play again
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.end = False
                        really_done = False
                        return really_done
            screen.fill(BLACK)
            screen.blit(self.game_over_label, (145, 300))
            screen.blit(self.try_again_label, (130, 350))
            pygame.display.flip()

    def you_win_screen(self, screen):
        """Display win screen."""
        while self.end:
            for event in pygame.event.get():
                # Quit game
                if event.type == pygame.QUIT:
                    self.end = False
                    really_done = True
                    return really_done
                # Play again
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.end = False
                        really_done = False
                        return really_done
            screen.fill(BLACK)
            screen.blit(self.you_win_label, (165, 300))
            screen.blit(self.try_again_label, (130, 350))
            pygame.display.flip()
