import json
x='{"name":"saumya","age":30,"city":"delhi"}'
y=json.loads()
print(y)


# convert to json string to python dictionary


import json
x='{"name":"saumya","age":30,"city":"delhi"}'
y=json.loads(x)
print(y["age"])

