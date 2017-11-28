cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

#使用sort()方法对列表进行永久性排序
cars.sort()
print("使用sort()方法对列表进行永久性排序：")
print(cars)

cars.sort(reverse=True)
print("使用sort()方法对列表进行永久性排序：")
print(cars)

#使用sort()函数对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("使用sort()函数对列表进行临时排序：" + str(sorted(cars)) + " 原始列表为：" + str(cars))

#使用reverse()方法对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("使用reverse()方法对列表进行反转,原始列表为：" + str(cars))
cars.reverse()
print("使用reverse()方法对列表进行反转：" + str(cars))

#使用len()函数获取列表长度
print("列表长度为：" + str(len(cars)))
