savings = 5000000

while True:
    name = input("请输入您的用户名:").strip()

    if name:
        break
    else:
        print("!!用户名不能为空!!\n")

def back():
    input("按下回车键返回菜单\n")


def balance():
    print("\n----------查询余额----------")
    print(f"用户\"{name}\"的余额为:{savings}\n")
    back()


def deposit():
    print("\n----------存款----------")
    global savings
    while True:
        user_input = input("请输入需要存款的金额(输入q/Q返回菜单):").strip()
        if user_input.lower() == 'q':
            print("输入回车键确认返回")
            back()
            break

        try:
            deposits = float(user_input)
        except ValueError:
            print("!!请输入有效金额!!")
            continue

        if deposits <= 0:
            print("!!请输入有效金额!!")
            continue
        else:
            savings += deposits
            print(f"存款成功,用户\"{name}\"当前的余额为:{savings}\n")
            back()
            break


def withdraw():
    print("\n----------取款----------")
    global savings
    while True:
        user_input = input("请输入需要取款的金额(输入q/Q返回菜单):").strip()
        if user_input.lower() == 'q':
            print("输入回车键确认返回")
            back()
            break

        try:
            withdraws = float(user_input)
        except ValueError:
            print("!!请输入有效金额!!")
            continue

        if withdraws > savings:
            print("!!您的余额不足!!")
            continue
        elif withdraws <= 0:
            print("!!请输入有效金额!!")
            continue
        else:
            savings -= withdraws
            print(f"取款成功,用户\"{name}\"当前的余额为:{savings}\n")
            back()
            break


def menu():
    print(f"-----用户\"{name}\",欢迎来到市银行-----")
    print("查余额\t[输入0]")
    print("存款\t\t[输入1]")
    print("取款\t\t[输入2]")
    print("退出\t\t[输入q/Q]")


while True:
    menu()
    num = input("请输入对应的业务代码:").strip()

    if num.lower() == 'q':
        print("\n----------已退出程序----------")
        break
    try:
        num = int(num)
    except ValueError:
        print("!!请输入正确的业务代码!!\n")
        continue

    if num not in (0, 1, 2):
        print("!!请输入正确的业务代码(0查余额,1存款,2取款,q退出)!!\n")
        continue

    if num == 0:
        balance()
        continue
    elif num == 1:
        deposit()
        continue
    else:
        withdraw()
        continue
