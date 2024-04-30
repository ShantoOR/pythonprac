import re

string1 = "by what right does the wolf judge the lion!"
print(string1)

## : : slicing/reverse/every nth item

new_st= string1 + " do u have anything else to say?"

print(new_st)

words= new_st.split()
print(words)

for i in words:
    print(i)

##list to string and string to list conversion

print(new_st.startswith("by"))    

a_str= "baba mama mafas kh. sfds dsa.asdd .asda"
print(a_str.split("."))   ## senntence split nice nice
 
 ##.format()
 
 ## check python enumerate
 #find()// enumerate  ## list comprehension
 
 
str_2= "you learning python, $# or@ python*^ learning you"
print("og string: " + str_2)
                                   ##  In the cases which contain all the special characters and
                                   # punctuation marks, the conventional method of finding words in string
                                   # using split can fail and hence requires regular expressions to perform this task.
regs= re.findall(r'\w+', str_2)
print("better one:" + str(regs))


##Using NLP Libraries



name = "Eric"
age = 25
a = f"Hello, {name}. You are {age}."
print(a)
pi = 3.14159
a = f"Pi is {pi:.3f}"
print(a)
# f-Strings are evaluated at runtime, which allows expressions
a = f"The value is {2*60}"
print(a)


 
 
