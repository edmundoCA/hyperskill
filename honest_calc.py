# write your code here
msg_ = ["Enter an equation",
        "Do you even know what numbers are? Stay focused!",
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "Yeah... division by zero. Smart move...",
        "Do you want to store the result? (y / n):",
        "Do you want to continue calculations? (y / n):",
        " ... lazy",
        " ... very lazy",
        " ... very, very lazy",
        "You are",
        "Are you sure? It is only one digit! (y / n)",
        "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)"]
result = 0
memory = 0
answer = "y"


def is_one_digit(v):
    if -10 < v < 10 and float(v).is_integer():
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_[7]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)


while True:
    if answer == "y":
        while True:
            print(msg_[0])
            calc = input()
            x, oper, y = calc.split()
            if x == "M":
                x = memory
            if y == "M":
                y = memory
            try:
                x = float(x)
                y = float(y)
            except ValueError:
                print(msg_[1])
                continue
            else:
                if oper == "+" or oper == "-" or oper == "*" or oper == "/":
                    check(x, y, oper)
                    if oper == "+":
                        result = x + y
                    elif oper == "-":
                        result = x - y
                    elif oper == "*":
                        result = x * y
                    elif oper == "/" and y != 0:
                        result = x / y
                    else:
                        print(msg_[3])
                        continue
                else:
                    print(msg_[2])
                    continue
            print(result)
            while True:
                print(msg_[4])
                answer = input()
                if answer == "y":
                    # memory = result
                    if is_one_digit(result):
                        msg_index = 10
                        while msg_index <= 12:
                            print(msg_[msg_index])
                            # print(eval(f"msg_{msg_index}")) while msg_0, msg_1, ..., msg_12
                            answer = input()
                            if answer == "y":
                                if msg_index < 12:
                                    msg_index += 1
                                else:
                                    memory = result
                                    break
                            elif answer == "n":
                                break
                    else:
                        memory = result
                    break
                elif answer == "n":
                    break
            break
    elif answer == "n":
        break
    print(msg_[5])
    answer = input()
