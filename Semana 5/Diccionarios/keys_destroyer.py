list_of_keys = ["department", "salary"]
employee = {
    "name": "Alice",
    "email": "alice@techcorp.com",
    "department": "IT",
    "salary": 75000,
    "location": "NY",
}


def remove_keys(dictionary, keys_to_remove):
    for key in keys_to_remove:
        if dictionary.get(key):
            dictionary.pop(key)

    return dictionary


print(remove_keys(employee, list_of_keys))
