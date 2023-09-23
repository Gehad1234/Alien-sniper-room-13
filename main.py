import pygame
from pygame import mixer
import random
import math
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
#Background 
background = pygame.image.load ('Gerry.jpg')
#background sound 
mixer.music.load('background.wav')
mixer.music.play(-1)
#Title and icon
pygame.display.set_caption("alien أوضة 13")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player

player = pygame.image.load('astronomy.png')
playerX = 370
playerY = 480
playerX_change = 0


#enemy 

enemy_img = []
enemyX = [] 
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 10

for i in range (num_of_enemies):
    enemy_img.append( pygame.image.load('alien.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.4)
    enemyY_change.append(3)


#Bullet

bullet_img = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"





def Player(X,Y):
    screen.blit(player, (X,Y) )

def enemy(X,Y,i):
    screen.blit(enemy_img[i], (X,Y) )  

def buulet_fire(x,y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bullet_img, (x+16,y+10))
def iscollision (enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance <27 :
        return True
    else:
        return False
#score 
score_val = 0
font = pygame.font.Font('freesansbold.ttf',37)
textX = 10
textY = 10
def show_score(x,y):
    score = font.render("score : " + str(score_val),True,(225,225,225))
    screen.blit(score,(x,y))
#Game loop
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change = -0.4
            if event.key ==pygame.K_RIGHT:
                playerX_change = 0.4
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX= playerX
                    buulet_fire(bulletX,bulletY)
        if event.type== pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.type==pygame.K_RIGHT:
                playerX_change=0

    playerX += playerX_change
    if playerX<0:
        playerX=0
    elif playerX>736:
        playerX=736
#enemy movement
    for i in range(num_of_enemies):
        enemyX[i] +=enemyX_change[i]
        if enemyX[i]<0:
            enemyX_change[i]= 0.3
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>736:
            enemyX_change[i] = -0.3
            enemyY[i]+=enemyY_change[i]
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            enemy_sound = mixer.Sound('explosion.wav')
            enemy_sound.play()            
            bulletY= 480 
            bullet_state= "ready"
            score_val+=1
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i], enemyY[i],i)  
#bullet movement
    if bulletY < 0:
        bulletY = 480 
        bullet_state="ready"
    if bullet_state == "Fire":
        buulet_fire(bulletX,bulletY)
        bulletY-=bulletY_change
 
    Player(playerX, playerY)   
    show_score(textX,textY)
    pygame.display.update()