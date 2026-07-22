import random

# 取1-100随机值,6次机会
answer = random.randint(1, 100)
chances = 6
attempts = 0

#同while chances > 0:
while chances:
    try:
        # 输入一个数字
        guess = int(input("请输入一个整数(0-100):"))

    # 排除整数外的输入,不减少次数
    except ValueError:
        print("错误:请输入一个整数(0-100)!\n")
        continue

    attempts += 1

    # 检测:如果等于该数,则输出答对文本并结束
    if guess == answer:
        print(f"您在第{attempts}次时答对了,该数为{answer}\n")
        break

    # 如果大于该数,则输出大于文本并减少一个机会次数
    elif guess > answer:
        print(f"您猜的{guess}大了")

    # 如果小于该数,则输出小于文本并减少一个机会次数
    else:
        print(f"您猜的{guess}小了")

    chances -= 1
    if chances > 0:
        print(f"还有{chances}次机会\n")

# 如果机会次数等于0,则输出机会用尽文本
if chances == 0:
    print(f"机会用完了,该数是{answer}\n")
