import random

list = []
list.append("your mom")
list.append("what the hell is going on")
for x in list:
    print(x)


def dice_d20():
    d20 = random.random(1, 20)
    print(d20)
    return d20


def main():

    def function(input1, input2):
        number = input1 + input2
        if (number < 2):
            print("vetsi jak dva")
        return number
