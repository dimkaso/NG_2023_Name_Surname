import math
value_a = int(input("Value ax²: a= "))
value_b = int(input("Value bx: b= "))
value_c = int(input("Value c: c= "))

#The condition for deriving the formula - changes to +
if value_c < 0:
    print(f'{value_a}x²+{value_b}x{value_c}')
if value_c >= 0:
    print(f'{value_a}x²+{value_b}x+{value_c}')

# How to find D (formula)
D = value_b**2 - 4*value_a*value_c 
print(f'Discriminant= {D}:')

# There are no roots
if D <0:
    print("If D < 0, there are no roots;")

# There is exactly one root
if D  == 0:
    print('If D = 0, there is exactly one root;')
    x = -value_b/2*value_a
    print(x)

# There is exactly two root
if D > 0:
    print('If D > 0,there is exactly two root ')
    x1 = (-value_b + math.sqrt(D))/ (2*value_a)
    x2 = (-value_b - math.sqrt(D))/ (2*value_a)
    print(f'x1 = {x1} and x2 = {x2}')