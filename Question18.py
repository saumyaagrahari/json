import json
name={
    'name':'saumya',
    'salary':50000,
    'skills':[
        'Raspberry pi',
        'Machine Learning',
        'Web Davelopment'
    ],
    'email':'saumyaagrahari21@navgurkul.org',
    'projects':[
        'Python Data Mining',
        'Python Data Science'
    ]
}

a=open('devloper.json','w')
json.dump(name,a,indent=4,sort_keys=True)
a.close()

a=open('devloper.json','r')
s= a.read()
print(s)
print(type(s))
a.close()

a=open('devloper.json','r')
s=json.load(a)
print(s)
print(type(s))
a.close()

# b=json.dumps(name)
# print(b)
# print(type(b))
# print(type(name))

# b=json.loads(name)
# print(b)
# print(type(b))
# print(type(name))







