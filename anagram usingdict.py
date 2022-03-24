#Count the occurance of each of the charecter
#and add in hashmap,Compare the hashmap to check is this anagram

flag2=0

scount,tcount={},{}
s=input("Enter the 1st name-:")
t=input("Enter 2nd name-:")
for x in range (len(s)):
    #To avoid key error we r using get function,bcz initially the first key may not be present
    scount[s[x]]=1+scount.get(s[x],0)
    tcount[t[x]]=1+tcount.get(t[x],0)
#Compare both the hashmap with key
#here k is the key,we compare the values with the key
for k in scount:
    if scount[k]!=tcount.get(k,0):
        flag2=0
        print("False")
        break
        
    else:
        flag2=1
if(flag2==1):
    print("True")


