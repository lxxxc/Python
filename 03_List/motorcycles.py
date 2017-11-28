bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# 直接输出列表
print("直接输出列表：" + str(bicycles))

# 输出列表元素
print("输出列表任意元素：" + str(bicycles[1].title()))

# 输出列表的最后一个元素
print("输出列表倒数第一个元素：" + str(bicycles[-1].title()))

# 输出列表的倒数第二个元素
print("输出列表倒数第二个元素：" + str(bicycles[-2].title()))


motorcycles = ['honda', 'yamaha', 'suzuki']
print("直接输出列表元素：" + str(motorcycles))

# 修改列表元素
motorcycles[0] = 'ducati'
print("修改列表任意元素：" + str(motorcycles))

#将元素添加到列表末尾
motorcycles.append('honda')
print("将元素添加到列表末尾：" + str(motorcycles))

#在列表中插入元素
motorcycles.insert(0, 'BMW')
print("在列表中插入元素：" + str(motorcycles))

#使用del语句删除元素：需要知道索引值
del motorcycles[0]
print("使用del语句删除元素：" + str(motorcycles))

#使用pop()方法删除元素：可以继续使用元素
#删除列表末尾元素
popped_motorcycle = motorcycles.pop()
print("使用pop()方法删除列表末尾元素：" + str(motorcycles) + " 删除的元素是：" + str(popped_motorcycle))

#删除列表任意位置元素
popped_motorcycle = motorcycles.pop(2)
print("使用pop()方法删除列表任意元素：" + str(motorcycles) + " 删除的元素是：" + str(popped_motorcycle))

#根据值删除元素
motorcycles.remove('ducati')
print("根据值删除元素：" + str(motorcycles))
