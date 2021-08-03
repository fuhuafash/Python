import time  # 导入time模块
from rich.console import Console  # 导入模块

console = Console()

account = input('Please enter account:')  # 输入账号

password = input('Please enter password:')  # 输入密码

try:  # 检测是否为整型
    password = int(password)
except Exception:
    console.print('Error:That not is number!',style='bold red')

time.sleep(0.5)

times = 3  # 有3次输入机会
for i in range(times):
    times = times - 1

    if times == 0:  # 检测剩余机会
        break

    if account == 'admin' and password == 123456:  # 检测账号密码是否正确
        print('You are logged in to the system')  # 提示进入并退出循环
        choice = input('Please enter 0 to open data：')
        print('\n')
        try:
            choice = int(choice)
        except Exception:  # 检测是否为整型
            console.print('Error:That not is number!', style='bold red')

        if choice == 0:
            systemdata = open(r'data\systemdata.txt')
            data = systemdata.read()
            print(data, '\n')

        break
    else:  # 错误时继续循环
        console.print('Error:Please check your account or password!', style='bold red')
        print('You have', times, 'chance!')
        account = input('Please enter account:')
        password = input('Please enter password:')
        time.sleep(0.5)
        try:  # 检测是否为整型
            password = int(password)
        except Exception:
            console.print('Error:That not is number!', style='bold red')

input('Please push-button to exit')
