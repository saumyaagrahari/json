# Jsmoduleon string ko check karo ki bo complex object contain karti hai ya nahi?

import json
a = {"name":5,"class":20,"age":7}
b = json.dumps(a)
print(b)
print(type(b))
print(type(a))