# Python object ko json string mai convert karne ka program likho?


import json

Student_data={
    "Student_1":{
        "name":"anshuman",
        "roll_no":85,
    },
    "Student_2":{
        "name":"arav",
        "roll_no":124}
}

# print(Student_data)

out_in_file = open("student_data.json","w")
json.dumps(Student_data,out_in_file, indent = 4)
out_in_file.close()
print(Student_data)


import json
x={"bhole nath":5}
Student_details = json.dumps(x)
print(Student_data)

