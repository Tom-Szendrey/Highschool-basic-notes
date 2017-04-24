word = raw_input("Which word would you like to check to see if it is a palindrome? ")

forwards = word.replace(" ", "")

backwards = forwards[::-1]

if len(forwards) > 0:
    print forwards + " This is your selected word"
else:
    print "you have not created a valid word"


if backwards == forwards:
    print forwards + " is a palindrome"
else:
    print forwards + "  is not a palindrome"


