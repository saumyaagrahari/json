# Text file data ko json file data mai convert karo,jaise ki neeche diya hai?

# python program to convert text file to JSON


Text = {"Name":"Abhishek","Designation":"CEO of navgurukul","Gender":"male","Age":29}
import json
out_file = open ("new.json","w")
json.dump(Text,out_file,indent = 4,sort_keys = True)
out_file.close()


# import json
a = open("new.json","r")
Text=json.load(a)
print(Text)
print(type(Text))
a.close()              


# a=open('devloper.json','r')
# s=json.load(a)
# print(s)
# print(type(s))
# a.close()













