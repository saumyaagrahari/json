# Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?


import json
# j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
# print("Original String:")
# print(j_str)
# print("\nJSON data:")
# print(json.dumps(j_str, sort_keys=True, indent=4))


json_srt = {4:5,6:7,1:3,2:4}
print("original string:")
print("\n",json_srt)
print("\nJSON data:")
print(json.dumps(json_srt,sort_keys=True, indent = 4))