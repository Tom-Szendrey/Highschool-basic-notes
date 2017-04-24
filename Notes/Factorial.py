def main():
    num = int(input("Please enter a positive number "))
    while num != abs(num):
        num = int(input("Please re enter your number as a positive number "))
    fact = factorial(num)
    sF = str(fact)
    print "The amount of digits is ", len(sF)
    print
    print
    print "The factorial of ",num," is ",fact
 
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
 
main()
