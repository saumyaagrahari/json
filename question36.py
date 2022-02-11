# dump()--
# dump() method python object ko json file me store karne ke liye use hota hai.
# dump() method json file pr hi kaam karta  hai, aur python objects ko ek argument ki tarah stor karta hai.
# example-- python object (dictionary) ko ham json file me dump karte hai.

import json

from simplejson import load 
dict={"emp1":{'name':'lisa',
"disignation":"programmer",
"age":"34","salary":"54000"},
"emp2":{"name":"list","disignation":"trainee","age":"24","salary":"40000"}}
out_file=open("myfile.json","w")
json.dump(dict,out_file,indent=6)
out_file.close()

# load()--read
# the json.load() is used to read the json document from file.

# dump()--
# the json dump() method used to write python object as json formatted data in to file.

# loads()--
# the json loads() is used to convert the json string document in to python dictionary.

# dumps()--
# the json.dumps() method encodes any python into json formatted string.

# diffirence json for fictionary.
# jaon file are string format.
# dictionary are object format.
# in json we store data in file.
# in dictionary we get output on tarminal.

# http:// json path finder.com/

