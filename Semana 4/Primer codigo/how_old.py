def ages_classification(age):
    if age <= 2:
        return 'baby'
    elif age <= 10:
        return 'child'
    elif age <= 13:
        return 'preteen'
    elif age <= 18:
        return 'teen'
    elif age <= 35:
        return 'young adult'
    elif age <= 65:
        return 'adult'
    else:
        return 'senior'
    

def get_data():
    name = input("What's your name? \n")
    last_name = input("What's your last name? \n")
    age = int(input("What's your age? \n"))

    category = ages_classification(age)

    if category == 'adult':
        print(f"{name} {last_name} is an {category}")
    else:
        print(f"{name} {last_name} is a {category}")

get_data()




              