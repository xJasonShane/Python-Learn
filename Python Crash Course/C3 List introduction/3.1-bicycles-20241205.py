bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 3.1.1
print(bicycles[0])  # 返回列表第一个元素
print(bicycles[0].title())

# 3.1.2
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])  # 返回列表最后一个元素，-2代表倒数第二个，以此类推

# 3.1.3
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)