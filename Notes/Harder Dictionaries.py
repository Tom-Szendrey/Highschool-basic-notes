inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 


inventory["pocket"] = "seashell", "strange berry", "lint"   #create pocket which is a list in in inventory              
inventory["backpack"].remove("dagger")                      #removes dagger in backpack
inventory["gold"] += 50                                     #adds 50 cash money
inventory["backpack"].sort()                                #sorts backpack 

print "This is your inventory." , inventory 
print "This is your gold.", inventory["gold"]
print "This is what is in your backpack." , inventory["backpack"]

