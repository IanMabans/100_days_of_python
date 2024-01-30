def add(*args):
    print(args[0])
    summ = 0
    for n in args:
        summ += n

    return summ


print(add(3, 5, 7, 8, ))


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs['add']
    n += kwargs['multiply']
    print(n)


calculate(5, add=3, multiply=5, divide=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.model)


def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)


bar(1, 2)


def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)


bar(toast='nah', spam=4, eggs=2)


def test(*args):
    print(args)


test(1, 2, 3, 5)


def test(*args):
    print(args)


test(1, 2, 3, 5)