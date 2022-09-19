from random import randint
names = ["John", "Jack"]
total_pencils = 0
who_is = 0


def who_is_first():
    # index = 0
    # try:
    #     index = int(names.index(input()))
    # except ValueError:
    #     print("Choose between '" + names[0] + "' and '" + names[1] + "'")
    #     who_is_first()
    # return index
    n = input()
    if n == names[0]:
        return 0
    elif n == names[1]:
        return 1
    else:
        print("Choose between '" + names[0] + "' and '" + names[1] + "'")
        who_is_first()


def how_many_pencils():
    pencils = input()
    if not pencils.isnumeric():
        print("The number of pencils should be numeric")
        how_many_pencils()
    else:
        pencils = int(pencils)
        if total_pencils == 0:
            if pencils == 0:
                print("The number of pencils should be positive")
                how_many_pencils()
        else:
            if pencils > 3:
                while not (pencils == 1 or pencils == 2 or pencils == 3):
                    print("Possible values: '1', '2' or '3'")
                    try:
                        pencils = int(input())
                    except Exception:
                        continue
                # how_many_pencils()
            if pencils > total_pencils:
                print("Too many pencils were taken")
                if(total_pencils - 2) == 0:
                    total_pencils - int(input())
                    print(names[(who_is + 1) % 2] + " won!")
                    return pencils
                if (total_pencils - 1) == 0:
                    total_pencils - int(input())
                    print(names[(who_is + 1) % 2] + " won!")
                    return pencils
                how_many_pencils()
    return pencils


def ill_lose():
    global total_pencils
    random_pencils = randint(1,3)
    if random_pencils > total_pencils:
        random_pencils = total_pencils
    total_pencils -= random_pencils
    print(random_pencils)


def ill_win(many_pencils):
    global total_pencils
    if many_pencils == 2:
        total_pencils -= 1
        print(1)
    elif many_pencils == 3:
        total_pencils -= 2
        print(2)
    else:
        total_pencils -= 3
        print(3)


def im_bot():
    mod_pencils = total_pencils % 4
    if mod_pencils == 1:
        ill_lose()
    else:
        ill_win(mod_pencils)


print("How many pencils would you like to use:")
total_pencils = how_many_pencils()
print("Who will be the first (John, Jack):")
# who_is = who_is_first()
who_is = input()
while who_is != 0 and who_is != 1:
    if who_is == names[0]:
        who_is = 0
    elif who_is == names[1]:
        who_is = 1
    else:
        print("Choose between '" + names[0] + "' and '" + names[1] + "'")
        who_is = input()

while total_pencils > 0:
    print("|" * total_pencils)
    print(names[who_is] + "'s turn:")
    if who_is == 0:
        took_pencils = how_many_pencils()
        total_pencils -= took_pencils
    else:
        im_bot()
    if total_pencils == 0:
        print(names[(who_is + 1) % 2] + " won!")
    who_is = (who_is + 1) % 2
