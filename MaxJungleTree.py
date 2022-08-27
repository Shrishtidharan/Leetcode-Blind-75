
Each cell is either water 'W' or a tree 'T'. Given the information about the field, print the size of the largest forest. The size of a forest is the number of trees in it. See the sample case for clarity

INPUT:

First-line contains the size of the matrix N. The next N lines contain N characters each, either 'W' or 'T'.

OUTPUT:

Print the size of the biggest forest.

Sample input:

5
TTTWW
TWWTT
TWWTT
TWTTT
WWTTT

//

t_cases = int(input())
k1 = 0
k2 = 0
for _ in range(t_cases):
    list1 = (input())
    z = 0
    list2 = []
    for i in range(len(list1)):
        z = list1.count('T')
        if list1[i] == "W":
            break
        elif list1[i] == "T":
            list2.append(list1[i])
            
    k1 = k1 + list2.count('T')
    if z > list2.count('T'):
        k2 = k2 + (z - list2.count('T'))
    else: 
        k2 = k2 + (list2.count('T')- z)
if k1 > k2:
    print(k1)
else: 
    print(k2)
