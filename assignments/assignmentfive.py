#Question - 1
print("#Write a Python script to add a key to a dictionary")
d = {'0': 10, '1': 20}
d['2'] = 30
print(d)

#Question - 2
print("#Python script to check weather a given key already exists in dictionaries")
dic = {"Hero":"NtrJr", "Heroine":"KajalAgarwal"}
a = "Hero"
if a in dic.keys():
    print("Present")
else: 
    print("not present")

#Question -3 
print("#Python program to iterate over dictionaries using for loops")
dic = {"india":"msd", "england":"kevin pietersen","srilanka":"dasun shanka"}  
for key,value in dic.items():
    print(key,value)

#Question -4 
print("#Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.Sample Dictionary")
d=dict()
for x in range(1,16):
    d[x]=x**2
print(d) 

#Question -5 
print("#Python program to create a dictionary from a string")
str = "marolix technology"
char = {}
for i in str:
    if i in char:
        char[i] += 1
    else:
        char[i] = 1
print(char)

#Question - 6
print(" #Python program to sum all the items in a dictionary")
dict_a={
    "a":1000,
    "b":2000,
    "c":3000
}
print(sum(dict_a.values()))
#Question - 7
print("#Python program to combine two dictionary by adding values for common keys")
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3=dict(d1)
d3.update(d2)
for i,j in d1.items():
    for x,y in d2.items():
        if i==x:
            d3[i]=(j+y)
print(d3)

#Question-8
print("#Python program to access dictionary key's element by index")
Dictionary = {'Physics': 99, 'Maths': 90, 'Chemistry': 96}
print(list(Dictionary)[0])
print(list(Dictionary)[1])
print(list(Dictionary)[2])

#Question - 9
print("#Python program to remove a key from a dictionary")
dictionary={
    "msd":100,
    "virat":85,
    "rashid":95
}
del dictionary["msd"]
print(dictionary)

#Question -10
print("# Python script to merge two Python dictionaries")
dict_1 = {"vamsi":101,"krishna":102}
dict_2 = {"lakshmi":2001,"venkat":2002}
res = {**dict_1,**dict_2}
print(res)
