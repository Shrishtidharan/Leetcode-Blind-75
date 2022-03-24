#To predict the largest area for the bucket to hold max water
height=[100,80,60,20,50,40,80,30,70]
#Bruteforce-Checking every possible lp and rp
maxwaterarea=0
for lp in range(len(height)):
    for rp in range(lp+1,len(height)):
        #width is rp-lp and height shd be minimum 
        area=(rp-lp)*min(height[lp],height[rp])
        print(area)
        maxwaterarea=max(maxwaterarea,area)
print("The maxArea is - ",maxwaterarea)

