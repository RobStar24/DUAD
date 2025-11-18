from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass

    @property
    def name(self):
        return self._name


class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
        return "Admin"

    def has_permission(self, permission):
        return True


class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
        return "Regular User"

    def has_permission(self, permission):
        allowed_permissions = ["read"]
        return permission.lower() in allowed_permissions


user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

print(user1.has_permission("delete"))
print(user2.has_permission("delete"))

print(user1.has_permission("read"))
print(user2.has_permission("read"))
