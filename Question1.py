#  Json data ko python object main convert karne ka program likho?.

import json
json_obj = '{"Name":"Arav","Class":"I","Age":6}'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(python_obj)
print("\nName:",python_obj["Name"])
print("Class:",python_obj["Class"])
print("Age:",python_obj["Age"])
