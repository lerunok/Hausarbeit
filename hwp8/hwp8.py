def openfile(file):
    words = []
    with open ('text.txt', 'r', encoding='utf-8') as f:
        for line in f.read().replace('\n', ' ').split():
            words.append(line.lower())
    for i in range(len(words)):
        words[i] = words[i].strip('.,!?*()«»\'";:-')
    return words

def countw(words):
    count_with = 0
    count_without = 0
    omnis = []
    non_omnis = []
    omnis_words = []
    non_omnis_words = []
    for i in range(len(words)):
        if words[i].startswith("omni"):
            count_with += 1
            omnis.append(words[i])
            if words[i] not in omnis_words:
                omnis_words.append(words[i])
    for word in omnis_words:
        word_new = word[4:]
        non_omnis_words.append(word_new)
        for i in range(len(words)):
            if word_new == words[i]:
                count_without += 1
                non_omnis.append(words[i])
    print("С приставкой omni- встретилось", count_with, "слов(а).")
    print("____________________________________________________________________")
    for word in omnis_words:
        n = omnis.count(word)
        print("Для слова", word, "встретилось", n, "примеров(a).")
    print("____________________________________________________________________")
    print("Тех же слов, но без приставки omni- встретилось", count_without, "штук(и).")
    if count_without != 0:
        print("____________________________________________________________________")
        for word in non_omnis_words:
            n = non_omnis.count(word)
            if n != 0:
                print("Для слова", word, "встретилось", n, "примера(ов).")

def main():
    countw(openfile(input('Введите имя файла: ')))

main()
