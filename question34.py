import  json
x={"name":"john",
"age":30,"married":True,
"divorced":False,
"children":("ann","billy"),
"prts":None,"cars":[{"model":"BNW 230","mpg":27.5},
{"model":"ford edge","mpg":24.1}]}
print(json.dumps(x,indent=4))
# print(json.dumps(x))
# print(type(x))