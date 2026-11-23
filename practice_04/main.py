# Задание 1 
x = 17  # внешняя (глобальная) переменная (за функцией)

def show():
    x = 7   # локальная переменная (внутри функции)
    print(x) 

show()
print(x)

# ВЫВОД:
# 7
# 17


# Задание 2 
def total(*args):
    return sum(args)

print(total(7, 8, 9))


# Задание 3 
def person(**kwargs):
    name = kwargs.get("name", "Гость")
    age = kwargs.get("age", 0)
    return name, age

print(person(name="Мария", age=18))


# Задание 4 
def increase(x):
    return x + 2

def apply(func, value):
    return func(value)

print(apply(increase, 4))


# Задание 5 
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)

countdown(4)
