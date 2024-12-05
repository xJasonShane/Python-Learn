motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 删除指定索引元素
del motorcycles[0]
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 使用pop弹出指定元素
# 默认弹出最后一个元素
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# 函数填写索引值弹出指定元素
specify_motorcycles = motorcycles.pop(1)
print(specify_motorcycles)
print(motorcycles)