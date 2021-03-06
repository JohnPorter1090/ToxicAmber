"""
ToxicAmber
Created by AmberPixel

Credits
blackSnow by airtone (c) copyright 2021 Licensed under a Creative Commons Attribution (3.0) license. http://dig.ccmixter.org/files/airtone/63513
PixelPlanets by Deep-Fold
"""



from numpy import full
import pygame
import os

print("Opening ToxicAmber...")

default_display = pygame.SCALED
fullscreen_display = pygame.SCALED | pygame.FULLSCREEN
windowless_display = pygame.SCALED | pygame.NOFRAME


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT), default_display)
pygame.display.set_caption("ToxicAmber")

BLACK = (0, 0, 0)



pygame.mixer.init()
blackSnow_by_airtone = pygame.mixer.music.load(os.path.join('audio', 'blacksnow.mp3')) #plays music
pygame.mixer.music.play(-1)



BACKGROUND = pygame.Rect(0, 0, WIDTH, HEIGHT)

TOXICAMBER_IMAGE = pygame.image.load(os.path.join('images', 'ToxicAmberLogo.png'))

TITLESCREEN = pygame.transform.scale(pygame.image.load(os.path.join('images', 'ToxicAmberTitleScreenNoLetter.png')), (WIDTH, HEIGHT))

CHARACTER_HEIGHT, CHARACTER_WIDTH = 10, 10                                               #Changes the Character Size
CHARACTER_IMAGE = pygame.image.load(os.path.join('images', 'Character.png'))
CHARACTER = pygame.transform.scale(CHARACTER_IMAGE, (CHARACTER_HEIGHT, CHARACTER_WIDTH)) #Handles the Character Size

pygame.display.set_icon(TOXICAMBER_IMAGE)

X_CENTER, Y_CENTER = WIDTH/2, HEIGHT/2 


CHARACTER_VEL = 5 #Changes the Characters Speed
FPS = 60

def form_window(character):
    WIN.blit(TITLESCREEN, (0, 0))
    WIN.blit(CHARACTER, (character.x, character.y))
    

    pygame.display.update()

def handle_character_movement(keys_pressed, character):
    if keys_pressed[pygame.K_a] and character.x - CHARACTER_VEL > 0:
        character.x -= CHARACTER_VEL
        print("Character X: " + str(character.x) + " Character Y: " +str(character.y))
    if keys_pressed[pygame.K_d] and character.x + CHARACTER_VEL + character.width < WIDTH:
        character.x += CHARACTER_VEL
        print("Character X: " + str(character.x) + " Character Y: " +str(character.y))
    if keys_pressed[pygame.K_w] and character.y - CHARACTER_VEL > 0:
        character.y -= CHARACTER_VEL
        print("Character X: " + str(character.x) + " Character Y: " +str(character.y))
    if keys_pressed[pygame.K_s] and character.y + CHARACTER_VEL + character.height < HEIGHT:
        character.y += CHARACTER_VEL
        print("Character X: " + str(character.x) + " Character Y: " +str(character.y))
    if keys_pressed[pygame.K_LEFT] and character.x - CHARACTER_VEL > 0:
        character.x -= CHARACTER_VEL
        print("Character X: " + str(character.x) + " Character Y: " +str(character.y))
    if keys_pressed[pygame.K_RIGHT] and character.x + CHARACTER_VEL + character.width < WIDTH:
        character.x += CHARACTER_VEL
        print("Character X: " + str(character.x) + " Character Y: " +str(character.y))
    if keys_pressed[pygame.K_UP] and character.y - CHARACTER_VEL > 0:
        character.y -= CHARACTER_VEL
        print("Character X: " + str(character.x) + " Character Y: " +str(character.y))
    if keys_pressed[pygame.K_DOWN] and character.y + CHARACTER_VEL + character.height < HEIGHT:
        character.y += CHARACTER_VEL
        print("Character X: " + str(character.x) + " Character Y: " +str(character.y))


def main():
    character = pygame.Rect(X_CENTER, Y_CENTER, CHARACTER_WIDTH, CHARACTER_HEIGHT)
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
                if event.key == pygame.K_F8:
                    WIN = pygame.display.set_mode((WIDTH, HEIGHT), fullscreen_display)
                    TOXICAMBER_IMAGE = pygame.image.load(os.path.join('images', 'ToxicAmberLogo.png'))
                if event.key == pygame.K_F7:
                    WIN = pygame.display.set_mode((WIDTH, HEIGHT), default_display)
                    TOXICAMBER_IMAGE = pygame.image.load(os.path.join('images', 'ToxicAmberLogo.png'))
                if event.key == pygame.K_F6:
                    WIN = pygame.display.set_mode((WIDTH, HEIGHT), windowless_display)
                    TOXICAMBER_IMAGE = pygame.image.load(os.path.join('images', 'ToxicAmberLogo.png'))
        keys_pressed = pygame.key.get_pressed() #Checks for keys that are currently being held down

        
        
        handle_character_movement(keys_pressed, character)
        form_window(character)



    pygame.quit()

if __name__ == "__main__":
    main()