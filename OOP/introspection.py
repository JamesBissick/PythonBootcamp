# # Instrospection
# wiz2 = Wizard('Merlin', 60, age=77)
# print(dir(wiz2))

class Toy:
    def __int__(self, color, price):
        self.color = color
        self.price = price


action_figure = Toy()
# print(action_figure.__str__())
print(str(action_figure))  # special function, other way of calling it