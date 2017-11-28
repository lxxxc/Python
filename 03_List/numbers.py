# 使用range()函数生成数字序列
print("使用range()函数生成数字序列")
for value in range(1, 5):
    print(value)

# 使用list()函数创建列表
print("使用list()函数创建列表")
numbers = list(range(1, 6))
for number in numbers:
    print(number)

# 使用list()函数创建列表，并指定步长
print("使用list()函数创建列表，并指定步长")
even_numbers = list(range(2, 11, 2))
for even_number in even_numbers:
    print(even_number)

# 使用range()函数创建数字集
print("使用range()函数创建数字集")
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# 找出列表中的最大值、最小值、总和
print("最大值为：" + str(max(squares)))
print("最小值为：" + str(min(squares)))
print("和为：" + str(sum(squares)))

# 使用列表解析创建列表
squares = [value ** 2 for value in range(1, 11)]
print("使用列表解析创建列表：" + str(squares))




