class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, User):
            return self.name.lower() == other.name.lower()
        return False


# Приклад використання
user1 = User("John")
user2 = User("john")
user3 = User("Alice")

print(user1 == user2)
print(user1 == user3)
