#membership check
#ex-1
print('#Membership operator using in and not in,#enter name')
name="my name is yejju"
input_name=input()

if input_name in name:
    print(" YES : Word present in name ")
else:
    print("NO: word not present in name")

print()
#ex-2
print("#enter the name")
word="my name is yejju"
input_word=input()

result=input_word in word

print(result)


#ex-3

print("#enter the name of an actor")
names=["jr ntr","mohan lal","rajanikanth","shiva raj kumar"]
input_name=input()

for input_name in names:
    if input_name in names:
        print(input_name,"is present in names")
    else:
        print(input_name,"is not present in names")


#strip method


#example:1

print(' #strip')
name="     jr ntr is my favourite Hero  "
name1=name.strip()
length=len(name1)
print(length)

#example:2

text = "     mango    "
x = text.strip()
print("out of all fruits", x, "is my favorite")






#comparing two strings

#example:1
print("#string comparision # entrer the vegetable name ")
vegetable=input()

if vegetable=="tomoato":
    print("Yes it is tomato")
elif vegetable=="potato":
    print("yes it is potato")
elif vegetable=="carrot":
    print("yes it is carrot")
elif vegetable=="ladiesfinger":
    print("yes it is ladiesfinger")
else:
    print("no vegetable matched")

#example:2

string_x = 'Hi & Gm'
string_y = 'Hi & Gm'


if string_x == string_y:
 
    print ("Same Strings")
 
else:
 
    print ("Different Strings")


#rindex method
print("#finding a sub string by suing rindex method","#enter the name of a player")
player_names = "Sachin Tendulkar, Virat Kohli, Rohit Sharma, MS Dhoni, Sachin Tendulkar"


sachin_index = player_names.rindex("Sachin Tendulkar")
print("Last 'Sachin Tendulkar' index:", sachin_index)


rohit_index = player_names.rindex("Rohit Sharma")
print("Last 'Rohit Sharma' index:", rohit_index)

#indexmethod
print("#finding a sub string by using index method","#enter name ")
player_names = "Sachin Tendulkar, Virat Kohli, Rohit Sharma, MS Dhoni, Sachin Tendulkar"


sachin_index = player_names.index("Sachin Tendulkar")
print("'Sachin Tendulkar' index:", sachin_index)


rohit_index = player_names.index("Rohit Sharma")
print("'Rohit Sharma' index:", rohit_index)

#find method
print("#find method")
vegetables= "tomato is very costly vegetable"
x = vegetables.find("vegetable")
print(x)

# rfind method
print("#rfind method")
vegetables= "tomato is very costly vegetable"
x = vegetables.rfind("vegetable",15,24)
print(x)

#replacing the string
print("replacing the string method")

original_string = "I love mangoes. Mangoes are delicious fruits."


new_string = original_string.replace("mangoes", "oranges")

print("Original string:", original_string)
print("New string:", new_string)

#split method

print("#split method ")
flower_string = "Rose Lily Tulip Daisy Sunflower"
flower_list = flower_string.split()
print("List of flowers:", flower_list)

#join operator
print("#joinoperator")
laptop_names = ['Dell', 'HP', 'Lenovo', 'Asus', 'Apple']


laptop_string = ", ".join(laptop_names)
print("Laptop string:", laptop_string)

