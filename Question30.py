import json

with open('path_to_file/person.json') as f:
  data = json.load(f)

print(data)


import json

#reading
with open(f, 'r') as f:
	data = json.load(f)

#writing
with open(f, 'w') as f:
	json.dump(data, f) #use indent to make easyer to read eg. indent = 4


#there are many modes you can open files in. r means read.
file = open('C:\Users\yourname\files\file.txt','r')
text = file.read()

#you can write a string to it, too!
file = open('C:\Users\yourname\files\file.txt','w')
file.write('This is a typical string')

#don't forget to close it afterwards!
file.close()


import json

with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
