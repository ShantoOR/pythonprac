### Python itertools module is a collection of tools
#for handling iterators. Simply put, iterators are data
#types that can be used in a for loop. The most common 
#iterator in Python is the list.


from itertools import permutations

perm=permutations(['A', 'B', 'X', 'L'],3)
##print(list(perm), len(list(perm)))


##product (curtasian prod)
## combinations

##accumulate[array additition accumulation]
        #func=operator.mul   #func=max







from itertools import groupby   ##specific key(your wish) er respect ey partitioning 




L1 = [("a", 1), ("b", 2), ("a", 3), ("b", 4),("c",3), ("b",2), ("a",5)]
L=[1,2,3,4,5,6,7,8,9,10,11,2,126,14,15,13,16]


def func(x):         ##func = lambda x: x[0]
    return (x%3)==0 

for  key, group in groupby(L, func):
	print(key, ":", list(group))




def func(x):         ##func = lambda x: x[0]
    return x[0]

for  key, group in groupby(sorted(L1), func):
	print(key, ":", list(group))
       
L4=sorted(L1) 

print(L4)      

string = 'mkamakamskamaksmskmskssmakmsksms'

def func(x):
    return x

for key, group in groupby(sorted(string), func):
    print(key, ":", list(group))


'''
anagrams =['angel','below','glean','bored','robed','study','dusty','cat','act','inch','chin','taste','state','elbow']
grouped_anagrams = [list(group) for key, group in groupby(sorted(anagrams, key=sorted),sorted)]
print(grouped_anagrams)
'''


students = [
    {
        'name':'Teri Howard',
        'state':'CA'
    },
    {
        'name':'Stephen Reyes',
        'state':'CA'
    },
    {
        'name':'Thalia Franklin',
        'state':'CA'
    },
    {
        'name':'Yvonne Slater',
        'state':'Tx'
    },
    {
        'name':'Rolf Wilcher',
        'state':'Tx'
    },
    {
        'name':'Teri Dinwiddie',
        'state':'MS'
    },
    {
        'name':'Fred Greer',
        'state':'AL'
    },
    {
        'name':'Lane Snee',
        'state':'AL'
    }
]

def get_state(stu_ite):
    return stu_ite['state']

 
for state, students in groupby(students, get_state):  #### so ekhane ashole groupby(stu, get_st) eitai filtering kore feltese pura student list theke
    print(f"State: {state}")
    print("Students: ", end="")
    i=1
    for student in students:   ## studentder list students dic thekei paoa jabe ar state-wise filtering agei hoye gese 
        print(i,". ", student['name'],sep="", end="  ")
        i=i+1
        
    print()




person=[]

dictn= {'name':'abc', 'id':'23134', 'cap':74,  'bonus': True}

person.append(dictn)
person.append({'name':'ggg', 'id':'24270', 'cap':29,  'bonus': True})
n="new namm" 
id='44141'
person.append({'name':n, 'id':id, 'cap':55,  'bonus': False})

''''
for i in range(2):
    n=input('name:')
    id=input('id:')
    cap=int(input('cap:'))
    bon=input('bonus:')
    if bon=='True':
        bonus=True
    else: bonus=False    
    person.append({'name':n, 'id':id, 'cap':cap,  'bonus': bonus})
'''

def get_bonuspart(x):
    return x['bonus'] 
   
for key, group in groupby(person, key=get_bonuspart):
    print(key, end=": ")
    L=list(group)
    k=1
    