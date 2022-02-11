# import  json
# x={"name":"john",
# "age":30,"married":True,
# "divorced":False,
# "children":("ann","billy"),
# "prts":None,"cars":[{"model":"BNW 230","mpg":27.5},
# {"model":"ford edge","mpg":24.1}]}
# print(json.dumps(x,indent=4,seperator=(".","=")))



import  json
x={"name":"john",
"age":30,"married":True,
"divorced":False,
"children":("ann","billy"),
"prts":None,"cars":[{"model":"BNW 230","mpg":27.5},
{"model":"ford edge","mpg":24.1}]}
print(json.dumps(x,indent=4,sort_keys=True))


# json -- javascript object notation
# in json we store data in form of keys and values. in json keys are in string and values are in any data type.
# key and values are sperated (:)colon. curly bracket{} are represent to json the extension of json file.json

# use of json--
# (1) json jyada tar server se web application or web application se server ke beech data transmit karne ke kaam aata hai.
# (2) web services and APIS json format ka use public data dene me use karta hai.
# (3) aur ye morden programming me bhi use hota hai etc.

# characteristric of JSON --
# (1) json padhane aur likhne me aasan hota hai.
# (2) json language ek independent language hai ye kisi par nirbhar nhi hoti hai.
# (3) ye light weight and text based interchange format hai.

# syntax--
# (1) data hamesha keys and values ki form me hona chahiye.
# (2) data hamesha comma se separated hona chahiye.
# (3) data curly bracets {} me hota hai.
# (4) data jo squre brackets [] me hota hai usse array kahtr hai.
 