def add(a:int,b:int)->int:
    c=a+b
    return c

a=24
b=63
print(add(a,b))









def prime(n): 
    if n in [2,3]: 
        return True 
    if (n==1) | (n%2==0): 
        return False
    r=3 
    while r*r <= n:
        if n%r==0: 
            return False 
        r+=2 
    return True 
                           
for i in range(5):
    print(i, prime(i))



    


            ####pass by reference
def myFun(x):   
  temp=x[0]
  x[0] = x[1]
  x[1]=temp


# Driver Code (Note that lst is modified
# after function call.
x=10
y=14

lst=[]
lst.append(x)
lst.append(y)
print(lst)
myFun(lst)
print(lst)








### list comrehension 
#Syntax: newList = [ expression(element) for element in oldList if condition ] 

List = [i**2 for i in range(11) if i % 2 == 0]
print(List)



List = []
for character in 'Geeks 4 Geeks!':
	List.append(character)
print(List)




matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)
print()








# Transpose matrix
twoDMatrix = [[10, 20, 30],
			  [40, 50, 60],
			  [70, 80, 90]]

# Generate transpose
trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix[0]))]

#print(trans)

for i in trans:
    print(i)







#### LAMBDA

  ##lambda x=arg  right-side op is return value 
cube = lambda y :  y**3
print(cube(3))




## inside another function
def multiplier(n):
    f= lambda x:x**n    ## f arekta function hishebe kaj korbe jar automatic arg holo x and return korbe x^n(n just ekta number whereas x is variable for the following function)
    return f

product= multiplier(2)        ##x=product(6)(2)  works damn
ans= product(6)
print(ans)
 
 
 

s1="fasfa"
s2="fasaf"

a=sorted(s1)
b=sorted(s2)

if a==b:
    print("YESSS!", a)
else: print("NO")    




L=[15,3,11,7,25,40]
print(sorted(L, key=lambda x: x%7))





id_n_performance=[]


id_n_performance.append(dict(id="NE0123", per=61))
id_n_performance.append(dict(id="NE8972", per=24))
id_n_performance.append(dict(id="NG4233", per=54))
id_n_performance.append(dict(id="NE4632", per=20))


print(sorted(id_n_performance, key=lambda x: x["id"]))


for i in id_n_performance:
    for j in i:
        print(j, ": ", i[j], end="   ", sep="")
    print("")       







people = [
    ('John', 25),
    ('Alice', 18),
    ('Bob', 30)
]

sorted_ppl=sorted(people, key=lambda x: x[1])

for i in sorted_ppl:
    print(i)    








a  = [1, 2, 3, 4, 5, 6]
b = list(map(lambda x: x * 2 , a))

# However, try to prefer list comprehension
# Use map if you have an already defined function
c = [x*2 for x in a]
print(b)
print(c)




### The reduce(fun,seq) function is used to apply a particular function passed
# in its argument to all of the list elements mentioned in the sequence passed along

# # # repeatedly applies the func to the elements and returns a single value.
# func takes 2 arguments.


# importing functools for reduce()
from functools import reduce

# initializing list
lis = [1, 3, 5, 6, 2]

a = [2, 3, 4]
product_a = reduce(lambda x, y: x*y, a)
print(product_a)
sum_a = reduce(lambda x, y: x+y, a)
print(sum_a)

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(reduce(lambda a, b: a if a > b else b, lis))


def abc(x,y):
    return x**y

# # # # #  ()  


print(reduce(abc, a))









