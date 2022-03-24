arr=[10,6,12,3,17,9]
#left pointer and right pointer
#lp -buy and rp -sell 
lp,rp=0,1
maxp=0
while rp< len(arr):
    if arr[rp]>arr[lp]:
        profit=arr[rp]-arr[lp]
        maxp=max(maxp,profit)
    else:
        # shifting the buyp to sell p
        lp=rp
    rp=rp+1
print(maxp)
    
