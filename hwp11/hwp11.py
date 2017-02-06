import re

def readfile():
    list=[]
    file = open('hh.html', 'r', encoding='UTF-8')
    for line in file:
        line=line.strip('\n')
        list.append(line)
    file.close()
    return list

def str_sphere():
    infobox=readfile()
    sphere=''
    q=0
    for line in infobox:
        if 'Отряд:' in line:
            sphere=infobox[q+2]
            break
        else:
            q+=1
    return sphere

def main():
    form=re.findall('>[а-я -]+</a>', str_sphere())
    list=''
    for el in form:
        el=el.strip('></a')
        with open('data.txt', 'a', encoding = 'utf-8') as f:
            f.write(el)
main()
