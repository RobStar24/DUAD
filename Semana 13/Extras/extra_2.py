def requires_login(func):
    def wrapper(user_logged_in, *args, **kwargs):
        if not user_logged_in:
            raise PermissionError("User not authenticated")
        return func(user_logged_in, *args, **kwargs)

    return wrapper


@requires_login
def view_profile(user_logged_in):
    print("Showing user profile")


user_logged_in = True
try:
    view_profile(user_logged_in)
except PermissionError as ex:
    print(ex)


user_logged_in = False
try:
    view_profile(user_logged_in)
except PermissionError as ex:
    print(ex)
