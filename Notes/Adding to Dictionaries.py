menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 #adding key/value pairs
print menu['Chicken Alfredo']

menu["spam"] = 2.50 #adding key/value pairs
menu["pi"] = 3.14   #format for this is dictname[newkey] = newvalue
menu["Block"] = 15
del menu["pi"] 



print "There are " + str(len(menu)) + " items on the menu."
print menu
