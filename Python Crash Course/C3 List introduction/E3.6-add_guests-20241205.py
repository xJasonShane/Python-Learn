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

print("Hi everyone, I found a bigger table, so I'm going to invite three more guests!")

guest_list.insert(0, 'Bruce')
guest_list.insert(2, 'Max')
guest_list.append('Vito')
print(f"Hi {guest_list[0]}! I invite you to dinner!")
print(f"Hi {guest_list[1]}! I invite you to dinner!")
print(f"Hi {guest_list[2]}! I invite you to dinner!")
print(f"Hi {guest_list[3]}! I invite you to dinner!")
print(f"Hi {guest_list[4]}! I invite you to dinner!")
print(f"Hi {guest_list[5]}! I invite you to dinner!")
print(f"Hi {guest_list[6]}! I invite you to dinner!")