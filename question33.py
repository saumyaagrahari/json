# from array import array
# import json
# import numbers
# import string
# print(json.dumps({"name":"john","age":30}))

# print(json.dumps(["apple","banana"]))

# print(json.dumps(("apple","banana")))

# print(json.dumps("hello"))

# print(json.dumps(42))

# print(json.dumps(31.76))

# print(json.dumps(True))

# print(json.dumps(False))

# print(json.dumps(None))

# # print(type(json))

# dict = object
# list = array
# tuple = array
# str = string
# int = numbers
# float = numbers
# True = true
# False = false
# None = none

import json
x={"name":"john","age":30,"married":True,"divorced":False,"children":("ann","billy"),"prts":None,"cars":[{"model":"BNW 230","mpg":27.5},
{"model":"ford edge","mpg":24.1}]}
print(type(x))
y=(json.dumps(x))
# print(json.dumps(x,indent=4))
print(json.dumps(x))
print(type(y))