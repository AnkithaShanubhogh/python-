with open("file1.txt","r")as ifile:
    lines=ifile.readlines()

words=[]

for line in lines:
    for word in line.strip().split():
        word=word.strip("!?>.,:;")
        if  word:
            words.append(word)
words.sort()
print(words)

with open("file2.txt","w")as ofile:
    for word in words:
        ofile.write(word + "\n" )
ofile.close()
        
