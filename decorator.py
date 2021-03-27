# Python Decorator Function
import time

# def decorator_function(function):
#     def wrapper_function():
#         function()
#     return wrapper_function()


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()
    return wrapper_function # ()는 방아쇠다. 장전만 하고 방아쇠는 당기지 않는다.

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

decorated_funtion = delay_decorator(say_greeting)
decorated_funtion()