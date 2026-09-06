para = input("Enter a paragraph: ")
words = para.split()

freq={}

for w in words:
    freq[w]=freq.get(w,0)+1

sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print("Top 3 frequent words:")
for word, count in sorted_words[0:3]:
    print(word, ":", count)
