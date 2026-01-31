#String
s1 = 'Thirty\tdays\tof\tpython'
s2 = 'coding\tfor\tall'
print(s1 , s2)

#variable
company = 'Coding For All'
print(company)
print(len(company))
#case conversion
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
#searching
first_word = company[:6]
print('Coding' in company)
print(company.index('Coding'))
print(company.find('Coding'))
new_company = company.replace('Coding', 'Python')
print(new_company)

phrase ="Python For Everyone"
short_phrase = phrase.replace('Everyone', 'All')
print(short_phrase)

words = phrase.split(' ')
print(words)

companies = "Facebook, Google, Microsoft, Twitter, Instagram, YouTube"
company_list = companies.split(' ')
print(company_list)
