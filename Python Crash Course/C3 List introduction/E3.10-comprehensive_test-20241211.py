countrys = ['China', 'United States', 'United Kingdom', 'Japan']
# 访问列表元素
print(countrys)
print(countrys[0])

# 修改列表中的元素
countrys[2] = 'Brazil'
print(countrys)

# 添加列表内元素
countrys.append('Nepal')
print(countrys)

countrys.insert(3, 'Korea')
print(countrys)

# 删除列表元素
del countrys[5]
print(countrys)

# 弹出元素
popped = countrys.pop()
popped2 = countrys.pop(2)
print(popped)
print(popped2)
print(countrys)

# 添加元素继续操作
countrys.append('Japan')
countrys.append('Brazil')
countrys.append('Russia')
print(countrys)

# 根据值删除元素
countrys.remove('Brazil')
print(countrys)

# 对列表永久排序
countrys.sort()
print(countrys)
# 反向排序
countrys.sort(reverse=True)
print(countrys)
# 临时排序
print(sorted(countrys))
print(countrys)
# 翻转列表
countrys.reverse()
print(countrys)
# 测算列表长度
print(len(countrys))