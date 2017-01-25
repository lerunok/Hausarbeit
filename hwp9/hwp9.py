import random

def fileopen():
    with open('dict.csv', 'r', encoding = 'utf-8') as f:
        file = f.readlines()
        dictionary = {}
        for row in file:
            string = row.split(', ')
            string[1] = string[1].strip()
            dictionary[string[0]] = string[1]
        return dictionary
    
def guess():
    dictionary = fileopen()
    array = sorted(dictionary.keys())
    word = str(random.choice(array))
    p = dictionary[word]
    print(p + 'что?')
    i = 3
    while i != 0:
        i-=1
        w = input('Твоя догадка: ')
        if w == word:
            print('Верно!')
            break
        else:
            if i == 0:
                print('Неверно, это было слово '+word)
                break
            t = print('Число оставшихся попыток:'+str(i))
            
def main():
    guess()
    a = input('Играть еще?\n')
    if a == ('да' or 'Да'):
        main()
    else:
        print('До свидания!')
main()
