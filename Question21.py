######## [] 	A set of characters

import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[m-z]", txt)
print(x)


######## \ 	Signals a special sequence (can also be used to escape special characters)

import re

txt = "That will 5678 be  dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)


# a=[1,1,0,1,1,1,0,1]
# i=0
# b=[]
# d=[]
# c=0
# while i<len(a):
#     if a[i]==0:
#         c=c+1
#         b.append(a[i])
#     else:
#         d.append(a[i])
#     i=i+1
# print(c)
# print(b)
# print(d)
