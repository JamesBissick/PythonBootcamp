# OOP

class User:
    membership = True  # Class object attribute (static)

    def __init__(self, name, age):
        if self.membership:
            self.name = name  # attribute
            self.age = age

    def run(self):
        print(f'{self.name} is running..')

    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old.')

    def attack(self):
        print('Do nothing!!')

    # Class methods
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Jonas', num1 + num2)

    # Static methods
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


# Inheritance
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        self.num_arrows = self.num_arrows - 1
        print(f'{self.name} attacks with arrows, arrows left: {self.num_arrows}')


class Wizard(User):
    def __init__(self, name, power, age):
        super().__init__(name, age)  # Inherits the parent class properties
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)  # Runs
        print(f'{self.name} throws a fireball, using {self.power} mana')


# Basics of OOP
# player1 = User('Jake', 21)
# player2 = User('May', 34)
# player2.drink = 'Feels refreshed'

# print(player1.name)
# print(player1.run())  # Returns none because run function doesn't return anything
# print(player2.age)

# print(player1.drink)  # Error
# print(player2.drink)

# print(User.adding_things(2, 3))
#
# # Inheritance
# archer1 = Archer('Kaster', 50)
# print(archer1.attack())
# print(archer1.run())
#
#
# # Polymorphism
# def player_attack(char):
#     char.attack()
#
#
# wiz1 = Wizard('Oblask', 25, age=34)
# print(wiz1.attack())
#
# player_attack(archer1)

