# all the files
import pygame
import Menu
import time
import random
import EndResult
# Initialize pygame
pygame.init()

screen = pygame.display.set_mode([950,950])

# picture of Mr Beast
cardimg1 = pygame.image.load('card1.jpg').convert()
cardimg1 = pygame.transform.scale(cardimg1, (110, 150))
# picture of Bill Gates
cardimg2 = pygame.image.load('card2.jpg').convert()
cardimg2 = pygame.transform.scale(cardimg2, (110, 150))
# picture of Steve jobs
cardimg3 = pygame.image.load('card3.jpg').convert()
cardimg3 = pygame.transform.scale(cardimg3, (110, 150))
# picture of tesla
cardimg4 = pygame.image.load('card4.jpg').convert()
cardimg4 = pygame.transform.scale(cardimg4, (110, 150))
# picture of Hitler
cardimg5 = pygame.image.load('card5.jpg').convert()
cardimg5 = pygame.transform.scale(cardimg5, (110, 150))
# Picture of Taylor swift
cardimg6 = pygame.image.load('card6.jpg').convert()
cardimg6 = pygame.transform.scale(cardimg6, (110, 150))
# picture of Queen Elizabeth
cardimg7 = pygame.image.load('card7.jpg').convert()
cardimg7 = pygame.transform.scale(cardimg7, (110, 150))
# picture of Lee hsien loong
cardimg8 = pygame.image.load('card8.jpg').convert()
cardimg8 = pygame.transform.scale(cardimg8, (110, 150))
# Initialize
firstClickCard = ""
secondCLickCard = ""
clickTime = 0
totalNumberCards = 16
randomNumList = []
noPressing = False
numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
stats = ["", 0 ,0, 0, 0] # [0] = time, [1] = "time taken", [2] = "accurate", [3] = "inaccurate", [4] = Total click

# randomize the cards
numSize = len(numList)
for i in range(numSize):
    num = random.choice(numList)
    randomNumList.append(num)
    numList.remove(num)

 # draw rectangle (card)
def DrawCard(x, y):
    pygame.draw.rect(screen, (0, 0, 0), (x, y, 110, 150), 0)

# show picture
def ShowCard(x, y, img): #
    screen.blit(img, (x, y))
width = 110
height = 150
card_x = [50, 300, 550, 800, 50, 300, 550, 800, 50, 300, 550, 800, 50, 300, 550, 800]
card_y = [50, 50, 50, 50, 250, 250, 250, 250, 475, 475, 475, 475, 700, 700, 700, 700]

# dictionary to find cards
deck = {"Card1":  {"x1": 0, "y1": 0, "x2": 0, "y2": 0, "image": cardimg1, "id": 1, "status": 1},
        "Card2":  {"x1": 0, "y1": 0, "x2": 0, "y2": 0, "image": cardimg1, "id": 1, "status": 1},
        "Card3":  {"x1": 0, "y1": 0, "x2": 0, "y2": 0, "image": cardimg2, "id": 2, "status": 1},
        "Card4":  {"x1": 0, "y1": 0, "x2": 0, "y2": 0, "image": cardimg2, "id": 2, "status": 1},
        "Card5":  {"x1": 0, "y1": 0, "x2": 0, "y2": 0, "image": cardimg3, "id": 3, "status": 1},
        "Card6":  {"x1": 0, "y1": 0, "x2": 0, "y2": 0, "image": cardimg3, "id": 3, "status": 1},
        "Card7":  {"x1": 0, "y1": 0, "x2": 0, "y2": 0, "image": cardimg4, "id": 4, "status": 1},
        "Card8":  {"x1": 0, "y1": 0, "x2": 0, "y2": 0, "image": cardimg4, "id": 4, "status": 1},
        "Card9":  {"x1": 0, "y1": 0, "x2": 0, "y2": 0, "image": cardimg5, "id": 5, "status": 1},
        "Card10": {"x1": 0, "y1": 0, "x2": 0, "y2": 0, "image": cardimg5, "id": 5, "status": 1},
        "Card11": {"x1": 0, "y1": 0, "x2": 0, "y2": 0, "image": cardimg6, "id": 6, "status": 1},
        "Card12": {"x1": 0, "y1": 0, "x2": 0, "y2": 0, "image": cardimg6, "id": 6, "status": 1},
        "Card13": {"x1": 0, "y1": 0, "x2": 0, "y2": 0, "image": cardimg7, "id": 7, "status": 1},
        "Card14": {"x1": 0, "y1": 0, "x2": 0, "y2": 0, "image": cardimg7, "id": 7, "status": 1},
        "Card15": {"x1": 0, "y1": 0, "x2": 0, "y2": 0, "image": cardimg8, "id": 8, "status": 1},
        "Card16": {"x1": 0, "y1": 0, "x2": 0, "y2": 0, "image": cardimg8, "id": 8, "status": 1}}

index = 0
for key in deck.keys():
    # randomNum = select one of the 16 cards and change its x1, x2, y1, y2
    randomNum = randomNumList[index]
    deck[key]["x1"] = card_x[randomNum]
    deck[key]["x2"] = card_x[randomNum] + width
    deck[key]["y1"] = card_y[randomNum]
    deck[key]["y2"] = card_y[randomNum] + height
    index = index+1

# Initialize the program
clock = pygame.time.Clock()
screen.fill((90,90,90))

game = True
gameClock = 0
gameClockUpdate = 0
frameRate = 15
font = pygame.font.SysFont("Arial", 25)
pygame.display.flip()

# import Menu.py
# welcome screen
Menu.menu(screen)

# Main Body of Program
while game == True:
    # Game time
    gameClockUpdate = gameClockUpdate + 1
    if gameClockUpdate == frameRate:
        gameClock = gameClock + 1
        gameClockUpdate = 0
    screen.fill((90, 90, 90))

    # When key 'q' is pressed, exit the game
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game = False
                stats[0] = time.asctime()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePressed = pygame.mouse.get_pressed()
            if mousePressed[0] and noPressing == False:  # [0] is left button
                mouseX, mouseY = pygame.mouse.get_pos()
                stats[3] += 1

                for key in deck.keys():
                    if deck[key]["status"] == 1 and mouseX > deck[key]["x1"] and mouseX < deck[key]["x2"] and mouseY > deck[key]["y1"] and mouseY < deck[key]["y2"]:
                            stats[2] += 1
                            stats[3] -= 1

                            if firstClickCard == "":
                                # first card is clicked
                                firstClickCard = key
                            else:
                                # second card is clicked
                                secondCLickCard = key
                                clickTime = gameClock
                                noPressing = True
                                if deck[key]["id"] == deck[firstClickCard]["id"] and key != firstClickCard:
                                    # first card and second card clicked match
                                    deck[key]["status"] = 0
                                    deck[firstClickCard]["status"] = 0
                                    totalNumberCards -= 2
                                    if totalNumberCards == 0:
                                        stats[0] = time.asctime()
                                        stats[1] = gameClock
                                        stats[4] = stats[2] + stats[3]
                                        game = False
                                

    # Timer
    img = font.render('Time: ' + str(gameClock), True, (255, 250, 200))
    screen.blit(img, (410, 20))
    # when cards are flipped
    for key in deck.keys():
        if deck[key]["status"] == 1:
            DrawCard(deck[key]["x1"], deck[key]["y1"])
    if firstClickCard != "":
        ShowCard(deck[firstClickCard]["x1"], deck[firstClickCard]["y1"],deck[firstClickCard]["image"])
    if secondCLickCard != "":
        ShowCard(deck[secondCLickCard]["x1"], deck[secondCLickCard]["y1"], deck[secondCLickCard]["image"])
        if gameClock - clickTime >= 1:
            secondCLickCard = ""
            firstClickCard = ""
            noPressing = False

    pygame.display.flip()

    clock.tick(frameRate)
# import EndResult.py
# result page
EndResult.EndResult(screen, stats)
# quit
pygame.quit()
