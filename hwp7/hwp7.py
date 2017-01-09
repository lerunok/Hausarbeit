import random
def nounslist():
    # существительные
    n = open('nouns.txt', 'r', encoding = 'utf-8')
    nouns = n.read()
    nouns = nouns.split()
    n.close()
    return nouns
def verbslist():
    # сослагательное наклонение
    v = open ('verbsInd.txt', 'r', encoding = 'utf-8')
    verbsInd = v.read()
    verbsInd = verbsInd.split()
    v.close()
    return verbsInd
def verbsimplist():
    # повелительное наклонение
    vi = open('verbsImp.txt', 'r', encoding='utf-8')
    verbimps = vi.read()
    verbimps = verbimps.split()
    vi.close()
    return verbimps
def verbsCondlist():
    # условноe наклонениe
    v1 = open('verbsCond.txt', 'r', encoding = 'utf-8')
    vp1 = v1.read()
    vp1 = vp1.split()
    v1.close()
    return vp1
def noun():
    nouns = nounslist()
    n = random.choice(nouns)
    return ('la ') + n
def verb():
    verbsInd = verbslist()
    verbInd = random.choice(verbsInd)
    return verbInd
def verbImp():
    verbsImp = verbsimplist()
    verbImp = random.choice(verbsImp)
    return verbImp
def verbCond():
    verbsCond = verbsCondlist()
    verbCond = random.choice(verbsCond)
    return verbCond
def sentence(s, t="."):
    st = ' '.join(s)
    st += t
    st = st.capitalize()
    return st
def questsentence(s, k = "?"):
    st = ' '.join(s)
    st += k
    st = st.capitalize()
    return st
def indic():
    indic = [noun(), verb(), noun()]
    return sentence(indic)
def negat():
    negat = [noun(), 'ne', verb(), 'pas', noun()]
    return sentence(negat)
def question():
    question = ['qui', verb(), noun()]
    return questsentence(question)
def imper():
    imper = [verbImp(), noun(),', s´il te plaît']
    return sentence(imper)
def condit():
    condit = [noun(), verbCond(), noun()]
    return sentence(condit)
def text():
    sentences = [indic(), negat(), question(), imper(), condit()]
    random.shuffle(sentences)
    for i in range(len(sentences)):
        print(sentences[i])
text()

