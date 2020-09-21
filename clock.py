try:
    import pygame
    from pygame import mixer
    import time
    import math

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption("Countdown Timer")
    GREY = (150, 150, 150)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    font = pygame.font.SysFont('sans', 50)
    text1 = font.render('+', True, BLACK)
    text2 = font.render('-', True, BLACK)
    text3 = font.render('+', True, BLACK)
    text4 = font.render('-', True, BLACK)
    text5 = font.render('Start', True, BLACK)
    text6 = font.render('Stop', True, BLACK)
    text7 = font.render('Reset', True, BLACK)

    totalSeconds = 0
    total = 0
    start = False
    running = True
    sound = mixer.Sound('favoriteSong.wav')
    clock = pygame.time.Clock()

    while running:
        clock.tick(64)
        screen.fill(GREY)
        mouseX, mouseY = pygame.mouse.get_pos()
        #print(mouseX)

        pygame.draw.rect(screen, WHITE, (100, 50, 50, 50))
        pygame.draw.rect(screen, WHITE, (100, 200, 50, 50))
        pygame.draw.rect(screen, WHITE, (200, 50, 50, 50))
        pygame.draw.rect(screen, WHITE, (200, 200, 50, 50))
        pygame.draw.rect(screen, WHITE, (300, 30, 150, 50))
        pygame.draw.rect(screen, WHITE, (300, 130, 150, 50))
        pygame.draw.rect(screen, WHITE, (300, 230, 150, 50))

        screen.blit(text1, (112, 46))
        screen.blit(text2, (117, 194))
        screen.blit(text3, (212, 46))
        screen.blit(text4, (217, 194))
        screen.blit(text5, (328, 26))
        screen.blit(text6, (330, 126))
        screen.blit(text7, (324, 224))

        pygame.draw.rect(screen, BLACK, (50, 520, 400, 50))
        pygame.draw.rect(screen, WHITE, (60, 530, 380, 30))

        # pygame.draw.circle(screen, BLACK, [250, 380], 100, 2)
        # pygame.draw.circle(screen, WHITE, [250, 380], 97)
        # pygame.draw.circle(screen, BLACK, [250, 380], 4)
        # pygame.draw.aaline(screen, BLACK, [250, 380], [250, 290], 3)

        pygame.draw.circle(screen, BLACK, [250, 400], 100)
        pygame.draw.circle(screen, WHITE, [250, 400], 95)
        pygame.draw.circle(screen, BLACK, [250, 400], 5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (sound.play()): # Press any button to stop the alarm sound. Otherwise, it willnot stop until reach the end of the song
                    if event.button == 1: 
                        if (100 < mouseX < 150) and (50 < mouseY < 100):
                            totalSeconds += 60
                            print("press '+' minutes")
                        if (100 < mouseX < 150) and (200 < mouseY < 250):
                            totalSeconds -= 60
                            print("press '-' minutes")
                        if (200 < mouseX < 250) and (50 < mouseY < 100):
                            totalSeconds += 1
                            print("press '+' second")
                        if (200 < mouseX < 250) and (200 < mouseY < 250):
                            totalSeconds -= 1
                            print("press '-' second")

                    if event.button == 1:
                        if (300 < mouseX < 450) and (30 < mouseY < 80):
                            start = True
                            total = totalSeconds
                            if (total != 0):
                                pygame.draw.rect(screen, RED, (60, 530, int(380 * (totalSeconds / total)), 30))
                            print("press Start")
                        if (300 < mouseX < 400) and (130 < mouseY < 180):
                            print("press Stop")
                            start = False
                        if (300 < mouseX < 400) and (230 < mouseY < 280):
                            totalSeconds = 0
                            print("press Reset")
                            print("Total seconds: " + str(totalSeconds))
                sound.stop()

        if start:
            totalSeconds -= 1
            if (totalSeconds == 0):
                start = False
                sound.play()
            time.sleep(1)

        if (totalSeconds < 0):
            totalSeconds = 0

        mins = int(totalSeconds / 60)
        secs = totalSeconds - mins * 60

        timeNow = str(mins) + " : " + str(secs)

        textTime = font.render(timeNow, True, BLACK)
        screen.blit(textTime, (120, 120))

        xSec = 250 + 90 * math.sin(6 * secs * (math.pi / 180))
        ySec = 400 - 90 * math.cos(6 * secs * (math.pi / 180))
        pygame.draw.line(screen, BLACK, (250, 400), (int(xSec), int(ySec)))

        xMin = 250 + 40 * math.sin(6 * mins * (math.pi / 180))
        yMin = 400 - 40 * math.cos(6 * mins * (math.pi / 180))
        pygame.draw.line(screen, RED, (250, 400), (int(xMin), int(yMin)))

        if (total != 0):
            pygame.draw.rect(screen, RED, (60, 530, int(380 * (totalSeconds / total)), 30))

        pygame.display.flip() 

    pygame.quit()

except Exception as bug:
    print(bug)

input()
