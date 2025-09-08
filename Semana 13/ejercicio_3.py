from datetime import datetime


class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = datetime.now()
        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (
            self.date_of_birth.month,
            self.date_of_birth.day,
        ):
            age -= 1

        return age


def check_adult_age(func):
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise PermissionError(
                "The User is a minor and cannot access the restricted area."
            )
        return func(user, *args, **kwargs)

    return wrapper


@check_adult_age
def access_restricted_area(user, *args, **kwargs):
    print("Welcome User, you are an adult, you are allowed to enter.")


try:
    user1 = User(datetime(2005, 6, 25))
    access_restricted_area(user1)
except PermissionError as ex:
    print(ex)

try:
    user2 = User(datetime(2010, 1, 1))
    access_restricted_area(user2)
except PermissionError as ex:
    print(ex)
