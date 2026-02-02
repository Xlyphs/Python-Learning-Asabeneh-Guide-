empty_tuple = ()
bro = ('Joshua','Felix','Noel')
sis = ('Cella','Chika')
siblings = bro + sis
print(len(siblings))
parents = ('Jhonny','Elizabeth')
family = parents + siblings
print(family)
father, mother , *sibling = family
print(father)
print(mother)

fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'eggs', 'cheese')
food_stuff =fruits + vegetables + animal_products
print(food_stuff)

food_stuff =list(food_stuff)
print(food_stuff)

middle_item_tp = food_stuff[4]
middle_item_lt = food_stuff[4]
print(middle_item_tp)

first_three = food_stuff[:3]
last_three = food_stuff[-3:]
print(first_three)
print(last_three)

del food_stuff

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print(f"is Estonia a nordic country {'Estonia' in nordic_countries}")
print(f"is Iceland a nordic country {'Iceland' in nordic_countries}")
