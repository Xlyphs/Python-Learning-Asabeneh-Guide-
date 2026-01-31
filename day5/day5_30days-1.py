empty_list = list()
listing=['mango' , 'apple', 'banana', 'pineapple','grape']
length = len(listing)
first_item, second_item, third_item, fourth_item, fifth_item = listing
print(first_item)
print(third_item)
print(fifth_item)
mixed_data = ['Xlyph', '19', '175','have a gf','123street']
it_companies =['Google','Meta','Apple','Microsoft','IBM','Oracle','Amazon']


it_companies[0] = 'GOOGLE'

joined_string = '#; '.join(it_companies)
print(joined_string)  # GOOGLE#; Meta#; Apple#; Microsoft#; IBM#; Oracle#; Amazon

it_companies.insert(4,'Tencent')
first, second, third,fourth,fifth,sixth,seventh,eighth = it_companies
long = len(it_companies)
print(long)
print(first , fourth , seventh)
does_exist = 'Apple' in it_companies
print(does_exist)

it_companies.sort(reverse=True)
print(it_companies)

slicing = it_companies[0:3]
print(slicing)

dicing = it_companies[-3:]
print(dicing)