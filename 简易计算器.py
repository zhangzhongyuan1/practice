def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print('欢迎使用计算器')
print('--------------------------------------')
print('计算器有如下的功能')
print('1.加法 \n2.减法 \n3.乘法 \n4.除法')

choice=input('请选择您的计算(1/2/3/4)')
num1=int(input('请输入您的第一个数字:'))
num2=int(input('请输入您的第二个数字:'))

if choice=='1':
    print(num1,'+',num2,'=',add(num1,num2))

elif choice=='2':
    print(num1,'-',num2,'=',subtract(num1,num2))

elif choice=='3':
    print(num1,'*',num2,'=',multiply(num1,num2))

elif choice=='4':
    print(num1,'/',num2,'=',divide(num1,num2))

else:
    print('无效输入，请重新输入')
