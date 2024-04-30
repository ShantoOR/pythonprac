
mango=9

fruit= ["banana", 7==6, mango]  #lists allow different data type # i mean lists allow variables directly
print(fruit)

alist= ["snort", "zacob", "xenon","carb","victim", "blaming","mob","hiararchy","fault"]
alist[-1]="new"
print(alist[-1])
v="elements"
alist.insert(4,"in X")  #pop/rmv/clear/sort/ed...
print(alist)
print("lenght:",len(alist),v, 3==3)

# list copying: copy() vs =

for i in alist:
    print(i)

print("check a test: ")
if "s" in alist:
    print(True)
else: print(False)    
print()    
    
    
dlist=[('yellow',1), ('red',3), ('green',10), ('blue',7)]
print(dlist[2])




matrix = []
for i in range(3):

	# Append an empty sublist inside the list
	matrix.append([])
    
	for j in range(5):
		matrix[i].append(j)
  


print(matrix)






'''
ss="GACTTACGTACT"

L=[]
i=0
j=0
k=0
for i in range(int(len(ss)/3)):
    #print(ss[i+j:i+j+3])
    L.append(ss[i+j:i+j+3])
    j=j+2
    
   
print(L)   
    
    
#a=L[2]
#b=a[1:3]
#print(b)

L2=[]
for i in range(len(L)):
    z=L[i]
    x=z[0:2]
    c=z[1:3]
    #print(z)
    #print(x)
    #print(c)
    L2.append(x)
    L2.append(c)
    
#print(L2) 
   

from collections import OrderedDict

L3=list(OrderedDict.fromkeys(L2))
print(L3)

j=0

for i in range(len(L3)):
    print(L3[j], "->", L3[j+1])
    j=j+1
    if j==(len(L3)-1):
        break
    
    
'''

sr= "abcdefghijklmnopqrstuvwxyz!"
##print(len(sr))
j=0 
L=[]
for  i in range(int(len(sr)/3)):
    a=sr[j:j+3]
   ## print(a)
    L.append(a)
    j=j+3
    
##print(L)    