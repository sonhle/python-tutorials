f = open('json', 'w')

import json
x = [1, 'simple', 'list']
#print(json.dumps(x))
json.dump(x, f)
f.close()

with open('json', 'r') as out:
    ret = json.load(out)
    print(ret)