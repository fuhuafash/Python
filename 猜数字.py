import random                                                           #导入random模块
from rich.console import Console                                        #导入rich.console模块
console = Console()

guess = random.randint(0,100)                                           #生成0-100的随机整数
keyopen = 0
game = 0


while game == 0:

    input('按下任意键开始游戏\n')

    print('猜想 0-100 的数字\n')

    if keyopen == 1:
        print(guess)

    chance = 10                                                         #有10次机会
    for i in range(chance):
        print('你现在还有',chance,'次机会!\n')
        chance = chance - 1

        if chance == 0:
            console.print('你已经没有机会了!\n')
            game = 1
            break

        number = (input('请输入所猜的数字:'))
        print()
        try:                                                            #检测是否为整型
            number = int(number)
        except Exception:
            console.print('你输入好像不是数字！\n', style='bold red')
            game = 0
            break

        if number > guess:
            print('猜大了\n')

        if number < guess:
            print('猜小了\n')

        if number == guess:
            print('猜中了!\n')
            break


    game = input('输入0继续游戏，输入1结束游戏')
    if game == 100:
        keyopen = 1
        game = 0
        break

    try:                                                                #检测是否为整型
        game = int(game)
    except Exception:
        console.print('你输入好像不是数字！\n', style='bold red')
        break

input('单机任意键退出')