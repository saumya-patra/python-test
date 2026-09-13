import requests
people = requests.get("http://api.open-notify.org/astros.json")
json_data = people.json()

print(json_data)
print("The people currently in space are: ")
for person in json_data['people']:
    print(person['name'])