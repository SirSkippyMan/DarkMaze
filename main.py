#-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
# 
# Welcome to the dark maze! To complete all levels, use the
# WASD keys to move the character through each level. Your
# goal is to make it to the end of each level as quickly and
# carefully as possible. If your character touches a wall,
# you will have to start the level over. There are 7 levels.
# Good luck!
#
# ~Credits~
# All code and art written by Josh Nygaard; music and sounds
# created by Josh Nygaard, created using Audiotool
#
# Version 1.0
#-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-

#-----IMPORTS AND INITIALIZATION-----
import pygame
import threading
import math
pygame.init()
pygame.font.init()

win = pygame.display.set_mode((500, 500), pygame.DOUBLEBUF)
pygame.display.set_caption("Dark Maze")

#-----SOUNDS-----
introSound = pygame.mixer.Sound("introSound.mp3")
clickSound = pygame.mixer.Sound("click.mp3")
deathSound = pygame.mixer.Sound("death.mp3")
goalSound = pygame.mixer.Sound("goalSound.mp3")
backgroundMusic = pygame.mixer.Sound("backgroundMusic.mp3")
pygame.mixer.music.load("backgroundMusic.mp3")

#-----CHARACTER IMAGES-----
charLeft = pygame.transform.scale(pygame.image.load('characterLeft.png'), (50, 50))
charRight = pygame.transform.scale(pygame.image.load('characterRight.png'), (50, 50))
charUp = pygame.transform.scale(pygame.image.load('characterUp.png'), (50, 50))
charDown = pygame.transform.scale(pygame.image.load('characterDown.png'), (50, 50))
charIdle = pygame.transform.scale(pygame.image.load('characterIdle.png'), (50, 50))

global cooldown
cooldown = 1

#-----INTRO INFO-----
introducing = 0
intro = pygame.image.load('intro.png')

#-----TITLE INFO-----
showTitle = 0
dmTitle = pygame.image.load('darkmazetitle.png')

#-----PLAY BUTTON INFO-----
plaBttn = pygame.image.load('playbutton.png')

#-----GAME OVER-----
gameOver = 0
missionAcc = pygame.image.load('gameOverText.png')

#-----INSTRUCTIONS-----
gameInstructions = pygame.image.load('gameInstructions.png')

#-----GOAL INFO-----
flag = pygame.transform.scale(pygame.image.load('goal.png'), (35, 35))
class endOfLevel(object):
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h

  def draw(self, win):
    win.blit(flag, (self.x, self.y))

#-----CHARACTER INFO-----
startGame = 0
class character(object):
  def __init__(self, x, y, w, h, v):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.v = v

  def draw(self, win):
    if keys[pygame.K_w]:
      win.blit(charUp, (self.x, self.y))
    elif keys[pygame.K_a]:
      win.blit(charLeft, (self.x, self.y))
    elif keys[pygame.K_s]:
      win.blit(charDown, (self.x, self.y))
    elif keys[pygame.K_d]:
      win.blit(charRight, (self.x, self.y))
    else:
      win.blit(charIdle, (self.x, self.y))

#-----INTRO CLASS-----
class introduction(object):
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h

  def draw(self, win):
    win.blit(intro, (self.x, self.y))

#-----TITLE CLASS-----
class darkMazeTitle(object):
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h

  def draw(self, win):
    win.blit(dmTitle, (self.x, self.y))

#-----PLAY BUTTON CLASS-----
class pb(object):
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h

  def draw(self, win):
    win.blit(plaBttn, (self.x, self.y))

#-----CHECK IF QUIT-----
def checkQuit():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False;

#-----CHECKS IF QUIT AND REDRAW WINDOW-----
def tick():
  redrawWin()
  checkQuit()

#-----CHECK IF MOUSE IS DOWN-----
def mouseDown():
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      return True
    elif event.type == pygame.MOUSEBUTTONUP:
      return False

#-----CHECK IF THE CHARACTER IS COLLIDING INTO A WALL-----
def colliding():
  if playerHB.colliderect(wall1) or playerHB.colliderect(wall2) or playerHB.colliderect(wall3) or playerHB.colliderect(wall4) or playerHB.colliderect(wall5) or playerHB.colliderect(wall6) or playerHB.colliderect(wall7) or playerHB.colliderect(wall8) or playerHB.colliderect(wall9) or playerHB.colliderect(wall10) or playerHB.colliderect(wall11) or playerHB.colliderect(wall12) or playerHB.colliderect(wall13) or playerHB.colliderect(wall14) or playerHB.colliderect(wall15) or playerHB.colliderect(wall16) or playerHB.colliderect(wall17) or playerHB.colliderect(wall18) or playerHB.colliderect(wall19) or playerHB.colliderect(wall20): 
    return True
  else:
    return False

#-----DRAW WALLS-----
def drawWall(wallX, wallY, wallW, wallH):
  return pygame.draw.rect(win, (0, 255, 255), (wallX, wallY, wallW, wallH))

#-----OBJECTS-----
introductionLogo = introduction(72, 144, 356, 211)
title = darkMazeTitle(168, 25, 165, 53)
playButton = pb(172, 350, 156, 46)
player = character(10, 45, 50, 50, 5)
goal = endOfLevel(450, 450, 50, 50)

#-----RUN THE GAME TIMER-----
def timerLoop():
  global gameTime
  gameTime = 0
  while startGame == 1:
    pygame.time.delay(1000)
    gameTime += 1

#----LEVEL 7 MOVING WALLS-----
def lvl7mov():
  global mov1
  mov1 = 15
  while startGame == 1:
    for i in range(67):
      pygame.time.delay(50)
      mov1 += 7 
    for i in range(67):
      pygame.time.delay(50)
      mov1 -= 7

#-----LEVEL 4 MOVING WALLS-----
def lvl4mov():
  global mov3
  mov3 = 100
  while startGame == 1:
    for i in range(33):
      pygame.time.delay(50)
      mov3 += 3
    for i in range(33):
      pygame.time.delay(50)
      mov3 -= 3

#-----LEVEL 6 MOVING WALLS-----
def lvl6mov1():
  global mov2
  mov2 = 0
  while startGame == 1:
    for i in range(50):
      pygame.time.delay(50)
      mov2 += 2
    for i in range(50):
      pygame.time.delay(50)
      mov2 -= 2

def lvl6mov2():
  global mov4
  mov4 = 100
  while startGame == 1:
    for i in range(100):
      pygame.time.delay(50)
      mov4 += 2
    for i in range(100):
      pygame.time.delay(50)
      mov4 -= 2

#-----REDRAW WINDOW-----
def redrawWin():
  win.fill((0, 0, 75))

  # intro
  if introducing == 1:
    introductionLogo.draw(win)

  # game menu
  if showTitle == 1:
    title.draw(win)
    playButton.draw(win)
    win.blit(gameInstructions, (88, 110))

  # gameplay
  if startGame == 1:
    # player and goal
    player.draw(win)
    goal.draw(win)

    # stats
    global myFont
    myFont = pygame.font.SysFont('Arial', 30)
    text = myFont.render("Time: " + str(math.floor(gameTime / 60)) + ":" + str(math.floor((gameTime % 60) / 10)) + str(gameTime % 10) + "     Deaths: " + str(deaths), False, (0, 255, 255))
    win.blit(text, (10,0))

    # walls
    global wall1
    global wall2
    global wall3
    global wall4
    global wall5
    global wall6
    global wall7
    global wall8
    global wall9
    global wall10
    global wall11
    global wall12
    global wall13
    global wall14
    global wall15
    global wall16
    global wall17
    global wall18
    global wall19
    global wall20
    wall1 = drawWall(0, 40, 500, 15)
    wall2 = drawWall(0, 40, 15, 500)
    wall3 = drawWall(485, 40, 15, 500)
    wall4 = drawWall(0, 485, 500, 15)

    if level == 1:
      wall5 = drawWall(0, 120, 400, 15)
      wall6 = drawWall(100, 200, 400, 15)
      wall7 = drawWall(0, 290, 400, 15)
      wall8 = drawWall(100, 380, 400, 15)
      wall9 = drawWall(0, 0, 0, 0)
      wall10 = drawWall(0, 0, 0, 0)
      wall11 = drawWall(0, 0, 0, 0)
      wall12 = drawWall(0, 0, 0, 0)
      wall13 = drawWall(0, 0, 0, 0)
      wall14 = drawWall(0, 0, 0, 0)
      wall15 = drawWall(0, 0, 0, 0)
      wall16 = drawWall(0, 0, 0, 0)
      wall17 = drawWall(0, 0, 0, 0)
      wall18 = drawWall(0, 0, 0, 0)
      wall19 = drawWall(0, 0, 0, 0)
      wall20 = drawWall(0, 0, 0, 0)
    elif level == 2:
      wall5 = drawWall(0, 120, 200, 15)
      wall6 = drawWall(300, 120, 200, 15)
      wall7 = drawWall(0, 200, 300, 15)
      wall8 = drawWall(400, 200, 100, 15)
      wall9 = drawWall(0, 290, 100, 15)
      wall10 = drawWall(200, 290, 300, 15)
      wall11 = drawWall(100, 290, 15, 130)
      wall12 = drawWall(185, 290, 15, 130)
      wall13 = drawWall(400, 400, 15, 150)
      wall14 = drawWall(250, 400, 15, 150)
      wall15 = drawWall(325, 290, 15, 150)
      wall16 = drawWall(0, 0, 0, 0)
      wall17 = drawWall(0, 0, 0, 0)
      wall18 = drawWall(0, 0, 0, 0)
      wall19 = drawWall(0, 0, 0, 0)
      wall20 = drawWall(0, 0, 0, 0)
    elif level == 3:
      wall5 = drawWall(60, 50, 15, 350)
      wall6 = drawWall(60, 390, 280, 15)
      wall7 = drawWall(420, 100, 15, 400)
      wall8 = drawWall(130, 100, 290, 15)
      wall9 = drawWall(325, 160, 15, 230)
      wall10 = drawWall(130, 100, 15, 240)
      wall11 = drawWall(260, 115, 15, 225)
      wall12 = drawWall(195, 160, 15, 230)
      wall13 = drawWall(130, 460, 15, 40)
      wall14 = drawWall(195, 400, 15, 40)
      wall15 = drawWall(260, 460, 15, 40)
      wall16 = drawWall(325, 400, 15, 40)
      wall17 = drawWall(60, 400, 15, 40)
      wall18 = drawWall(0, 0, 0, 0)
      wall19 = drawWall(0, 0, 0, 0)
      wall20 = drawWall(0, 0, 0, 0)
    elif level == 4:
      wall5 = drawWall(0, 100, 100, 15)
      wall6 = drawWall(200, 100, 100, 15)
      wall7 = drawWall(400, 100, 100, 15)
      wall8 = drawWall(0, 200, 100, 15)
      wall9 = drawWall(200, 200, 100, 15)
      wall10 = drawWall(400, 200, 100, 15)
      wall11 = drawWall(0, 300, 100, 15)
      wall12 = drawWall(200, 300, 100, 15)
      wall13 = drawWall(400, 300, 100, 15)
      wall14 = drawWall(0, 400, 100, 15)
      wall15 = drawWall(200, 400, 100, 15)
      wall16 = drawWall(400, 400, 100, 15)
      wall17 = drawWall(mov3, 100, 200, 15)
      wall18 = drawWall(299 - mov3, 200, 200, 15)
      wall19 = drawWall(mov3, 300, 200, 15)
      wall20 = drawWall(299 - mov3, 400, 200, 15)
    elif level == 5:
      wall5 = drawWall(75, 55, 15, 275)
      wall6 = drawWall(0, 375, 200, 15)
      wall7 = drawWall(300, 375, 200, 15)
      wall8 = drawWall(150, 315, 270, 15)
      wall9 = drawWall(150, 110, 15, 220)
      wall10 = drawWall(150, 110, 270, 15)
      wall11 = drawWall(405, 110, 15, 220)
      wall12 = drawWall(75, 430, 425, 15)
      wall13 = drawWall(185, 330, 15, 45)
      wall14 = drawWall(0, 0, 0, 0)
      wall15 = drawWall(0, 0, 0, 0)
      wall16 = drawWall(0, 0, 0, 0)
      wall17 = drawWall(0, 0, 0, 0)
      wall18 = drawWall(0, 0, 0, 0)
      wall19 = drawWall(0, 0, 0, 0)
      wall20 = drawWall(0, 0, 0, 0)
    elif level == 6:
      wall5 = drawWall(100, 50, 15, 350)
      wall6 = drawWall(200, 150, 15, 350)
      wall7 = drawWall(300, 50, 15, 350)
      wall8 = drawWall(400, 150, 15, 350)
      wall9 = drawWall(mov2, 250, 100, 15)
      wall10 = drawWall(400 - mov2, 250, 100, 15)
      wall11 = drawWall(mov4, 350, 100, 15)
      wall12 = drawWall(400 - mov4, 150, 100, 15)
      wall13 = drawWall(0, 0, 0, 0)
      wall14 = drawWall(0, 0, 0, 0)
      wall15 = drawWall(0, 0, 0, 0)
      wall16 = drawWall(0, 0, 0, 0)
      wall17 = drawWall(0, 0, 0, 0)
      wall18 = drawWall(0, 0, 0, 0)
      wall19 = drawWall(0, 0, 0, 0)
      wall20 = drawWall(0, 0, 0, 0)
    elif level == 7:
      wall5 = drawWall(0, 156, 425, 15)
      wall6 = drawWall(75, 312, 425, 15)
      wall7 = drawWall(mov1, 171, 15, 75)
      wall8 = drawWall(469 - mov1, 237, 15, 75)
      wall9 = drawWall(75, 55, 15, 55)
      wall10 = drawWall(150, 101, 15, 55)
      wall11 = drawWall(225, 55, 15, 55)
      wall12 = drawWall(300, 101, 15, 55)
      wall13 = drawWall(375, 55, 15, 55)
      wall14 = drawWall(0, 370, 450, 15)
      wall15 = drawWall(50, 430, 450, 15)
      wall16 = drawWall(0, 0, 0, 0)
      wall17 = drawWall(0, 0, 0, 0)
      wall18 = drawWall(0, 0, 0, 0)
      wall19 = drawWall(0, 0, 0, 0)
      wall20 = drawWall(0, 0, 0, 0)

  # end of game  
  if gameOver == 1:
    gameOverText = myFont.render("Time: " + str(math.floor(gameTime / 60)) + ":" + str(math.floor((gameTime % 60) / 10)) + str(gameTime % 10), False, (0, 255, 255))
    gameOverText2 = myFont.render("Deaths: " + str(deaths), False, (0, 255, 255))
    gotRect = gameOverText.get_rect(center = (250, 250))
    got2Rect = gameOverText.get_rect(center = (250, 300))
    win.blit(missionAcc, (88, 100))
    win.blit(gameOverText, gotRect)
    win.blit(gameOverText2, got2Rect)

  pygame.display.update()

#-----MAIN LOOP-----
run = True
level = 0
while run:
  # initial variables
  keys = pygame.key.get_pressed()
  playNotClicked = True
  
  # intro
  tick()
  print("Credits: all art and code written by Josh Nygaard. Music and sounds created by Josh Nygaard using Audiotool. Version: 1.0")
  pygame.time.delay(1000)
  introducing = 1
  pygame.mixer.Sound.play(introSound)
  tick()
  pygame.time.delay(3000)
  introducing = 0
  tick()
  pygame.time.delay(500)
  
  # title screen
  showTitle = 1
  pygame.mixer.music.play(-1)
  print("Welcome to the dark maze! To complete all levels, use the WASD keys to move the character through each level. Your goal is to make it to the end of each level as quickly and carefully as possible. If your character touches a wall, you will have to start the level over. There are 7 levels. Good luck!")
  while not plaBttn.get_rect(topleft = (172, 350)).collidepoint(pygame.mouse.get_pos()) and mouseDown() == False or mouseDown() == None:
    tick()
    pygame.time.delay(50)
  showTitle = 0
  pygame.mixer.Sound.play(clickSound)

  # gameplay
  tick()
  startGame = 1
  thread1 = threading.Thread(target = timerLoop)
  thread2 = threading.Thread(target = lvl4mov)
  thread3 = threading.Thread(target = lvl7mov)
  thread4 = threading.Thread(target = lvl6mov1)
  thread5 = threading.Thread(target = lvl6mov2)
  thread1.start()
  thread2.start()
  thread3.start()
  thread4.start()
  thread5.start()
  level = 1
  global deaths
  deaths = 0

  # when game starts
  while startGame == 1:
    #definitions
    keys = pygame.key.get_pressed()
    playerHB = pygame.draw.rect(win, (0, 255, 255), (player.x + 10, player.y + 10, player.w - 25, player.h - 25))
    safety = pygame.draw.rect(win, (0, 255, 255), (0, 40, 60, 50))
    goalHB = pygame.draw.rect(win, (0, 0, 0), (goal.x, goal.y, 35, 35))

    # maintenance
    tick()
    pygame.time.delay(50)
    if colliding():
        deathX = player.x
        deathY = player.y
        player.y = 45
        player.x = 10
        if not playerHB.colliderect(safety):
          deaths += 1
          pygame.mixer.Sound.play(deathSound)
        tick()
      
    # check if player reaches goal
    if playerHB.colliderect(goalHB):
      if level == 7:
        startGame = 0
        gameOver = 1
      player.x = 10
      player.y = 45
      level += 1
      pygame.mixer.Sound.play(goalSound)
      pygame.time.delay(250)

    # player movement
    if keys[pygame.K_w]:
      player.y -= player.v * cooldown
      
    if keys[pygame.K_s]:
      player.y += player.v * cooldown
     
    if keys[pygame.K_a]:
      player.x -= player.v * cooldown
     
    if keys[pygame.K_d]:
      player.x += player.v * cooldown

    #print(pygame.mouse.get_pos())
  # end of game
  print("Time: " + str(math.floor(gameTime / 60)) + ":" + str(math.floor((gameTime % 60) / 10)) + str(gameTime % 10))
  print("Deaths: " + str(deaths))
  while gameOver == 1:
    tick()
    pygame.time.delay(50)
    
pygame.quit()  