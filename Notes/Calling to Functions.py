def one_good_turn(n):
    return n + 1
    
def deserves_another(n):
    return one_good_turn(n) + 2

print(one_good_turn(1))
x = deserves_another(5)
print(x)
