import json

username = input("What's your name? ")
filename = "chapter10\\username.json"
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}")