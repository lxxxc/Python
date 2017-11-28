# 使用列表的一部分
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("原始列表为：" + str(players))

#提取列表的前3个元素
print("提取列表的前3个元素：" + str(players[0:3]))

#提取列表的前4个元素
print("提取列表的前4个元素：" + str(players[:4]))

#提取列表的第2个元素到最后的所有元素
print("提取列表的第2个元素到最后的所有元素：" + str(players[1:]))

#提取列表的最后3个元素
print("提取列表的最后3个元素：" + str(players[-3:]))

#遍历列表的最后3个元素
for player in players[-3:]:
    print(player)

