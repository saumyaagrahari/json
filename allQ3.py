print("Started Reading JSON file")

print("Decoded JSON Data From File")
    
print("Done reading json file")


import json 
     
# Data to be written 
dictionary ={ 
  "id": "04", 
  "name": "sunil", 
  "department": "HR"
} 
     
# Serializing json  
json_object = json.dumps(dictionary, indent = 4) 
print(json_object)



