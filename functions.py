from re import X


def say_hi(name):
    return "Hi " + name
greeting = say_hi("Michael")
print(greeting)


def add(a, b):
    x = a + b
    return x
sum1 = add(4, 6)
sum2 = add(1, 4)
sum3 = sum1 + sum2
print(sum1, sum2, sum3)


