import random as random
money = []
print("We add you 100$")
money.append(100)
list = ['lemon', 'orange', 'grape']
random_list = []
def func(money, list, random_list):
    quest = input("Start [Y/N]\n> ")
    for i in range(3):
        if quest == "Y":
            random_list.append(random.choice(list))
    if len(set(random_list)) == 1:
        print("You are won")
        print(random_list)

        random_list.clear()
        money.append(money[-1]+50)
        print("your count", money[-1])
    else:
        print("You lose")
        print(random_list)
        random_list.clear()
        money.append(money[-1] - 50)
        print("your count", money[-1])
    if quest == "N":
        pass
    print("Do you want again?")
    inp = input("Again? [Y/N]\n> ")
    if inp == "Y":
        func(money, list, random_list)
    elif inp == "N":
        print("Bye")
func(money, list, random_list)
