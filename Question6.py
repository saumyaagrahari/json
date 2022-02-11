# Python object key unique key value ko access karne ka program likho?


import json
j_file = '{"a":1,"a":2,"a":3,"a":4,"b":1,"b":2}'
print("\n original file:",j_file)
print("\n updated file:")
k=(json.loads(j_file))
print(type(k))

