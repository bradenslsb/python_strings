"""
sentence = 'The quick brown fox jumped over the lazy dog.'

sentence = sentence.replace('quick', 'slow')

print(sentence.replace('quick', 'slow'))
print(sentence)


url = "   https://google.com    "
url2 = "https://google.com"
url3 = "https://google.com"
url4 = "https://google.com"
url5 = "https://google.com"

print(url.strip())
print(url2.strip("https://")) #this will mess with the security.
print(url3.lstrip("https://"))
print(url4.rstrip(".com"))
print(url5.strip("https://" ".com").capitalize())
"""
"""
heading = "Python: An Introduction"

header, _, subheader = heading.partition(": ")

print(header)
print(subheader)

heading2 = "Python: An Introduction, and Python: Advanced"

header2, _, subheader2 = heading2.partition(": ")

print(header2)
print(subheader2)
"""
"""
tags = "python, coding, programming, development"

list_of_tags = tags.split(",") #meaning its going to remove that item and put the rest in a list.

print(list_of_tags)

list_of_tags = tags.split() #puts every element in the list.

print(list_of_tags)
"""
"""
heading = "Python: An Introduction"

heading_list = heading.split(": ")

print(heading_list)

heading2 = "Python: An Introduction, and Python: Advanced"

heading_list_2 = heading2.split(": ")

print(heading_list_2)
"""

api_data = "5"
greeting = "hi there" 
greeting2 = "hithere"

print(api_data.isalpha()) #if its the alphabet
print(greeting.isalpha()) #doesn't count spaces
print(greeting2.isalpha())

print(api_data.isnumeric()) #if its a number
print(greeting.isnumeric())

from functools import reduce

def expontent (num, num_two):
    li = [num] * num_two
    return reduce((lambda x, y: x * y), li)

print(expontent(10, 2))