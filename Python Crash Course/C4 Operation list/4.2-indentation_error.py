# 忘记缩进
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)

# 逻辑错误
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

# 不必要的缩进
message = "Hello Python world!"
    print(message)

# 循环后不必要的缩进
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    print("Think you, everyone. That was a great magic show!")

# 遗漏的冒号
magicians = ['alice', 'david', 'carolina']
for magician in magicians
    print(magician)