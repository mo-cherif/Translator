from googletrans import Translator
import json
import time
import random
translator = Translator()

newjson = {}

i = 0
f = open('a0.json')
datas = json.load(f)

for k,v in datas.items():
    time.sleep(random.random()+1)
    result = translator.translate(v, dest='arabic')
    i+=1
    print(i)
    newjson[k] = result.text

with open("r0.json", "a", encoding='utf-8') as outfile:
    json.dump(newjson, outfile,indent=2,ensure_ascii=False)

# Closing file
print(json.dumps(newjson, ensure_ascii=False))
f.close()



