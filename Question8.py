# Tumhare pass four employes ki details hai list mai:-


# ["neelam","programer",24,2400]
# ["komal","trainer",24,20000]
# ["anuradha","HR",25,40000]
# ["Abhishek","manager",29,63000]

import json

list = {
        "emp1":
        {"name":"nilam",
        "Designation":"programmer",
        "Age":34,
        "salary":24000,
        },

        "emp2":
        {"name":"komal",
        "Designation":"trainee",
        "Age":24,
        "salary":20000,
        },

        "emp3":
        {"name":"anuradha",
        "Designation":"HR",
        "Age":25,
        "salary":40000
        },

        "emp4":
        {"name":"Abhishek",
        "Designation":"Manager",
        "Age":29,
        "salary":60000
        }
    }
print(list)
new_list=open("employee.json","w")
json.dump(list,new_list,indent=4,sort_keys=False)
new_list.close()

print(type(list))
print(type(new_list))
