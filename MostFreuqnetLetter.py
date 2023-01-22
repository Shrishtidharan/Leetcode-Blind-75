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


or 

#
def mostfreq(word):
    ltrcount={}
    for ltr in word:
        ltrcount[ltr] = 1+ ltrcount.get(ltr,0)
    maxi = max(ltrcount.values())
    for key , value in ltrcount.items():
        if value == maxi:
            return key
def findmostfreq(sentence):
    for word in sentence:
        print(mostfreq(word))
        
sentence = list(input().split())
findmostfreq(sentence)
