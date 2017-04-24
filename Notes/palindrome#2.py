"""
Tom Szendrey
Feb. 20th 2015
This program checks to see if a word is a palindrome.
"""

word = raw_input("Which word would you like to check to see if it is a palindrome? ")
forwards = word.replace(" ","")
forwards = forwards.lower()

while len(forwards) % 2 == 0:
    half = len(forwards) / 2
    first = forwards[0:half]
    last = forwards[half:len(forwards)]
    last = last[::-1]
    if first == last:
        print "This is a palidrome, and has an even amount of digits."
    else:
        print "This is not a palidrome"
    break
#make a loop to check if the back of last, is the same as the front of first

while len(forwards) % 2 != 0:
    
    half = (len(forwards) / 2) - int(0.5)
    first = forwards[0:half]
    last = forwards[half + 1:len(forwards)]
    last = last[::-1]
    if first == last:
        print "This is a palidrome, and has an odd amount of digits"
    else:
        print "This is not a palidrome"
    break


    
