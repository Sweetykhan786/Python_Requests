import json
import os.path
if os.path.exists("courses.json"):
    print("file exists")
    a=open("courses.json","r")
    file=a.read()
    data=json.loads(file)
else:
    print("File does not exists")


