import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_fuction():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f'{function.__name__} run speed: {end_time - start_time}')

    return wrapper_fuction


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        var = i * i


@speed_calc_decorator
def slow_function():
    for i in range(1000000):
        var = i * i


fast_function()
slow_function()
