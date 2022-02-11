# python object to json data

import json
a={"name":"davil","class":"I","age":6}
with open("my_file.json","w") as s:
    json.dump(a,s,indent=4)


a={"name":"davil","class":"I","age":6}
print(json)
print(json.dumps(a))

# pahle ham dum ki huii file load bhi kr sakte hai.

with open ("my_file.json","r") as file:
    data=json.load(file)
    print(data)


import json
a = '{"name":"ram","class":"IV","age":9,}'
print(json.loads(a))

        