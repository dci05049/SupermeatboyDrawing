import pygame
import random
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (  85,107,47)
RED      = ( 255,   0,   0)
SKYBLUE  = (135,206,250)
TREEGREEN = (34,139,34	)
MOUNTAINGREY = (105,105,105)
BROWN = (222,184,135)
WATERBLUE = (100,149,237)
SNOWHITE = (255,250,250)
SNOWGROUND = (205,201,201)
SUNYELLOW = (255,255,0)
CLOUDWHITE = (240,255,255)
pygame.init()
PI = 3.141592653

# Set the width and height of the screen [width, height]
size = (700, 500)



# display screen
screen = pygame.display.set_mode(size)



pygame.display.set_caption("My Game")
#create an array
def draw_bush(screen, x, y):
    """ --- Function for a snowman ---
    Define a function that will draw a snowman at a certain location.
    """
    pygame.draw.ellipse(screen, GREEN, [30 + x, 10 + y, 60, 40])
    pygame.draw.ellipse(screen, GREEN, [15 + x, 20 + y, 60, 40])
    pygame.draw.ellipse(screen, GREEN, [30 + x, 20 + y, 60, 40])
snow_list = []
# Loop 50 times and add a snow flake in a random x,y position
for i in range(1000):
    x = random.randrange(0, 700)
    y = random.randrange(0, 700)
    snow_list.append([x, y])

clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# starting position
rect_x = 700
rect_y = 50

# Speed and direction of wind
rect_change_x = -10
rect_change_y = 0

#2 wind
# starting position
rect2_x = 600
rect2_y = 400

# Speed and direction of wind 2
rect2_change_x = -4
rect2_change_y = 0


#3 wind
# starting position
rect3_x = 450
rect3_y = 200

# Speed and direction of wind 3
rect3_change_x = -6
rect3_change_y = 0

#4 wind
# starting position
rect16_x = 650
rect16_y = 350

# Speed and direction of wind 3
rect16_change_x = -6
rect16_change_y = 0

# starting position off screen...................................
rect17_x = 1400
rect17_y = 50
# Speed and direction of wind
rect17_change_x = -10
rect17_change_y = 0

#2 wind
# starting position
rect18_x = 1200
rect18_y = 400

# Speed and direction of wind
rect18_change_x = -4
rect18_change_y = 0


#3 wind
# starting position
rect19_x = 800
rect19_y = 200

# Speed and direction of wind
rect19_change_x = -6
rect19_change_y = 0

#4 wind
# starting position
rect20_x = 1800
rect20_y = 350

# Speed and direction of wind
rect20_change_x = -6
rect20_change_y = 0






                    #positions and direction for birds


# starting position of bird 1
rect4_x = 655
rect4_y = 10
# Speed and direction of bird1
rect4_change_x = -1
rect4_change_y = 0
# starting position of bird1
rect5_x = 650
rect5_y = 11
# Speed and direction of bird1
rect5_change_x = -1
rect5_change_y = 0

# do bird 2
# starting position of bird2
rect6_x = 645
rect6_y = 21
# Speed and direction of bird2
rect6_change_x = -1
rect6_change_y = 0
# starting position of bird2
rect7_x = 640
rect7_y = 20
# Speed and direction of bird2
rect7_change_x = -1
rect7_change_y = 0

# do bird 3
# starting position of bird3
rect8_x = 660
rect8_y = 15
# Speed and direction of bird3
rect8_change_x = -1
rect8_change_y = 0
# starting position of bird3
rect9_x = 665
rect9_y = 16
# Speed and direction of bird3
rect9_change_x = -1
rect9_change_y = 0


# do bird 4
# starting position of bird4
rect10_x = 670
rect10_y = 5
# Speed and direction of bird4
rect10_change_x = -1
rect10_change_y = 0
# starting position of bird4
rect11_x = 675
rect11_y = 6
# Speed and direction of bird4
rect11_change_x = -1
rect11_change_y = 0

# do bird 5
# starting position of bird5
rect12_x = 630
rect12_y = 30
# Speed and direction of bird5
rect12_change_x = -1
rect12_change_y = 0
# starting position of bird5
rect13_x = 635
rect13_y =31
# Speed and direction of bird5
rect13_change_x = -1
rect13_change_y = 0

# do bird 6
# starting position of bird5
rect14_x = 680
rect14_y = 30
# Speed and direction of bird5
rect14_change_x = -1
rect14_change_y = 0
# starting position of bird5
rect15_x = 685
rect15_y =31
# Speed and direction of bird5
rect15_change_x = -1
rect15_change_y = 0


# draw the sun
# starting position
ellipse_x = 10
ellipse_y = 10
# Speed and direction of sun
ellipse_change_x = .2
ellipse_change_y = .0001


# draw the cloud
# starting position
ellipse1_x = 650
ellipse1_y = 20
# Speed and direction of cloud
ellipse1_change_x = -.2
ellipse1_change_y = -.0001

# draw the cloud
# starting position
ellipse2_x = 600
ellipse2_y = 50
# Speed and direction of cloud
ellipse2_change_x = -.2
ellipse2_change_y = -.0001

# draw the cloud
# starting position
ellipse2_x = 350
ellipse2_y = 10
# Speed and direction of cloud
ellipse2_change_x = -.2
ellipse2_change_y = -.0001

# draw the cloud
# starting position
ellipse3_x = 500
ellipse3_y = 10
# Speed and direction of cloud
ellipse3_change_x = -.2
ellipse3_change_y = -.0001

# draw the cloud
# starting position
ellipse4_x = 200
ellipse4_y = 35
# Speed and direction of cloud
ellipse4_change_x = -.2
ellipse4_change_y = -.0001

# draw the cloud
# starting position
ellipse5_x = 100
ellipse5_y = 50
# Speed and direction of cloud
ellipse5_change_x = -.2
ellipse5_change_y = -.0001

# draw the cloud
# starting position
ellipse6_x = 400
ellipse6_y = 80
# Speed and direction of cloud
ellipse6_change_x = -.2
ellipse6_change_y = -.0001

#draw space debris i.e metoer, rocks from space
# starting position
ellipse7_x = 700
ellipse7_y = 50
# Speed and direction of meteor
ellipse7_change_x = -2
ellipse7_change_y = 1

ellipse8_x = -100
ellipse8_y = 0
# Speed and direction of meteor
ellipse8_change_x = 2
ellipse8_change_y = 1

# draw ufo moving.....................................
ellipse9_x = -50
ellipse9_y = 15
# Speed and direction of ufo
ellipse9_change_x = 2
ellipse9_change_y = 0.1

ellipse10_x = -40
ellipse10_y = 10
# Speed and direction of ufo
ellipse10_change_x = 2
ellipse10_change_y = 0.1

#draw rockets...................................

ellipse11_x = -200
ellipse11_y = 20
# Speed and direction of rocket
ellipse11_change_x = 2
ellipse11_change_y = 0


ellipse12_x = -210
ellipse12_y = 20
# Speed and direction of rocket
ellipse12_change_x = 2
ellipse12_change_y = 0


ellipse13_x = -400
ellipse13_y = 10
# Speed and direction of rocket
ellipse13_change_x = 2
ellipse13_change_y = 0

ellipse14_x = -410
ellipse14_y = 10
# Speed and direction of rocket
ellipse14_change_x = 2
ellipse14_change_y = 0


# draw the fish1............................................
# starting position
ellipse15_x = 600
ellipse15_y = 450
# Speed and direction of fish
ellipse15_change_x = .2
ellipse15_change_y = .0001
# starting position
ellipse16_x = 595
ellipse16_y = 448
# Speed and direction of fish
ellipse16_change_x = .2
ellipse16_change_y = .0001

# draw the fish2
# starting position
ellipse17_x = 550
ellipse17_y = 400
# Speed and direction of fish
ellipse17_change_x = .2
ellipse17_change_y = .0001
# starting position
ellipse18_x = 550
ellipse18_y = 398
# Speed and direction of fish
ellipse18_change_x = .2
ellipse18_change_y = .0001

# draw the fish3
# starting position
ellipse19_x = 530
ellipse19_y = 490
# Speed and direction of fish
ellipse19_change_x = .2
ellipse19_change_y = .0001
# starting position
ellipse20_x = 530
ellipse20_y = 488
# Speed and direction of fish
ellipse20_change_x = .2
ellipse20_change_y = .0001







# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
    # set background colour
    screen.fill(SKYBLUE)

    # --- Game logic should go here


    # --- Drawing code should go here

    #make background blue to make sky
    #moving sun

#sun moving
    pygame.draw.ellipse(screen, SUNYELLOW,[ellipse_x, ellipse_y, 50,50])
    # Move the rectangle starting point
    ellipse_x += ellipse_change_x
    ellipse_y += ellipse_change_y

#draw rockets

    pygame.draw.ellipse(screen, MOUNTAINGREY,[ellipse11_x, ellipse11_y, 30,10])
    # Move the rectangle starting point
    ellipse11_x += ellipse11_change_x
    ellipse11_y += ellipse11_change_y
    pygame.draw.ellipse(screen, SUNYELLOW,[ellipse12_x, ellipse12_y, 20,10])
    # Move the rectangle starting point
    ellipse12_x += ellipse12_change_x
    ellipse12_y += ellipse12_change_y


    pygame.draw.ellipse(screen, MOUNTAINGREY,[ellipse13_x, ellipse13_y, 30,10])
    # Move the rectangle starting point
    ellipse13_x += ellipse13_change_x
    ellipse13_y += ellipse13_change_y
    pygame.draw.ellipse(screen, SUNYELLOW,[ellipse14_x, ellipse14_y, 20,10])
    # Move the rectangle starting point
    ellipse14_x += ellipse14_change_x
    ellipse14_y += ellipse14_change_y






#draw ufo

    pygame.draw.ellipse(screen, MOUNTAINGREY,[ellipse10_x, ellipse10_y, 30,10])
    # Move the rectangle starting point
    ellipse10_x += ellipse10_change_x
    ellipse10_y += ellipse10_change_y

    pygame.draw.ellipse(screen, BLACK,[ellipse9_x, ellipse9_y, 50,10])
    # Move the rectangle starting point
    ellipse9_x += ellipse9_change_x
    ellipse9_y += ellipse9_change_y



# draw comets passing by
    pygame.draw.ellipse(screen, BLACK,[ellipse7_x, ellipse7_y, 5,2])
    # Move the rectangle starting point
    ellipse7_x += ellipse7_change_x
    ellipse7_y += ellipse7_change_y

    pygame.draw.ellipse(screen, BLACK,[ellipse8_x, ellipse8_y, 5,2])
    # Move the rectangle starting point
    ellipse8_x += ellipse8_change_x
    ellipse8_y += ellipse8_change_y

    #draw mountains behind land
    pygame.draw.line(screen, MOUNTAINGREY , [0,500],[250,100],150)
    pygame.draw.line(screen, MOUNTAINGREY , [250,100],[200,700],150)
    pygame.draw.polygon(screen, MOUNTAINGREY , [[300,20], [325,100], [175,100]],0)
    pygame.draw.polygon(screen, MOUNTAINGREY , [[650,10], [600,450], [350,500]], 0)

    #draw the clouds moving
    pygame.draw.ellipse(screen, WHITE,[ellipse1_x, ellipse1_y, 50,20])
    # Move the rectangle starting point
    ellipse1_x += ellipse1_change_x
    ellipse1_y += ellipse1_change_y

    pygame.draw.ellipse(screen, WHITE,[ellipse2_x, ellipse2_y, 50,20])
    # Move the rectangle starting point
    ellipse2_x += ellipse2_change_x
    ellipse2_y += ellipse2_change_y

    pygame.draw.ellipse(screen, WHITE,[ellipse3_x, ellipse3_y, 50,20])
    # Move the rectangle starting point
    ellipse3_x += ellipse3_change_x
    ellipse3_y += ellipse3_change_y

    pygame.draw.ellipse(screen, WHITE,[ellipse4_x, ellipse4_y, 50,20])
    # Move the rectangle starting point
    ellipse4_x += ellipse4_change_x
    ellipse4_y += ellipse4_change_y

    pygame.draw.ellipse(screen, WHITE,[ellipse5_x, ellipse5_y, 50,20])
    # Move the rectangle starting point
    ellipse5_x += ellipse5_change_x
    ellipse5_y += ellipse5_change_y


    #draw the land
    pygame.draw.line(screen,SNOWGROUND ,[0, 500], [700, 400], 200)
    #draw trees
    pygame.draw.rect(screen,BROWN  ,[450,300,10,450],0)
    pygame.draw.line(screen,BROWN,[450,450], [450,100],5)
    pygame.draw.polygon(screen,TREEGREEN, [[450,20], [400,405], [500,405]], 0)
    pygame.draw.rect(screen,BROWN  ,[20,300,20,300],0)
    pygame.draw.polygon(screen,TREEGREEN, [[30,100], [0,400], [60,400]], 0)
    pygame.draw.rect(screen,BROWN  ,[250,300,20,300],0)
    pygame.draw.polygon(screen,TREEGREEN, [[250,100], [200,400], [300,400]], 0)
    pygame.draw.rect(screen,BROWN  ,[350,300,10,100],0)
    pygame.draw.polygon(screen,TREEGREEN, [[350,250], [400,370], [300,370]], 0)
    #draw bush
    draw_bush(screen, 10, 465)
    draw_bush(screen, 130, 430)
    draw_bush(screen, 360, 450)
    draw_bush (screen, 290, 400)
    #draw lake
    pygame.draw.ellipse(screen, WATERBLUE, [500,300,500,350],0)


#draw fish going left to rig                                      W   H
    pygame.draw.ellipse(screen, BLACK,[ellipse15_x, ellipse15_y, 20,10])
    # Move the rectangle starting point
    ellipse15_x += ellipse15_change_x
    ellipse15_y += ellipse15_change_y
    pygame.draw.ellipse(screen, BLACK,[ellipse16_x, ellipse16_y, 10,15])
    # Move the rectangle starting point
    ellipse16_x += ellipse16_change_x
    ellipse16_y += ellipse16_change_y

    pygame.draw.ellipse(screen, BLACK,[ellipse17_x, ellipse17_y, 20,10])
    # Move the rectangle starting point
    ellipse17_x += ellipse17_change_x
    ellipse17_y += ellipse17_change_y
    pygame.draw.ellipse(screen, BLACK,[ellipse18_x, ellipse18_y, 10,15])
    # Move the rectangle starting point
    ellipse18_x += ellipse18_change_x
    ellipse18_y += ellipse18_change_y

    pygame.draw.ellipse(screen, BLACK,[ellipse19_x, ellipse19_y, 20,10])
    # Move the rectangle starting point
    ellipse19_x += ellipse19_change_x
    ellipse19_y += ellipse19_change_y
    pygame.draw.ellipse(screen, BLACK,[ellipse20_x, ellipse20_y, 10,15])
    # Move the rectangle starting point
    ellipse20_x += ellipse20_change_x
    ellipse20_y += ellipse20_change_y







# draw wind moving from right to left
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 100,2])
    # Move the rectangle starting point
    rect_x += rect_change_x
    rect_y += rect_change_y

    # wind 2
    pygame.draw.rect(screen, WHITE, [rect2_x, rect2_y, 100,2])
    # Move the rectangle starting point
    rect2_x += rect2_change_x
    rect2_y += rect2_change_y

    # wind 3
    pygame.draw.rect(screen, WHITE, [rect3_x, rect3_y, 100,2])
    # Move the rectangle starting point
    rect3_x += rect3_change_x
    rect3_y += rect3_change_y

     # wind 4
    pygame.draw.rect(screen, WHITE, [rect16_x, rect16_y, 100,2])
    # Move the rectangle starting point
    rect16_x += rect16_change_x
    rect16_y += rect16_change_y

    pygame.draw.rect(screen, WHITE, [rect17_x, rect17_y, 100,2])
    # Move the rectangle starting point
    rect17_x += rect17_change_x
    rect17_y += rect17_change_y

    # wind 2
    pygame.draw.rect(screen, WHITE, [rect18_x, rect18_y, 100,2])
    # Move the rectangle starting point
    rect18_x += rect18_change_x
    rect18_y += rect18_change_y

    # wind 3
    pygame.draw.rect(screen, WHITE, [rect19_x, rect19_y, 100,2])
    # Move the rectangle starting point
    rect19_x += rect19_change_x
    rect19_y += rect19_change_y

     # wind 4
    pygame.draw.rect(screen, WHITE, [rect20_x, rect20_y, 100,2])
    # Move the rectangle starting point
    rect20_x += rect20_change_x
    rect20_y += rect20_change_y



#draw a bunch of birds from a far

     # bird 1
    pygame.draw.rect(screen, BLACK, [rect4_x, rect4_y, 5,2])
    # Move the rectangle starting point
    rect4_x += rect4_change_x
    rect4_y += rect4_change_y
    pygame.draw.rect(screen, BLACK, [rect5_x, rect5_y, 5,2])
    # Move the rectangle starting point
    rect5_x += rect5_change_x
    rect5_y += rect5_change_y
    # bird  2
    pygame.draw.rect(screen, BLACK, [rect6_x, rect6_y, 5,2])
    # Move the rectangle starting point
    rect6_x += rect6_change_x
    rect6_y += rect6_change_y
    pygame.draw.rect(screen, BLACK, [rect7_x, rect7_y, 5,2])
    # Move the rectangle starting point
    rect7_x += rect7_change_x
    rect7_y += rect7_change_y
    # bird 3
    pygame.draw.rect(screen, BLACK, [rect8_x, rect8_y, 5,2])
    # Move the rectangle starting point
    rect8_x += rect8_change_x
    rect8_y += rect8_change_y
    pygame.draw.rect(screen, BLACK, [rect9_x, rect9_y, 5,2])
    # Move the rectangle starting point
    rect9_x += rect9_change_x
    rect9_y += rect9_change_y
    # bird 4
    pygame.draw.rect(screen, BLACK, [rect10_x, rect10_y, 5,2])
    # Move the rectangle starting point
    rect10_x += rect10_change_x
    rect10_y += rect10_change_y
    pygame.draw.rect(screen, BLACK, [rect11_x, rect11_y, 5,2])
    # Move the rectangle starting point
    rect11_x += rect11_change_x
    rect11_y += rect11_change_y
    # bird 5
    pygame.draw.rect(screen, BLACK, [rect12_x, rect12_y, 5,2])
    # Move the rectangle starting point
    rect12_x += rect12_change_x
    rect12_y += rect12_change_y
    pygame.draw.rect(screen, BLACK, [rect13_x, rect13_y, 5,2])
    # Move the rectangle starting point
    rect13_x += rect13_change_x
    rect13_y += rect13_change_y
    # bird 6
    pygame.draw.rect(screen, BLACK, [rect14_x, rect14_y, 5,2])
    # Move the rectangle starting point
    rect14_x += rect14_change_x
    rect14_y += rect14_change_y
    pygame.draw.rect(screen, BLACK, [rect15_x, rect15_y, 5,2])
    # Move the rectangle starting point
    rect15_x += rect15_change_x
    rect15_y += rect15_change_y


# snow codes
    for i in range(len(snow_list)):

        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, snow_list[i],2)

        # Move the snow flake down one pixel
        snow_list[i][1] += 1

        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] >700:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 700)
            snow_list[i][0] = x



# Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

# Render the text. "True" means anti-aliased text.
# Black is the color. The variable BLACK was defined
# above as a list of [0, 0, 0]
# Note: This line creates an image of the letters,
# but does not put it on the screen yet.

    text = font.render("Winter in the Mountains",True,RED)


# Put the image of the text on the screen at 250x250
    screen.blit(text, [10, 470])




    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
