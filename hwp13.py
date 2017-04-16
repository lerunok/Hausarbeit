import os
import re
def filelist():
    names = os.listdir ('.')
    files = [name for name in names if os.path.isfile(name) == True]
    return files

def filesearch(files):
    names = [re.search(r'(.*)\.(.*)', name) for name in files]
    return names

def filespunct(names):
    arrfilespunct = [key.group(0) for key in names if re.search('[.,!_;]', key.group(1)) != None]
    return arrfilespunct


def exercise():
    allelem = os.listdir('.')
    files = [name for name in allelem if os.path.isfile(name) == True]
    files = filesearch(files)
    arrdirects = [name for name in allelem if os.path.isdir(name) == True]
    filenames = [file.group(1) for file in files]
    unicarray = []
    for name in files:
        if name.group(1) not in unicarray:
            unicarray.append(name.group(1))
        for name in arrdirects:
            if name not in unicarray:
                unicarray.append(name)
        return unicarray

def main():
    print('1')
    for word in filespunct(filesearch(filelist())):
        print(word)
    print('2')
    for word in exercise():
        print(word)
main()
