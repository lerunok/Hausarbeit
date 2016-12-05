count = 0
score = 0
with open('repka.txt', 'r', encoding='utf-8') as a:
    for text in a:
        str = text.split()
        score += len(str)
        for word in str:
            if word[0].istitle():
                count +=1
total = count/score*100
print('Слов с большой буквы: ', total, '%', sep ='')
