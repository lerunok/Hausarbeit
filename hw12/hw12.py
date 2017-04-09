            
def opentext():
    f = open('text.txt', 'r', encoding='utf-8')
    text = f.read()
    f.close()
    return text


def splitsent(text): 
    text = text.replace('?', '.')
    text = text.replace('!', '.')
    text = text.replace(':', '.')
    return text


def sentences(text):
    sarray = [sentence for sentence in text.split('.')]
    return sarray


def midlength(sentence):
    arr = [len(word.strip('./",:;-—()!?')) for word in sentence.split()]
    mid = round(sum(arr)/len(sentence.split()), 1)
    return mid


def dictsentences(sarray):
    dictionary = {sentence: midlength(sentence) for sentence in sarray if len(sentence.split()) > 10}
    return dictionary


def printout(dictionary):
    out = [key+' '+'\nЭто предложение со словами длины {}'.format(dictionary[key]) for key in dictionary]
    for i in out:
        print(i)


def main():
    printout(dictsentences(sentences(splitsent(opentext()))))


if __name__ == "__main__":
    main()
