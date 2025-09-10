def log_params_and_return(func):
    def wrapper(*args, **kwargs):
        print(f"Received Params: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Function's return: {result}")
        return result

    return wrapper


@log_params_and_return
def add(a, b):
    return a + b


@log_params_and_return
def greet(name="Carlos"):
    return f"Hello, {name}"


add(15, 20)
greet("Gloria")
