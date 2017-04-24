class Meal(object):

    def __init__(self, initial):
        self.price= initial

    def printPrice(self):
        return(self.price)

    def calcTax(self,rate):
        self.tax= self.price*rate
        #return(self.tax) jsing if yah do this print tax isnt needed
    
    def printTax(self):
        return(self.tax)


lunch = Meal(50)
lunch.calcTax(0.2)
print lunch.printTax()
