import string

def text_analysis(paragraph):
    translator=str.maketrans("","" , string.punctuation)
    cleaned_text = paragraph.translate(translator).lower()

    words = cleaned_text.split()
    frequency = {}
    for word in words:
        frequency[word]=frequency.get(word,0)+1

    longest_word = max(words,key=len)if words else None

    sentences=0
    for ch in (paragraph):
        if ch in (".!?"):
            sentences+=1
    print(f"total words:{len(words)}")
    print(f"total unique words:{len(frequency)}")
    print(f"longest word:{longest_word}")
    print(f"number of sentences:{sentences}")
    print("\n---word frquencies---")
    for word,count in frequency.items():
        print(f"{word}:{count}")

paragraph=input("enter paragraph for analysis:\n")
text_analysis(paragraph)
    
