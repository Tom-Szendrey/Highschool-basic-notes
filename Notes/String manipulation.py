#String manipulation practice
f = open("C://Programing//ComputerClass//Test.txt")
message = f.read()
print message
print "Length is: ", len(message)
print "T's are now R's: \n", message.replace("T", "R")
print "One line: \n", message.replace("\n", "")
print "No spaces: \n", message.replace(" ", "")
counter = 0
x = 0
message = message.replace("\n"," ")
while x < len(message):
    if message[x] == " ":
        counter += 1
    x += 1
print "Counter: ", counter
