import random
import colorama
from colorama import Fore, Back, Style


colorama.init()
words = open("slova5bykvwordly", "r", encoding='utf-8').read().split("\n")
randomslowo = random.choice(words)

def solo ():
    while True:
        print("вы играте solo или duo?")
        igr = input()
        if igr == "solo" or igr == "duo":
            break
        else:
            print("если хотите играть один, пишите solo, если c другом, то duo")
        continue
    if igr == "duo" and len(igr) <= 5:
        print("введите слово которое хотите загадать, оно должно быть длиной 5 букв")
        slovo = input()
        if slovo in words:
            randomslowo = slovo
        else:
            print("такого слова не существует")
            return
    print("введите слово:")
    for i in range(5, 0, -1):
        print(Style.RESET_ALL + f" осталось попыток: {i}")
        a = input()
        if a not in words:
            print("этого слова не существует")
            break
        if len(a) > 5:
            print("слово длинее 5 букв")
            break
        if a == randomslowo:
            print(f"вы угадали слово, потребовалось попыток: {i}")
            return
        for k in range(5):
            Style.RESET_ALL
            if a[k] in randomslowo:
                b = randomslowo.find(a[k])
                if k == b:
                    c = a[k]
                    print(Back.GREEN + c, end="")
                else:
                    print(Back.YELLOW + a[k], end="")
            else:
                print(Style.RESET_ALL + a[k], end="")
    print(Style.RESET_ALL + ", к большому сожалению вы не отгадали слово, загаданное слово:", randomslowo)



print("готовы играть?")
while True:
    play = input()
    if play == "yes":
            if play == "yes":
                 solo()
            break
    else:
        print("если хотите играть скажите yes")
        continue



