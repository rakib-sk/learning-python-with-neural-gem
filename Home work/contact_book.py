import json
import os

print("If you want to stop, type: exit")


all_data = []

while True:
    name = input("Enter name: ")
    
    if name == "exit":
        break

    phone = input("Enter phone: ")

    all_data.append({"name": name, "phone": phone})



if not os.path.exists("info.json"):
    with open("info.json", "w") as f:
        json.dump([], f)


with open("info.json", "r") as f:
    old_data = json.load(f)


old_data.extend(all_data)


with open("info.json", "w") as f:
    json.dump(old_data, f, indent=4)

print("Data saved successfully!")