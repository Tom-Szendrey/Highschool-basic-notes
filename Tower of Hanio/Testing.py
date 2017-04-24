import pygame
#appending to stack currently means nothing bud

#height reduced
#x value reduced
#after 7 blocks it looks bad, fix that shit yo
#rules
#need a variable that is the height on a stack
#start screeen
pygame.init()
white = (255,255,255)
greenblue = (0,255,255)
brown = (205,133,63)
background = pygame.image.load("background.png") #make is simplier 



gameDisplay = pygame.display.set_mode((700,700))
pygame.display.set_caption("Tower of Hanoi")
gameExit = False
#22.5 works with 100 (for x and width)
#Stack[0][0] = x value of first pillar, Stack[0][1] = y value of first pillar
#Stack = [[50, 400],[300, 400],[550, 400]],[],[]] #Stack[0] will become the first pillar's cord. ect ect
#Make blocks a dict. allowing you to place the whole blocks into a stack?
Stack = [[],[],[]]
dimensions = []
colour = []

amount = int(input("How many blocks do you want, note much be more than 1: ")) #The following will ask the user how many blocks they want in the game
amount = amount - 1 
x = 0
y = 0
width = 0
block = [0 for x in range(amount + 1)]

flag1 = 0 #counter
while flag1 <= amount: #the following will create the blocks in a list
    dimensions.append([10+x, 625-y, 125-width, 25]) #x,y,width,hieght
    flag1 += 1
    x += 6.25
    y += 25
    width += 12.5

flag2 = 0
q = 0
while flag2 <= amount: #The following will change the colour for each block
    colour.append([0,255-q,255-q])
    flag2 += 1
    q += 25

while gameExit == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                a = Stack[0].pop()
                #testing for 4 blocks
                #dimensions[amount] = [31.75+250, 550, 87.5, 25]  
                # UGHHHHH print dimensions[amount[0]]
                print block[amount]
                pygame.display.update()
                
                #if event.key == pygame.K_a:
                    #place on first pillar
                #if event.key == pygame.K_s:
                    #place on second pillar
                #if event.key == pygame.K_d:
                    #place on third pillar


            """
            #block[0][0] is x cord. of the block
                if #Stack is empty do the following:
                    block[amount][1] = 625
            if event.key == pygame.K_d:
                block[amount][0] += 250
                if #Stack is empty do the following:
                    block[amount][1] = 625
            """        

    
    gameDisplay.blit(background,(0,0))
    #x, y, width, height
    pygame.draw.rect(gameDisplay, brown, [0, 650, 700, 50]) #base
    pygame.draw.rect(gameDisplay, brown, [50, 400, 40, 900]) #first pillar
    pygame.draw.rect(gameDisplay, brown, [300, 400, 40, 900]) #second pillar
    pygame.draw.rect(gameDisplay, brown, [550, 400, 40, 900]) #third pillar
    
    flag3 = 0
    while flag3 <= amount: #Prints blocks
        block[flag3] = pygame.draw.rect(gameDisplay,colour[flag3],dimensions[flag3]) 
        flag3 += 1
        
    flag4 = 0
    while flag4 <= amount:
        Stack[0].append(block[flag4])
        flag4 += 1
    pygame.display.update()




pygame.quit()
quit()
