from string import punctuation
import helper

data = h.read('basics/pride_n_prejudice.txt')
print(len(data))

#remove punctuation
for p in punctuation:
    data = data.replace(p,'')

#split into words and remove spaces and empty strings
word =[word.strip()for word in data .lower().split()]
print("TOTAL WORDS FOUND:",len(word))
print("UNIQUE WORDS FOUNDS:",len(set(word)))

# first a dictionary
wc={}
for word  in word:
    if word in wc:
        wc[word]+= 1
    else:
        wc[word] =1
     

#shorting the dictionary

wc =sorted(wc.items(),key =lambda x: x[1],reverse =True)

#print the top 10 words
for i in range(10): 
    print(wc[i])





