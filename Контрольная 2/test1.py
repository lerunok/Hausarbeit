fileread = open('text.xml', 'r', encoding = 'utf-8')
filewrite = open('res1.txt', 'w', encoding = 'utf-8')

text = fileread.read()
text = text[:text.index('</teiHeader>') + 12]
filewrite.write(str(text.count('\n')+ 1))

fileread.close()
filewrite.close()
    

