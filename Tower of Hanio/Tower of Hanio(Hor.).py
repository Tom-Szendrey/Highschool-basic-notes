"""
Tom Szendrey
3/23/2015
Tower of Hanio
"""
#Graphics
amount = int(input("How many blocks do you want, note much be more than 1: ")) #The following will ask the user how many blocks they want in the game
x = 0 #counter
block = [] #This is needed to define the list
while amount >= x: #the following will create the blocks in a list
    block.append("*"*(1+x))
    x += 1

#stack[0] (1st pillar) Stack[1] (2nd pillar) Stack[2] (3rd pillar)
Stack = [[],[],[]]
original = []

y = 1 #counter
while amount >= y:
    Stack[0].append(block[amount-y]) #Places the blocks in order in the 1st pillar
    original.append(block[amount-y]) #This will be used for the final while loop, this must be made here.
    y += 1

counter = 0
print Stack[0]
print Stack[1]
print Stack[2]
#This function will be used to ask the user where to move what blocks
#This function will check if that is a valid option, and if so will proceed in doing so
#This function will take the arguement Stack being Stack.
def userInput(Stack):
    take = int(input("Please type in 1, 2 or 3 to choose which you will take a block from "))
    give = int(input("Pick 1, 2, or 3 to choose where to place it "))
    take = take -1 #This is because the stack[0] is the first stack
    give = give -1

    if take == None or give == None: #If the user does not input any value for take or give (You wont need this with graphics and mouse clicks
        print #just for looks
        print "Sorry that is not a valid option please try again."
        print
        print Stack[0]
        print Stack[1]
        print Stack[2]
        return
    
    if take < 0 or take >= 3 or give < 0 or give >= 3: #This says that you cannot give or take a block from a pillar which does not exist
        print #just for looks
        print "Sorry that is not a valid option please try again."
        print
        print Stack[0]
        print Stack[1]
        print Stack[2]
        return
    
    if len(Stack[take]) == 0: #If the 1st choice stack has no value.
           print #just for looks
           print "Sorry you cannot take something from an empty pillar. Please try again."
           print
           print Stack[0]
           print Stack[1]
           print Stack[2]
           return

    if take <= 3:
        a = Stack[take].pop()
        if len(Stack[give]) != 0:
            b = Stack[give].pop() #redundent
            Stack[give].append(b) #redundent
            if len(Stack[give]) != 0 and a > b: #if the 2nd choice stack has a value, and if you're trying to place a bigger block onto a smaller block
                Stack[take].append(a)
                print
                print "Sorry you cannot place", a, "onto", b
                print Stack[0]
                print Stack[1]
                print Stack[2]
                return
        
    if take <= 3:       
        Stack[give].append(a) 
        print 
        print Stack[0]
        print Stack[1]
        print Stack[2]
  
while Stack[2] != original: #Trying to say while Stack[2] does not equal the original Stack[0]
    userInput(Stack)
    counter += 1
print "Finished"
print "It took you ", counter, "turns"

















