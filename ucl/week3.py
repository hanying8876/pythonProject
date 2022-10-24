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
lines = ["apple 5\n", "kiwi 12\n", "cereals 2\n"]
with open("my_grocery.txt", "w") as f:
    for line in lines:
        f.write(line)
# complete the code
my_grocery = {}
with open("my_grocery.txt", "r") as f:
    for line in f.readlines():
        tokens = line.split(" ")
        item = tokens[0]
        quantity = int(tokens[1])
        my_grocery[item] = quantity

print(my_grocery)


