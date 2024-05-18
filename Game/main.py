import GM
import pygame
import random
import math
import sys
from sys import exit
from enum import Enum

print(pygame.version.ver)

framerate = 500
width = 1000
height = 860

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Who is the killer?")

#region image loading
def GiveFile(input):
    return input

image1 = pygame.image.load(GiveFile('image1.jpg'))
image1.get_rect().center = (width / 2, height / 2)

image2 = pygame.image.load(GiveFile('image2.jpg'))
image2.get_rect().center = (width / 2, height / 2)

image3 = pygame.image.load(GiveFile('image3.jpg'))
image3.get_rect().center = (width / 2, height / 2)

map = pygame.image.load(GiveFile('map.png'))
map.get_rect().center = (width / 2, height / 2)

talk = pygame.image.load(GiveFile('E.png'))
talk.get_rect().center = (width / 2, height / 2)

guy1 = pygame.image.load(GiveFile('Character\\Guy1.png'))
if random.random() < .5:
    guy1 = pygame.image.load(GiveFile('Character\\Guy1.01.png'))
guy1_rect = guy1.get_rect()
guy1_rect.center = (0, -0)

guy2 = pygame.image.load(GiveFile('Character\\Guy2.png'))
if random.random() < .5:
    guy2 = pygame.image.load(GiveFile('Character\\Guy2.01.png'))
guy2_rect = guy2.get_rect()
guy2_rect.center = (0, -0)

woman = pygame.image.load(GiveFile('Character\\Woman.png'))
woman_rect = woman.get_rect()
woman_rect.center = (0, -0)

cop = [
    pygame.image.load(GiveFile('Character\\Anim\\Character1.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character2.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character3.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character4.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character5.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character6.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character7.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character8.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character9.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character10.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character11.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character12.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character13.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character14.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character15.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character16.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character17.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character18.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character19.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character20.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character21.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character22.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character23.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Character24.png'))
]
suit = [
    pygame.image.load(GiveFile('Character\\Anim\\Suit1.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit2.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit3.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit4.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit5.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit6.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit7.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit8.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit9.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit10.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit11.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit12.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit13.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit14.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit15.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit16.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit17.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit18.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit19.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit20.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit21.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit22.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit23.png')),
    pygame.image.load(GiveFile('Character\\Anim\\Suit24.png'))
]

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
#endregion
#region functions
def degree_to_position(degree):
    """ Convert degree to radian """
    radian = degree * math.pi / 180
    # Calculate x and y coordinates
    x = math.cos (radian)
    y = math.sin (radian)
    # Return coordinates as a tuple
    return (x, y)
def Similarity(n1, n2):
    """ Calculates a similarity score between 2 numbers """
    if n1 + n2 == 0:
        return 1
    else:
        return 1 - abs(n1 - n2) / (n1 + n2)
def draw_text(surface, text, size, color, x, y, relative):
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    text_surf = font.render(str(text), True, color)
    text_rect = text_surf.get_rect()

    if(relative == 'center'):
        text_rect.center = (x, y)
    
    surface.blit(text_surf, text_rect)
def disBetweenPoints(P1, P2):
    dis = (P1[1] - P2[1])**2 + (P1[0] - P2[0])**2
    return dis
def addInRange(val, add, minval, maxval):
    newval = val + add
    
    #(new value, was in bounds)
    if newval < minval: return (minval, False)
    if newval > maxval: return (maxval, False)
    return (newval, True)
def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)
def box_text(surface, font, x_start, x_end, y_start, text, colour):
    x = x_start
    y = y_start
    words = text.split(' ')

    for word in words:
        word_t = font.render(word, True, colour)
        if word_t.get_width() + x <= x_end:
            surface.blit(word_t, (x, y))
            x += word_t.get_width() * 1.1
        else:
            y += word_t.get_height() * 1.1
            x = x_start
            surface.blit(word_t, (x, y))
            x += word_t.get_width() * 1.1
    return y
#endregion
#region classes
class NPCType(Enum):
    guy1 = 1
    woman = 2
    guy2 = 3
class Vector2:
    x = 0
    y = 0
class Facing(Enum):
    DOWN = 1
    RIGHT = 2
    UP = 3
    LEFT = 4
class Character:
    def __init__(self, startPosX, startPosY, color):
        self.defaultPos = Vector2()
        self.defaultPos.x = startPosX
        self.defaultPos.y = startPosY

        self.pos = Vector2()
        self.pos.x = startPosX
        self.pos.y = startPosY
        
        self.vel = Vector2()
        self.maxVal = 100
        self.acc = 125
        self.size = 25
        self.color = color

        self.Facing = Facing.DOWN
        self.Moving = False
        self.Frame = 0
        self.stopwatch = 0
        self.cooldown = 0.04

    def VelocityUpdate(self, isX: bool, Direction):
        velocity = 0
        if isX: velocity = self.vel.x
        else: velocity = self.vel.y
        
        if(Direction != 0):
            velocity += self.acc * dt * Direction
            if(velocity > self.maxVal):
                velocity = self.maxVal
            if(velocity < -self.maxVal):
                velocity = -self.maxVal
        else:
            if velocity > 0:
                velocity -= self.acc * dt
                if(velocity < 0): velocity = 0
            elif velocity < 0:
                velocity += self.acc * dt
                if(velocity > 0): velocity = 0
        
        if isX: self.vel.x = velocity
        else: self.vel.y = velocity

    def Update(self, dt, up: bool, left: bool, down: bool, right: bool):
        
        horizontal = right - left
        #because up is negative in this engine but I don't like that
        vertical = -1 * (up - down)

        tempMoving = self.Moving

        self.Moving = True
        if(self.vel.y > 0):
            self.Facing = Facing.DOWN
        elif(self.vel.y < 0):
            self.Facing = Facing.UP
        elif(self.vel.x > 0):
            self.Facing = Facing.RIGHT
        elif(self.vel.x < 0):
            self.Facing = Facing.LEFT
        else:
            self.Moving = False

        self.JustStoppedMoving = False
        if(tempMoving != self.Moving):
            if(self.Moving == False):
                self.JustStoppedMoving = True

        self.VelocityUpdate(True, horizontal)
        self.VelocityUpdate(False, vertical)

        _X = addInRange(self.pos.x, self.vel.x * dt, 50, width - 50)
        if(_X[1] == False): self.vel.x = 0
        self.pos.x = _X[0]
        _Y = addInRange(self.pos.y, self.vel.y * dt, 50, height - 50)
        if(_Y[1] == False): self.vel.y = 0
        self.pos.y = _Y[0]
        self.DrawChar(dt)

    def DrawChar(self, dt):
        if(not self.Moving or not (self.Frame >= (self.Facing.value * 6 - 6) and self.Frame <= (self.Facing.value * 6 - 1))):
            if(self.Facing == Facing.DOWN):
                self.Frame = 0
            elif(self.Facing == Facing.RIGHT):
                self.Frame = 6
            elif(self.Facing == Facing.UP):
                self.Frame = 12
            elif(self.Facing == Facing.LEFT):
                self.Frame = 18
        else:
            self.stopwatch = self.stopwatch + dt * (abs(self.vel.x + self.vel.y) / (self.maxVal * 2))
            if(self.stopwatch > self.cooldown):
                self.stopwatch = self.stopwatch - self.cooldown
                self.Frame += 1
                if(self.Frame > self.Facing.value * 6 - 1):
                    self.Frame = (self.Facing.value * 6) - 6
        
        screen.blit(cop[self.Frame], (self.pos.x, self.pos.y))
        screen.blit(suit[self.Frame], (self.pos.x, self.pos.y))

    def Reset(self):
        self.pos.x = self.defaultPos.x
        self.pos.y = self.defaultPos.y
        self.vel.x = 0
        self.vel.y = 0
#endregion
#region Snowflake class
slowestSnowflake = 50
SnowFlakeVertical = 250
class Snowflake:

    def __init__(self):
        # Initialize the attributes of the snowflake
        self.x = 0 # The x coordinate
        self.y = 0 # The y coordinate
        self.speedY = 0 # The falling speed
        self.radius = 0 # The radius of the circle
        Snowflake.randomizeSnowflake(self)

    def update(self, dt):
        # Update the position of the snowflake
        self.y += self.speedY * dt # Move down by the speed
        self.x += SnowFlakeVertical * dt # Move down by the speed
        # If the snowflake reaches the bottom of the screen, reset its position
        if self.y > height or self.x > width:
            Snowflake.randomizeSnowflake(self)
        # Draw self
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.radius)
        
    def randomizeSnowflake(obj):
        obj.x = random.randint(int(-(height / slowestSnowflake) * SnowFlakeVertical)
                               - width, width) # Random x coordinate
        obj.y = random.randint(-height, 0) # Random y coordinate
        obj.speedY = random.randint(slowestSnowflake, 250) # Random speed
        obj.radius = random.randint(1, 2) # Random radius

#Create an empty list to store the snowflakes
snowflakes = []
#Fill snowflakes
def CreateSnow():
    for i in range(350):
        temp = Snowflake()
        snowflakes.append(temp)
CreateSnow()
#endregion

MouseHeldDown = False

EHeldDown = False
EnterHeldDown = False
EscapeHeldDown = False

WHeldDown = False
AHeldDown = False
SHeldDown = False
DHeldDown = False

UpHeldDown = False
LeftHeldDown = False
DownHeldDown = False
RightHeldDown = False

player1 = Character(width / 2, height / 2, (255, 0, 0))

StoryGoingDark = True
StoryCooldown = 0.00006
CurrentStoryState = 0
StoryStopwatch = 0

alpha = 1
GameState = 0

NPCPositions = [(630, 470), (670, 470), (710, 470)]

isTalking = False

closeNPC = NPCType.guy1

base_font = pygame.font.Font(None, 32) 
user_text = '' 
output = ""

output_text_y_end = 0

wonTheGame = False

#Update()
while 1:

    #count the time frame took and assign it to dt
    _dt = clock.tick(framerate)
    dt = _dt / 1000

    #resets screen
    screen.fill((255, 0, 0))

    #region detect events including inputs
    MousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            MouseHeldDown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            MouseHeldDown = False
        else: #this is awful fix that
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    EscapeHeldDown = True
                if event.key == pygame.K_RETURN:
                    EnterHeldDown = True
                if event.key == pygame.K_e:
                    EHeldDown = True
                if event.key == pygame.K_w:
                    WHeldDown = True
                if event.key == pygame.K_a:
                    AHeldDown = True
                if event.key == pygame.K_s:
                    SHeldDown = True
                if event.key == pygame.K_d:
                    DHeldDown = True
                if event.key == pygame.K_UP:
                    UpHeldDown = True
                if event.key == pygame.K_LEFT:
                    LeftHeldDown = True
                if event.key == pygame.K_DOWN:
                    DownHeldDown = True
                if event.key == pygame.K_RIGHT:
                    RightHeldDown = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    EscapeHeldDown = False
                if event.key == pygame.K_RETURN:
                    EnterHeldDown = False
                if event.key == pygame.K_e:
                    EHeldDown = False
                if event.key == pygame.K_w:
                    WHeldDown = False
                if event.key == pygame.K_a:
                    AHeldDown = False
                if event.key == pygame.K_s:
                    SHeldDown = False
                if event.key == pygame.K_d:
                    DHeldDown = False
                if event.key == pygame.K_UP:
                    UpHeldDown = False
                if event.key == pygame.K_LEFT:
                    LeftHeldDown = False
                if event.key == pygame.K_DOWN:
                    DownHeldDown = False
                if event.key == pygame.K_RIGHT:
                    RightHeldDown = False
        if(isTalking):
            EHeldDown = False
            WHeldDown = False
            AHeldDown = False
            SHeldDown = False
            DHeldDown = False
            UpHeldDown = False
            LeftHeldDown = False
            DownHeldDown = False
            RightHeldDown = False

                
    #endregion
    #region game states
    if GameState == 0:
        screen.fill((0, 0, 0))

        draw_text(screen, "Press enter key to start",
                  40, (255, 255, 255), width / 2, height / 2, "center")
        
        if EnterHeldDown:
            GameState = 1
    elif GameState == 1:
        screen.fill((0, 0, 0))

        if not StoryGoingDark:
            StoryStopwatch += dt
            if StoryStopwatch > StoryCooldown:
                StoryStopwatch = StoryCooldown
                StoryGoingDark = True
        else:
            StoryStopwatch -= dt
            if StoryStopwatch < 0:
                StoryStopwatch = 0
                CurrentStoryState += 1
                StoryGoingDark = False
            
        alpha = (StoryStopwatch / StoryCooldown) * 255

        if CurrentStoryState == 1:
            CurrentImg = image1
        elif CurrentStoryState == 2:
            CurrentImg = image2
        elif CurrentStoryState == 3:
            CurrentImg = image3
        elif CurrentStoryState == 4:
            GameState = 2

        CurrentImg.set_alpha(alpha)
        screen.blit(CurrentImg, CurrentImg.get_rect())
    elif GameState == 2:
        screen.blit(map, map.get_rect())

        screen.blit(guy1, NPCPositions[0])
        screen.blit(woman, NPCPositions[1])
        screen.blit(guy2, NPCPositions[2])

        cantalk = False
        guy1dis = disBetweenPoints([player1.pos.x, player1.pos.y], list(NPCPositions[0]))
        womandis = disBetweenPoints([player1.pos.x, player1.pos.y], list(NPCPositions[1]))
        guy2dis = disBetweenPoints([player1.pos.x, player1.pos.y], list(NPCPositions[2]))
        
        if(guy1dis < 500 or womandis < 500 or guy2dis < 500):
            cantalk = True
            if(guy1dis < guy2dis):
                if(guy1dis < womandis):#guy1
                    closeNPC = NPCType.guy1
                    screen.blit(talk, [(NPCPositions[0])[0], (NPCPositions[0])[1] - 50])
                else:#woman
                    closeNPC = NPCType.woman
                    screen.blit(talk, [(NPCPositions[1])[0], (NPCPositions[1])[1] - 50])
            else:
                if(guy2dis < womandis):#guy2
                    closeNPC = NPCType.guy2
                    screen.blit(talk, [(NPCPositions[2])[0], (NPCPositions[2])[1] - 50])
                else:#woman
                    closeNPC = NPCType.woman
                    screen.blit(talk, [(NPCPositions[1])[0], (NPCPositions[1])[1] - 50])

        player1.Update(dt,
            WHeldDown + UpHeldDown, AHeldDown + LeftHeldDown,
            SHeldDown + DownHeldDown, DHeldDown + RightHeldDown)
        
        for snowflake in snowflakes:
            snowflake.update(dt)

        #region talking stuff
        if cantalk:
            if EHeldDown:
                EHeldDown = False
                isTalking = True
        if isTalking:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    sys.exit()
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_BACKSPACE: 
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        EnterHeldDown = True
                    elif event.key == pygame.K_ESCAPE:
                        EscapeHeldDown = True
                    else: 
                        user_text += event.unicode

            draw_rect_alpha(screen, (0, 0, 0, 135), (0, height - 125, width, 125))
            box_text(screen, base_font, 0, width, height - 120, user_text, (255, 255, 255))

            if EnterHeldDown:
                if user_text == "":
                    if(closeNPC == NPCType.guy1):
                        wonTheGame = True
                    else:
                        wonTheGame = False
                    user_text = ""
                    isTalking = False
                    GameState = 3
                else:
                    if(closeNPC == NPCType.guy1):
                        print("SYSTEM MESSAGE: Message \"" + "User asks to Jeff: " + user_text + "\" is sent")
                        output = GM.ask("User asks to Jeff: \"" + user_text + "\"")
                        #output = Killer.ask(user_text)
                    elif(closeNPC == NPCType.woman):
                        print("SYSTEM MESSAGE: Message \"" + "User asks to Annie: \"" + user_text + "\" is sent")
                        output = GM.ask("User asks to Annie: \"" + user_text + "\"")
                        #output = innocentCS.ask(user_text)
                    elif(closeNPC == NPCType.guy2):
                        print("SYSTEM MESSAGE: Message \"" + "User asks to Abed: " + user_text + "\" is sent")
                        output = GM.ask("User asks to Abed: \"" + user_text + "\"")
                        #output = innocentHomeless.ask(user_text)
                    print(closeNPC.name + ": " + output)
                    print("SYSTEM MESSAGE: quiting talking mode")
                    user_text = ""
                    isTalking = False
            if EscapeHeldDown:
                print("SYSTEM MESSAGE: quiting talking mode")
                user_text = ""
                isTalking = False

        if(output != ""):
            draw_rect_alpha(screen, (0, 0, 0, 135), (0, 0, width, output_text_y_end + 25))
            output_text_y_end = box_text(
                screen, base_font, 0, width, 5, output, (255, 255, 255)) 
        #endregion

    elif GameState == 3:
        screen.fill((0, 0, 0))

        youWonText = ""
        if(wonTheGame):
            youWonText = "You won! Jeff was the killer!"
        else:
            youWonText = "You lost. Jeff was the killer."

        draw_text(screen, youWonText,
                  40, (255, 255, 255), width / 2, height / 2, "center")
    
    pygame.display.flip()