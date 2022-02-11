# Python object ko json data main convert karne ka program likho?


import json
# # a Python object (dict):
python_obj = {
  "name": "saumya",
  "class":"XIV",
  "age": 18,
  "phone number":8976546789  
}
# print(type(python_obj))
# print
# # convert into JSON:
json_data = json.dumps(python_obj)

# # result is a JSON string:
# print(json_data)

with open("2Details.json", "w") as outfile:
    outfile.write(json_data)










# {
#     "name": "David", 
#     "class": "I", 
#     "age": 6
# }