ifile=open("fruits.txt")
dict_words={}

for line in ifile:
    words=line.split()
    for word in words:
        dict_words[word]=dict_words.get(word,0)+1
list_words=[]
for key,val in dict_words.items():
    list_words.append((val,key))
list_words.sort(reverse = True)
print("first 10 slices of sorted dictionary are:\n")
print(list_words[0:10])
ifile.close()
