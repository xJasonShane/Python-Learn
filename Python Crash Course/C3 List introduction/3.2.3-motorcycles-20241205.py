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

# 根据值内容删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)
# .remove 方法只删除列表内出现的第一个所选值，如果列表内存在多个该值需要使用循环方法进行全部删除或其他操作