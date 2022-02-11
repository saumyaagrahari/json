# convert from python object to json string


import json
# a python object (dict)
x={"name":"saumya","age":18,"city":"delhi"}
# convert into json
y=json.dumps(x)
# the result is a json string
print(y)
print(type(y))
print(type(x))