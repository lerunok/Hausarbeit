import os
def countdirs(path):
    countf= 0
    for root, dirs, files in os.walk(path):
        filearr = [file for file in files if file.endswith('.') == True]
        for file in filearr:
            files.pop(file)
        dictionary = {f[-1:-3]:' ' for f in files}
        if len(dictionary)+len(filearr) != len(files):
            countf +=1
    print(countf)

def main():
    countdirs('.')

main()
