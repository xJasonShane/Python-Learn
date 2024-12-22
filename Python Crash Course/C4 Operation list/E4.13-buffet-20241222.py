buffet = ('rice', 'noodles', 'beef', 'chicken', 'pork')
for food in buffet:
    print(food)
# buffet[0] = 'bread'  # TypeError: 'tuple' object does not support item assignment
buffet = ('bread', 'noodles', 'beef', 'chicken', 'pork')
for food in buffet:
    print(food)