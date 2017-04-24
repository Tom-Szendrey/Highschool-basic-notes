#Opens file, reads each line and stores it to a variable, closes the file.
f = open ("c:\\Programing\\ComputerClass\\Python\\zombietext.txt", "r+")
xlength = f.readline()
ylength = f.readline()
zrow = f.readline ()
zcolumn = f.readline ()

#Turns the the strings into integers 
xlength = int(xlength) #this allows the x and y variables act as intigers (i can add and subtract from them)
ylength = int(ylength)

x = 0
y = 0

#Creates array called array
array = [[0 for x in range(ylength)]for x in range(xlength)]

while (x < xlength):
    while (y < ylength):
         array [x][y] = f.read (1)         
         x = x + 1
    x = 0
    
    y = y + 1
    
    
f.close
