class User():
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        name = self.name
        return name.capitalize()

    def age(self, current_year):
        age = current_year - self.birthyear
        return age


user = User(birthyear=1999, name="John")
user_age = user.age(2023)
user_name = user.get_name()
print(user_age)
print(user_name)
