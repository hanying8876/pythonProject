# CRS=坐标参考系统
# 方括号中少一个，第一个是0，多出来的数字没有对应字符就不输出，负数从-1开始倒着数
# 如果：后不填的话，默认到字符串结尾
print('hello'[-4] + 'and'[1:4] + 'ehthe'[2:6] + 'world')
x = 'fizzbuzz'[2:]
print(x)
name = 'John Snow'
print(name[5:7])
# 判断可以不管类型是否一致都可以进行比较
a = 1 + 10
b = str(11)
print(a == b)
# 字符串可以查看是否存在于另一个字符串，看前者是否出现于后者，不能反过来
print('hello' in 'world')
print('hello' not in 'world')
print('he' in 'hello')
print('hello' in 'he')
# 解释下面为何>0和int相加可行
print(True + 1, False)
# 十进制直接输入，二进制要用0b开头，八进制要有0o开头，十六进制用0x
print(33, 0b001110, 0o234567, 0x3A)
# 两个*是^，**2=^2
var_a = 2
var_b = 2
var_c = (var_a + var_b) ** 2
print(var_c)
value_a = 2 ** 2
value_b = value_a ** 3
print(value_a)
print(value_b)
# if语句+input
a = int(input())
b = 2

if b > 1:
    if a < 2:
        c = a + 4
    elif a > 2:
        c = a + 3
    else:
        c = a + 2
else:
    c = a + 1

print(c)
# 特别的是虚数用j来表示而不是i，(.real)是指数的实部，(.imag)是指数的虚部
print(1 + 5j, 1 + 5j.real, 1 + 5j.imag)
# %取余数，//整除
a = 26 // 5 + 7 % 3 - 2 ** 3
b = 26 // 5
c = 7 % 3
print(a, b, c)
s = [1, 2, 3, 'a', 4, 5]
s[4] = 1
print(s)
# 卧槽这是什么鬼东西？int还能TM加判断，什么狗！详细见上面print(true+1
number = 2.7
r_number = int((3000 - (number * 1000)) / 200) + ((3000 - (number * 1000)) % 200 > 0)
r = (3000 - (number * 1000)) % 200 > 0
m = int((3000 - (number * 1000)) / 200)
print('the number you are looking for is = ' + str(r_number))
print(r, m)
#  !=是不等于
a = 1 + 10
b = 11
c = [1, 2, 3]
if a == b or c[100]:
    print('The statement after or will be not executed when the statement before or is True.')
if a != b and c[100]:
    print('The statement after and will be not executed when the statement before and is False.')
# str()直接转换类型+[]选取字符串内字符转化成int
number = str(156785152)
print('lucky number is =' + str(3 * int(number[2]) + int(number[-2]) % 2))
# 有多边形记得检验角度和，可以第一个排除
# 循环语句 forloop和whileloop
for n in range(5):
    print("hello")
# whileloop
i = 1
while i < 7:
    print(i)
    i += 1  # i=i+1 终止循环，同时使得数值符合默认，计算机默认从0开始
# break语句
i = 1
while i < 7:
    print(i)
    if i == 3:
        break
    i += 1
# continue语句
i = 0
while i < 7:
    i += 1
    if i == 3:
        continue
    print(i)


# define函数
def sum(a, b, c):
    return a + b + c


print(sum(2, 2, 3))

a = 0
b = 1
while b < 10:
    print(b)
    c = b
    b = a + b
    a = c

# 星期改写为while函数，需要在loop里面包含输入的变量，只有不属于1-7时代码才能停止
n = int(input('Please enter an integer: '))

while n >= 1 and n <= 7:
    if n == 1:
        print('Monday')
    elif n == 2:
        print('Tuesday')
    elif n == 3:
        print('Wednesday')
    elif n == 4:
        print('Thursday')
    elif n == 5:
        print('Friday')
    elif n == 6:
        print('Saturday')
    elif n == 7:
        print('Sunday')

    n = int(input('Please enter an integer: '))

print('The provided integer does not correspond to a day!')

# for函数星期改写，以下输入的第一个数决定代码循环几次
n = int(input('Please enter an integer: '))

for i in range(n, 0, -1):
    if n == 1:
        print('Monday')
    elif n == 2:
        print('Tuesday')
    elif n == 3:
        print('Wednesday')
    elif n == 4:
        print('Thursday')
    elif n == 5:
        print('Friday')
    elif n == 6:
        print('Saturday')
    elif n == 7:
        print('Sunday')
    else:
        print('The provided integer does not correspond to a day!')
    if i > 1:
        n = int(input('Please enter an integer: '))

# 求方差和平均值
num = 0.0 # variable initialization
squared_num = 0.0

n = int(input('Number of inputs: '))

for i in range(n):
    a = float(input('Insert value number ' + str(i + 1) + ': '))
    num = num + a
    squared_num = squared_num + a**2

mean = num/n
variance = squared_num/n - mean**2

print('The mean is', mean, 'and the variance is', variance)
