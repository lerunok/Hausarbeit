import re

fileread = open('text.xml', 'r', encoding = 'utf-8')
filewrite = open('res2.txt', 'w', encoding = 'utf-8')
text = fileread.read()

types = []
result = re.finditer('<w lemma = [^>]*>', text)
for match in result:
    sametext = match.group()
    printtext = sametext[sametext.index('type="') + 6: -2]
    if printext in types:
        types[printtext] += 1
    else:
        types[printtext] = 1
        
for printtext in types:
    filewrite.write(printtext + ': ' + str(types(printtext)) + '\n')

fileread.close()
filewrite.close()
    

