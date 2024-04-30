#collection. db er moto kaaj kore. key-pair value MAPPING

dic_1 = {"Name":"shan", "Age": 42, "City":"dhala"}
#print(dic_1)

dic_1 = dict(Name="sakib", Age=61, City="new Y")
print(dic_1)

print("Age of first person is:" ,dic_1["Age"])

#update/check/delete
i=1
for k in dic_1.keys():
    print(i, k)
    i=i+1
  
print("")
  
i=1
for k in dic_1.values():
    print(i, k)
    i=i+1    

print("")

j=1
for k in dic_1: 
    print(j, '. ', k, ": " , dic_1[k], sep="")  ## d1.keys()  n d1.values() builtin funct
    j=j+1

    

#copy a dict **
#merged/nested **

    
    
        



