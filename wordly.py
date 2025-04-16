import random



print("вы играете solo или duo")
while True:
    play = input()
    if play == "solo" or play == "duo":
            break
    else:
        print("если играете один то пишите solo, если вдвоем, то duo")
        continue

words = open("slova5bykvwordly", "r", encoding='utf-8').read().split("\n")
randomslowo = random.choice(words)
print(randomslowo)