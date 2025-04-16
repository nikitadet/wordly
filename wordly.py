print("вы играете solo или duo")
while True:
    play = input()
    if play == "solo" or play == "duo":
            break
    else:
        print("если играете один то пишите solo, если вдвоем, то duo")
        continue
