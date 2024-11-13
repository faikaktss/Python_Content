# def greeting(name):
#     print('hello', name)

# print(greeting('ali'))
# print(greeting)
# sayHello = greeting
# del sayHello
# print(sayHello)
# print(greeting)

# encapsulation
# def outer(num1):
#     print('outer')
#     def inner_increment(num1):
#         print('inner')
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1, num2)

# outer(10)



def factoriyel(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")

    if not number >=0:
        raise ValueError("number must be zero or positive")

    def inner_factoriyel(number):
        if number <= 1:
            return 1

        return number * inner_factoriyel(number - 1)

    return inner_factoriyel(number)
try:
    print(factoriyel(-4))
except Exception as ex:
    print(ex)