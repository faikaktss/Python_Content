# def changeName(n):
#     n = 'ada'

# name = 'yiğit'

# changeName(name)
# print(name)

# def change(n):
#     n[0] = 'istanbul'

# sehirler = ['ankara','izmir']

# change(sehirler[:])

# print(sehirler)

def add(*params):
     sum = 0
     for n in params:
         sum = sum + n
     return sum

print(add(10, 20, 50))
print(add(10, 20, 30))
print(add(10, 20, 30,34,79,27))

def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name= 'Çınar', age =2, city = 'istanbul')
displayUser(name= 'Ada', age =12, city = 'kocaeli',phone ='12345')
displayUser(name= 'Yiğit', age =14, city = 'ankara', phone = '112345', email = 'yiğit@gmail.com' )

