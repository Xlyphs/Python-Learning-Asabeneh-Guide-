companies = ['Google', 'Meta', 'Apple', 'Microsoft', 'IBM', 'Oracle', 'Amazon']
middle_company = companies[3]
print(middle_company)
del companies[0]
del companies[3]
del companies[-1]
print(companies)

del companies[:]
print(companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
combined = front_end + back_end
full_stack = combined.copy()
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

min_age = ages[0]
max_age = ages[-1]
ages.append(min_age)
ages.append(max_age)
print(ages)

length = len(ages)
middle = ages[length // 2]
print(middle)

avg_age = sum(ages) / length
print(avg_age)

ages_range = ages[0:length//2]
print(ages_range)

min_to_average = ages_range.index(min(ages_range))
print(min_to_average)
max_to_average = ages_range.index(max(ages_range))
print(max_to_average)

compare = abs(ages_range[min_to_average]-ages_range[max_to_average])
print(compare)