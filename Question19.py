import json
a={
    "name":"sanjna",
    "age":21
}
with open("name.json","w")as k:
    print(json.dumps(a,k,indent=4))


  