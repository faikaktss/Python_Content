# Identy Operator: is

# x = y = [1, 2, 3]
# z = [1, 2, 3]

# print(x==y)
# print(x==z)
# print(x is z)
# print(x is y)


x = [1, 2, 3]
y = [2, 4]

del x[2]
y[1] = 1
y.reverse()

print(x==y)
print(x is y)

# Membership Operator: in

x = ['apple','banana']
print('banana' in x) 

name = 'çınar'
print('a' in name)