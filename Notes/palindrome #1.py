"""
Tom Szendrey
Feb. 19th 2015
This program checks to see if a word is a palindrome.
"""
x = "Y"

while x == "Y":
    word = raw_input("Which word would you like to check to see if it is a palindrome? ")
    forwards = word.replace(" ", "")
    backwards = forwards[::-1]

    forwards.lower()
    backwards.lower()

    if len(forwards) > 0:
        print word + " This is your selected word"
    else:
        print "you have not created a valid word"

    if backwards == forwards:
        print word + ": is a palindrome"
    else:
       print word + ": is not a palindrome"
    x = raw_input("Would you like to use this program? (Y for yes)")

while x != "Y":
    exit()
