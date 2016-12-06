with open('text.txt', 'r', encoding='utf-8') as a:
    text = a.read()
    quotes = text.split('\n')
n = 0
author = []
for quote in quotes:
    quote = quote.split('—')
    if "разум" in quote[0]:
        n = n+1
        author.append(quote[1])
print(n,"цитат, содержащих 'разум'")
for auth in author[:-1]:
    print(auth, end=", ")
print(author[-1])
