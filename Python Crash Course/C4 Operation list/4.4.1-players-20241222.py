players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
# 如果没有指定第一个索引，Python将自动从列表开头开始
print(players[:4])
# 如果没有制定末尾索引，Python将会自动截止到列表最后一个元素
print(players[2:])
# 输出列表倒数的元素可以采用负数索引方法
print(players[-3:])
# 可在表示切片的方括号内指定第三个值。这个值告诉Python在指定范围内每隔多少元素提取一个
print(players[0:3:2])