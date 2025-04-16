import random
import colorama
from colorama import Fore, Back, Style


colorama.init()
words = open("slova5bykvwordly", "r", encoding='utf-8').read().split("\n")
randomslowo = random.choice(words)


def solo ():
     for i in range(5):
        a = input()
        if len(a) > 5:
            print("слово длинее 5 букв")
            break
        if a == randomslowo:
            print("вы угадали слово, потребовалось попыток:" + i)
        for k in range(5):
            if a[k] in randomslowo:
                b = randomslowo.find(a[k])
                if k == b:
                    c = a[k]
                    print(Back.GREEN + c, end="")
                else:
                    print(Back.YELLOW + a[k], end="")
            else:
                print(Style.RESET_ALL + a[k], end="")
def duo ():
     print("duo")

print("вы играете solo или duo")
while True:
    play = input()
    if play == "solo" or play == "duo":
            if play == "solo":
                 solo()
            else:
                 duo()
            break
    else:
        print("если играете один то пишите solo, если вдвоем, то duo")
        continue



