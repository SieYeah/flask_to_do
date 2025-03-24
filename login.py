import requests

url = "http://127.0.0.1:5000/login"

payload = {
    "email": "three@three.com",
    "password" : "szakalakaskurwysynu"
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    token = response.json()["access_token"]
    with open(".token", "w") as f:
        f.write(token)
else:
    print("login failed lol", response.status_code)
    print(response.json())
    