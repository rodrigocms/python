
# Method 1
book_title=['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter={}

for word in book_title:
    if word in word_counter:
        word_counter[word]=1
    else:  
        word_counter[word]+=1

#Method 2
book_title=['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter={}
for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1        

print(word_counter)