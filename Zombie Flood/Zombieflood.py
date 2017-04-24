""" 
Tom Szendrey
March 4th 2015
Zombie flood fill assignement.
"""
import sys
f = open("H:\\My Documents\\Python\\zombiemap.txt", "r") 
#reads the first line and makes it the value of x
xlength = f.readline()
#reads the second line and makes it y
ylength = f.readline() 
zrows = f.readline() 
zcolumns = f.readline()

#this allows the x and y variables act as intigers
xlength = int(xlength)  
ylength = int(ylength)

zrows = int(zrows)
zcolumns = int(zcolumns)

#This will make a 2D array called cord, which will be as big as the range of ylength + 2, and the range of xlength
cord = [[0 for q in range(ylength + 2)]for q in range(xlength)] #makes the 2d array as big as it needs to be
#This + 2 is needed to reach the end of the text doct.
#The following will be used to fill in the 2D array one value at a tim
x = 0
y = 0
while(x < xlength):
    while(y < ylength + 2): #This 2 is needed to reach the end of the text doct.
        cord[x][y] = f.read(1) #This sets the value of the cord with its x and y components equal to 1 letter in the text doct.
        y += 1
    y = 0
    x += 1

#This function uses the import sys, and the cord variable
#This function will print the map properly using sys.stdoutwrite(), which will read the lines until it is told to create a new line.
#This allows me to print the text doctument as you would see it rather than having it print 1 letter per line.
def printmap(cord):
    for x in range(xlength):
        for y in range(ylength):
            sys.stdout.write(cord[x][y])
        sys.stdout.write("\n")

#This function uses the variables cord, zrows, zcolumnz, and the constant "Z"
#This function will be used to redefine the 2D array by using a recursion
def flood(cord, x, y, Zombie):
    xaxis = len(cord)
    yaxis = len(cord[0])

    #This means that if the position of the zombie is not a . stop.
    if cord[x][y] != ".":
        return
    #Change the cord of the zombie to a Z
    cord[x][y] = Zombie


    if x > 0: #This will go left
        flood(cord, x-1, y, Zombie)

    if y > 0: #This will go up
        flood(cord, x, y-1, Zombie)

    if x < xaxis-1: #This will go right
        flood(cord, x+1, y, Zombie) 

    if y < yaxis-1: #This will go down
        flood(cord, x, y+1, Zombie) 

#This function will check if the human is alive, or dead.
def checkhuman(cord):
    #This for loop will check every x, and y value to find when the cord is equal to H
    for x in range(xlength):
        for y in range(ylength):
            if cord[x][y] == "H": 
                if cord[x-1][y] == "Z" or cord[x+1][y] == "Z" or cord[x][y-1] == "Z" or cord[x][y+1] == "Z": #This will check up, down, left, or right of the human for zombies.
                    cord[x][y] = "Z" #If the human is beside a zombie, this will replace the H with a Z
                    print "You have died." 
                else:
                    print "You have lived."
    
   
printmap(cord) #This prints the original map first.

print #This is just for clarity between output
print

flood(cord, zrows, zcolumns, "Z") #This is used to redefine the variables in the 2D array.
checkhuman(cord) #This is used to check the human.
printmap(cord) #Now when I call to printmap the 2D array will have the new variables needed to print the end results.
f.close()





  
