#membership checking
#ex-1
name="my name is yejju"
input_name=input()

if input_name in name:
    print(" YES : Word present in name ")
else:
    print("NO: word not present in name")

print()
#ex-2

word="my name is yejju"
input_word=input()

result=input_word in word

print(result)


#ex-3


names=["jr ntr","mohan lal","rajanikanth","shiva raj kumar"]
input_name=input()

for input_name in names:
    if input_name in names:
        print(input_name,"is present in names")
    else:
        print(input_name,"is not present in names")


#strip method


#example:1

name="     jr ntr is my favourite Hero  "
name1=name.strip()
length=len(name1)
print(length)

#example:2

text = "     mango    "
x = text.strip()
print("out of all fruits", x, "is my favorite")

#example:3

text_word = ",,,,,ggggoooo.....cakes....pastryyy"
x = text_word.strip(",.ggoo")
print(x)




#comparing two strings

#example:1

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
player_names = "Sachin Tendulkar, Virat Kohli, Rohit Sharma, MS Dhoni, Sachin Tendulkar"


sachin_index = player_names.rindex("Sachin Tendulkar")
print("Last 'Sachin Tendulkar' index:", sachin_index)


rohit_index = player_names.rindex("Rohit Sharma")
print("Last 'Rohit Sharma' index:", rohit_index)

#indexmethod

player_names = "Sachin Tendulkar, Virat Kohli, Rohit Sharma, MS Dhoni, Sachin Tendulkar"


sachin_index = player_names.index("Sachin Tendulkar")
print("'Sachin Tendulkar' index:", sachin_index)


rohit_index = player_names.index("Rohit Sharma")
print("'Rohit Sharma' index:", rohit_index)

#find method
vegetables= "tomato is very costly vegetable"
x = vegetables.find("vegetable")
print(x)

# rfind method

vegetables= "tomato is very costly vegetable"
x = vegetables.rfind("vegetable",15,24)
print(x)

#replacing the string

original_string = "I love mangoes. Mangoes are delicious fruits."


new_string = original_string.replace("mangoes", "oranges")

print("Original string:", original_string)
print("New string:", new_string)

#split method


flower_string = "Rose Lily Tulip Daisy Sunflower"
flower_list = flower_string.split()
print("List of flowers:", flower_list)

#join operator
laptop_names = ['Dell', 'HP', 'Lenovo', 'Asus', 'Apple']


laptop_string = ", ".join(laptop_names)
print("Laptop string:", laptop_string)

