from analyzer import analyze_text
import json
text=input("enter some text: ")
results=analyze_text(text)
json_result=json.dumps(results,indent=4)

with open("result.json","w") as file:
    file.write(json_result)

print("Analysis saved to result.json")

print(json_result)

with open("result.json",'r') as file:
    data=json.load(file)
print("Saved results:")
print(data)

try:
    with open("result.json",'r') as file:
        data=json.load(file)
    print(type(data))
except FileNotFoundError:
    print("file not found")
except json.JSONDecodeError:
    print("invalid json")
