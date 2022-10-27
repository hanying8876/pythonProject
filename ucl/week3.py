n=int(input('how many?'))

num=0
for i in range(n):
    v=float(input('number'+str(i+1)+':'))
    num=num+v
print('average is', num / n)
# 限定个数，且可以终止

# 中英文对应
# list=列表，单个格子，并存在顺序不能重复
# tuples=不能更改，元组，有序且可以重复
# sets=集合，无序
# dictionaries=字典，一一对应且无序

# just execute this to write the file
# 文件 需要打开文件然后进行读(r)或写(w)的操作 with open(文件名，‘w’或‘r’) as f:
# 如果不写'r'或'w'，就默认读
lines = ["apple 5\n", "kiwi 12\n", "cereals 2\n"]
with open("my_grocery.txt", "w") as f:
    for line in lines:
        f.write(line)
# 最好使用with！！要么文件还需要关闭，如果文件不关闭在写入环节会默认一直存在于缓冲区，这样会慢，关闭后进入磁盘清空缓冲区
li='apple 5\n ,kiwi 12\n ,cereals 2\n '
print(li.split(" "))

# 怎么将文件内容写成字典
my_grocery = {}
with open("my_grocery.txt", "r") as f:
    for line in f.readlines():
        tokens = line.split(" ") # 分开字符串和数值，通过引号和空格
        item = tokens[0] # 键
        quantity = int(tokens[1]) # 值
        my_grocery[item] = quantity # 给键赋值

print(my_grocery)

print('\nquiz')
values = ('college', [5, 15, 30], (50, 150, 250))
print(values[2])
print(values[2][2]) # 取第二个集合中的第二个

s_1 = {100, 200, 300, 400}
s_2 = {500, 200, '100', 600}
s_3 = s_1.union(s_2)
print(s_3)

test_dic = {1: 2, 3: 4, 5: 6}
result = 1
for i in test_dic.keys(): # 取key，而不是值
    result *= i # 求阶乘
print(result)

# 有点东西
orders = [{'a': 100, 'b': 150, 'y': 200}, {'x': 120, 'y': 220}, {'a': 300, 'x': 200}]

total = {}

# 这里的值是相加的
for i in range(len(orders)):

    for k in orders[i].keys():

        if k not in total.keys():
            total[k] = 0

        total[k] += orders[i][k]

print(total)

a = {1:1, 2:4, 3:9, 4:16, 5:25}
print(a.pop(4))
print(a)