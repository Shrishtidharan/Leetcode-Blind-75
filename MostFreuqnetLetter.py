def mostfreq(word):
    ltrcount={}
    for ltr in word:
        ltrcount[ltr] = 1+ ltrcount.get(ltr,0)
    maxfreq=max(zip(ltrcount.values(),ltrcount.keys()))[1]
    return maxfreq
    
def findmostfreq(sentence):
    for word in sentence:
        print(mostfreq(word))
        
sentence = list(input().split())
findmostfreq(sentence)
