#  Python program to convert Python to JSON 


import json 

a={'id':4,'name':'saumya','department':'HR'}
b=json.dumps(a,indent=4)
print(b)
print(type(b))
print(type(a))