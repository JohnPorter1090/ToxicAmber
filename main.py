"""
ToxicAmber
Created by PixelPython
"""

import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ToxicAmber")

BLACK = (0, 0, 0)

BORDER = pygame.Rect(WIDTH//2 -5, 0, 10, HEIGHT)

TOXICAMBER_IMAGE = pygame.image.load(os.path.join('images', 'ToxicAmberLogo.png'))


CHARACTER_HEIGHT, CHARACTER_WIDTH = 10, 10                                               #Changes the Character Size
CHARACTER_IMAGE = pygame.image.load(os.path.join('images', 'Character.png'))
CHARACTER = pygame.transform.scale(CHARACTER_IMAGE, (CHARACTER_HEIGHT, CHARACTER_WIDTH)) #Handles the Character Size

pygame.display.set_icon(TOXICAMBER_IMAGE)

FPS = 60

def form_window():
    pygame.draw.rect(WIN, BLACK, BORDER)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) #Sets the FPS
        for event in pygame.event.get(): #checks for events 
            if event.type == pygame.QUIT: 
                run = False
            
            if event.type == pygame.KEYDOWN: #Checks for differect keystrokes
                if event.key == pygame.K_ESCAPE:
                    run = False
        
        form_window()





    pygame.quit()

if __name__ == "__main__":
    main()