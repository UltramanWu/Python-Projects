import random
target = random.randint(1, 10)
temp = input("请输入猜测的数字：")
guess = int(temp)

count = 0
while guess != target and count <= 3:

    if guess > target:
        print("大了！")
    else:
        if guess < target:
            print("小了！")
    temp = input("猜错了，请重新猜一遍：")
    guess = int(temp)

    count += 1

if guess == target:
    print("猜对了！")
else:
    print("抱歉，猜测次数已经足够多了")
print("Game Over!")

