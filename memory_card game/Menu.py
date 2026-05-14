# Import
import pygame

# Initialize
menuRunning = True

#draw button
def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (0, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
    return screen.blit(text_render, (x, y))

def credits():
    print("Special thanks to:\nName: Hayden Lee\nClass: 3 Nightingale")

def rules():
    print("Rules:\nMatch the Cards\nNo time limit\nthere are 16 cards with pictures \n8 pairs of different pictures")

# welcome page
def menu(screen):
    # Initialize
    global menuRunning
    screen.fill((170, 170, 170))
    Logo = pygame.image.load('MmG.jpg').convert()
    Logo = pygame.transform.scale(Logo, (300, 300))
    screen.blit(Logo, (300, 100))
    button1 = button(screen, (400, 550), "Credits")
    button2 = button(screen, (400, 450), "Start")
    button3 = button(screen, (400, 650), "Rules")
    #loop
    while menuRunning:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_start:
                    menuRunning = False
                key_to_credits = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_credits:
                    credits()
                key_to_rules = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_rules:
                    rules()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(pygame.mouse.get_pos()):
                    credits()
                if button3.collidepoint(pygame.mouse.get_pos()):
                    rules()
                elif button2.collidepoint(pygame.mouse.get_pos()):
                    menuRunning = False

        pygame.display.update()









