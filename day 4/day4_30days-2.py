company = 'Coding For All'
text = 'Coding For All'
print(text[0])
print(text[-1])
print(text[10]) #space
print(text.index('C'))
print(text.index('F'))

phrase = "Coding For All People"
print(phrase.rfind('l'))

phrase2 ="Python For Everyone"
acronym =''.join(word[0] for word in phrase2.split())
print(acronym)

acronym2 =''.join(word[0] for word in company.split())
print(acronym2)