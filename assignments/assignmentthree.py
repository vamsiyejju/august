#Question-1

print("#program to remove a given  character from string")
input_string = input("Enter a string: ")
char_to_remove = input("Enter the character to remove: ")

new_string = input_string.replace(char_to_remove, '')
print("Modified string:", new_string)

#Question-2:
print("#palindrome")
str=input("enter string")
if str==str[::-1]:
    print(str,"is palindrome")
else:
    print(str,"is not palindrome")
    
#Question-3
print("# program to check given character is vowel or consonant")
ch = input("enter the character : ")
if ch in 'aeiouAEIOU':
    print("character is vowel")
else:
    print("character is consonant")
    

#Question-4
print("#replace string space with given character in Python")
str = input("enter the string: ")
sub_string=input('enter character to replace: ')
new_string=str.replace(' ',sub_string)
print(new_string)

#Question-5
print("count alphabets, digits, and special characters in the string")
string=input('enter a string: ')
alphabets=0
digits=0
special_characters=0
for ch in string:
    if ch.isalpha():
        alphabets+=1
    elif ch.isdigit():
        digits+=1
    else:
        special_characters+=1
print(f'alphabet count = {alphabets}')
print(f'digits count = {digits}')
print(f'special_characters count = {special_characters}')

#Question-6
print("#remove all the blank spaces in a given string")
input_string = input("Enter a string: ")

new_string = input_string.replace(" ", "")
print( new_string)


#Question-7
print("# find sum of integers in the string")
string=input('enter a string: ')
sum=0
for ch in string:
    if ch.isdigit():
        sum+=int(ch)
print(sum)

#Question-8
print("# Remove Repeated Character from String")
string=input('enter a string: ')
new_string=''
for ch in string:
    if ch not in new_string:
        new_string+=ch
print(new_string)


#Question-9
print('# count occurrence of given character in string.')
string=input('enter a string: ')
sub_string=input('enter a character: ')
print(string.count(sub_string))

#Question-10
print("# check string is anagrams or not in Python")
string=input('enter a string1: ')
string2=input('enter a string2: ')
if len(string)==len(string2):
    for ch in string:
        if ch not in string2:
            print('not anagram')
            break
    else:
        print('anagram')
else:
    print('not anagram')





