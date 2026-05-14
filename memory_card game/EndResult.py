# import file
import pygame
import csv

# draw button for quit
def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (200, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (110, 110, 110), (x, y, w, h))
    return screen.blit(text_render, (x, y))

# the result of game
# Run until the user asks to quit
def EndResult(screen,statistics):
    screen.fill((180, 180, 180))
    button1 = button(screen, (800,800), "Quit")
    Logo = pygame.image.load('MmG.jpg').convert()
    Logo = pygame.transform.scale(Logo, (300, 300))
    screen.blit(Logo, (100, 600))
    font = pygame.font.SysFont('arial', 20)
    text1 = 'Date/time'
    text2 = 'Time taken'
    text3 = 'Accurate press'
    text4 = 'Inaccurate press'
    text5 = 'Total click'
    text6 = 'Past 5 results'
    coords = [10,270,400,600,800]
    rTexts = []
    rTexts.append(statistics[0])
    rTexts.append(str(statistics[1]) + " s")
    rTexts.append(str(statistics[2]) + " clicks")
    rTexts.append(str(statistics[3]) + " clicks")
    rTexts.append(str(statistics[4]) + " clicks")

    # file to store all the data
    # for doctor to check for dementia
    f = open("mmgamedata.csv", "a", newline='')
    csvWriter = csv.writer(f)
    csvWriter.writerow(statistics)
    f.close()

    f = open("mmgamedata.csv")
    csvReader = csv.reader(f)
    pastResults = list(csvReader)
    numOfPastResults = len(pastResults)
    upperLimit = numOfPastResults - 1 
    lowerLimit = numOfPastResults - 6
    if lowerLimit < -1:
        lowerLimit = -1

    running = True
    while running:
        # press button
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                key_to_quit = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_quit:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(pygame.mouse.get_pos()):
                    running = False
        pygame.display.update()
        # text for results
        text_surf1 = font.render(text1, True, (0, 0, 0), (110, 110, 110))
        screen.blit(text_surf1, (10, 0))

        text_surf2 = font.render(text2, True, (0, 0, 0), (110, 110, 110))
        screen.blit(text_surf2, (270, 0))

        text_surf3 = font.render(text3, True, (0, 0, 0), (110, 110, 110))
        screen.blit(text_surf3, (400, 0))

        text_surf4 = font.render(text4, True, (0, 0, 0), (110, 110, 110))
        screen.blit(text_surf4,(600, 0))

        text_surf5 = font.render(text5, True, (0, 0, 0), (110, 110, 110))
        screen.blit(text_surf5,(800, 0))

        for i in range(5):
            text_surf = font.render(rTexts[i], True, (0, 0, 0), (180, 180, 180))
            screen.blit(text_surf, (coords[i], 50))

        text_surf = font.render(text6, True, (0, 0, 0), (110, 110, 110))
        screen.blit(text_surf,(10, 100))
        # output last 5 results
        rowPos = 150
        for i in range(upperLimit, lowerLimit, -1):
            pastResultTexts = []
            pastStats = pastResults[i]
            pastResultTexts.append(pastStats[0])
            pastResultTexts.append(str(pastStats[1]) + " s")
            pastResultTexts.append(str(pastStats[2]) + " clicks")
            pastResultTexts.append(str(pastStats[3]) + " clicks")
            pastResultTexts.append(str(pastStats[4]) + " clicks")
            for i in range(5):
                text_surf = font.render(pastResultTexts[i], True, (0, 0, 0), (180, 180, 180))
                screen.blit(text_surf, (coords[i], rowPos))
            rowPos += 50

        pygame.display.flip()

