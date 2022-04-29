import json
import requests
url="https://api.merakilearn.org/courses"
a=requests.get(url)
abc=a.json()
print(abc)
with open("courses.json","w") as f:
    json.dump(abc,f,indent=4) 
with open("courses.json","r") as f1:
    read=json.load(f1)


# from re import A


