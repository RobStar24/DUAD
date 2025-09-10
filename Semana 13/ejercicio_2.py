def validate_numbers(func):
    def wrapper(*args, **kwargs):

        for i, arg in enumerate(args):
            if not isinstance(arg, (int, float)):
                raise ValueError(
                    f"Argument in position {i} must be a number, received: {type(arg).__name__}"
                )

        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise ValueError(
                    f"Argument {value} must be a number, received: {type(value).__name__}"
                )

        return func(*args, **kwargs)

    return wrapper


@validate_numbers
def multiply(a, b):
    return a * b


@validate_numbers
def add(x, y, z=0):
    return x + y + z


print(multiply(5, 3))
print(add(1, 2, z=3))
# print(multiply(5, "three"))
