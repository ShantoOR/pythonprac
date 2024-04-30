from collections import Counter

### The collection Module in Python provides different 
# types of containers. A Container is an object that 
# is used to store different objects and provide a way
# to access the contained objects and iterate over them



###  COUNTERRRRR : A counter is a container that stores elements as dictionary keys,
                    # and their counts are stored as dictionary values.

a="faf agfgerv argheawrhyearg 582346 %&*& ']\; vrgyerhujeryfvbgfdhnjasdfvbiughewfbasfdkpoeirweiotvldbnjkghsdamvbnxzcmqwopriweoity"
cnt=Counter(a)
print(cnt)

# print(cnt.items())
# print(cnt.keys())
# print(cnt.values())

print(cnt.most_common(3))
print(list(cnt.values()))



###NAMEDTUPLEs are easy to create, lightweight OBJECT(derived 
# from class) TYPES. They assign meaning to each position in a tuple and 
# allow for more readable, self-documenting code. They can be used 
# wherever REGULAR DICTIONARY or TUPLES are used, and they add the ability 
# to access fields by NAME INSTEAD OF POSITION INDEX. 
# Like dictionaries, they contain keys that are hashed to
# a particular value. 


from collections import namedtuple

Car= namedtuple('Car', 'speed, num_plate, x, y, fuel')
c1= Car(20,'ec35356',-45,12,100)
print(c1._fields)  

print(c1)
print(c1.speed/2)
print(c1[3])
print(c1.y)


Student= namedtuple('Student', 'name, age , level, house')

s1= Student('nan', 21, 'XI', 'Lanns')
print(s1)
s2List=['ryan', 12,'3','rocket']
s2=Student._make(s2List)  ##make any iterable er jonnei kaj kore
print(s2)

dic = {'name': "Nikhil", 'level': '1391997', 'house':'sasa', 'age': 19, }
print(Student(**dic))    ## from dictionary to namedtuple

print("")


##ORDEREDDICT less imp since python 3.7



## DEFAULTDICTIONARY: The functionality of both dictionaries
# and defaultdict are almost same except for the fact that 
# defaultdict never raises a KeyError.It provides a default 
# value for the key that does not exists.


from collections import defaultdict

def def_value():             ## default_factory: A function returning the default
                              #value for the dictionary defined. 
    return "Not Present"  

dict= defaultdict(def_value)

dict["a"] =1
dict["b"] =2
dict["c"] =2


##print(dict.items())
##print(dict.keys())
print(dict["b"])
print(dict["d"])
print("")

d=defaultdict(int)
d['yellow']=3
d['green']=2
d['orange']=6

print(d['yellow'])
print(d['blue'])


d= defaultdict(list)

for i in range(5):
    d[i].append(i+i)
    d[i].append(i*i)

print(d)
print(d[4])
print(d[7])

print("")


dl=defaultdict(list)
dlist=[('yellow',1), ('red',3), ('green',10), ('blue',7)]

for k,v  in dlist:         ### check k,v, single k/v all combinations- fun plus insights 
    dl[k].append(v)

print(dl.items())
print(dl['red'])
