import datetime


def log_call(func):
    def wrapper(*args):
        func_name = func.__name__
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"func:{func_name} - args: {args} - [{current_time}]")

        result = func(*args)

        print(f"Result: {result}")

        return result

    return wrapper


def validate_numbers(func):
    def wrapper(*args):
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise ValueError("All arguments must be numbers.")
        return func(*args)

    return wrapper


@validate_numbers
@log_call
def multiply(a, b):
    return a * b


try:
    multiply(5, 3)
    multiply("7", 5)
except Exception as ex:
    print(ex)
