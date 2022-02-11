import json
name='''{
    "name":"saumya",
    "salary":50000,
    "skills":[
        "Raspberry pi",
        "Machine Learning",
        "Web Davelopment"
    ],
    "email":"saumyaagrahari21@navgurkul.org",
    "projects":[
        "Python Data Mining",
        "Python Data Science"
    ]
}'''

b=json.loads(name)
print(b)
print(type(b))
print(type(name))
