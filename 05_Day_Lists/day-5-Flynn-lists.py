empty_list = []
print(len(empty_list))

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['tomato', 'potato', 'cabbage', 'onion', 'carrot']
animal_products = ['milk', 'cheese', 'yoghurt', 'meat', 'butter']

print('Fruits:', fruits)
print('Number of Fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of Vegetables:', len(vegetables))
print('Animal Products:', animal_products)
print('Number of Animal Products:', len(animal_products))


lst = ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}]

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
last_fruit = fruits[3]
print(last_fruit)
last_index = len(fruits) - 1
last_fruit = fruits[last_index]


lst = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)