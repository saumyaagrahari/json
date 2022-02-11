


import json
dictionary ={
"id": "04",
"name": "sunil",
"department": "HR"
}
json_object = json.dumps(dictionary, indent = 4)
print(json_object)


# Python program to write JSON
# to a file


import json
dictionary ={
	"name" : "sathiyajith",
	"rollno" : 56,
	"cgpa" : 8.6,
	"phonenumber" : "9976770500"
}
with open("sample.json", "w") as outfile:
	json.dump(dictionary, outfile)

# Python program to read
# json file


