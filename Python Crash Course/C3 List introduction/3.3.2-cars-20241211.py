# 使用sorted()函数对列表元素进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# 传参进行反向排序
print(sorted(cars,reverse=True))