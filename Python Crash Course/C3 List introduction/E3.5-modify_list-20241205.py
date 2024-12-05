guest_list = ['Jason', 'Shane', 'Jenson', 'Jack']
print(f"Hi {guest_list[0]}! I invite you to dinner!")
print(f"Hi {guest_list[1]}! I invite you to dinner!")
print(f"Hi {guest_list[2]}! I invite you to dinner!")
print(f"Hi {guest_list[3]}! I invite you to dinner!")

print(f"Due to other reasons, {guest_list.pop(2)} cannot participate in this dinner.")
guest_list.insert(2, 'Thompson')
print(f"Hi {guest_list[0]}! I invite you to dinner!")
print(f"Hi {guest_list[1]}! I invite you to dinner!")
print(f"Hi {guest_list[2]}! I invite you to dinner!")
print(f"Hi {guest_list[3]}! I invite you to dinner!")