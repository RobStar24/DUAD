def greater_than_10():
    users_time = int(input("Enter the time in seconds \n"))

    if users_time < 6000:
        remaining_seconds = users_time - 6000
        return remaining_seconds
    elif users_time > 6000:
        return "Greater"
    else:
        return "Equal"


print(greater_than_10())
