"""
Tom Szendrey
3/23/2015
Tower of Hanio
"""

#If user inputs nothing allow them to retry
print "This is Tower of Hanio. \n"

amount = int(input("How many blocks do you want, note much be more than 0: ")) #The following will ask the user how many blocks they want in the game
block = [] #This is needed to define the list
x = 0 #counter
q = amount 
while amount >= x: #the following will create the blocks in a list
    block.append("*"*(1+x)+(" ")*(q)) #This way all blocks will have the same amount of spaces
    x += 1
    q -= 1

#stack[0] (1st pillar) Stack[1] (2nd pillar) Stack[2] (3rd pillar)
Stack = [[],[],[]]
original = []
y = 1 #counter
while amount >= y:
    Stack[0].append(block[amount-y]) #Places the blocks in order in the 1st pillar
    original.append(block[amount-y])
    y += 1

counter = 0

#This function will be used to print the stacks vertically
#This function will be given the amount of blocks, and the phrase in which to tell the user, ie: invalid movement
def printFunction(amount, phrase):
    print phrase
    print "\n"
    flag = amount
    spaces = amount + 1
    while flag != 0:
        flag -= 1
        print 
        try:
            print Stack[0][flag],
        except:
            print " "*spaces, #prints the length of empty spaces n
        try:
            print Stack[1][flag],
        except:
            print " "*spaces,
        try:
            print Stack[2][flag], 
        except:
            print " "*spaces
    return

printFunction(amount, "Starting: ")

#This function will be used to ask the user where to move what blocks
#This function will check if that is a valid option, and if so will proceed in doing so
#This function will take the arguement Stack being Stack.
def userInput(counter):
    print
    take = int(input("Please type in 1, 2 or 3 to choose which you will take a block from "))
    give = int(input("Pick 1, 2, or 3 to choose where to place it "))
    take = take -1 #This is because the stack[0] is the first stack
    give = give -1

    if len(Stack[take]) == 0: #If the 1st choice stack has no value.
        printFunction(amount, "Sorry that pillar is empty.")
        return

    
    if take < 0 or take >= 3 or give < 0 or give >= 3: #This says that you cannot give or take a block from a pillar which does not exist
        printFunction(amount, "Sorry that is an invalid option please try again.")
        return
        
    
    if take <= 3:
        a = Stack[take].pop()
        if len(Stack[give]) != 0:
            b = Stack[give].pop() #This allows me to label b
            Stack[give].append(b) #This places b back to its spot
            if len(Stack[give]) != 0 and a > b: #if the 2nd choice stack has a value, and if you're trying to place a bigger block onto a smaller block
                Stack[take].append(a)
                printFunction(amount, ("Sorry you cannot place ", a, "on ", b))
                return
                

    if take <= 3:       
        Stack[give].append(a)
        printFunction(amount, "Valid move.")
        

    


        
while Stack[2] != original: #Trying to say while Stack[2] does not equal the original Stack[0]
    userInput(counter)
    counter += 1
print "Finished"
print "It took you ", counter, "turns"


