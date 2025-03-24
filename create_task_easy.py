import requests
import argparse
url = "http://127.0.0.1:5000"

parser = argparse.ArgumentParser(description="add new task for user")
parser.add_argument("-a", "--add", help="you need to add new tasks' title", required=True)
args = parser.parse_args()


try:
    with open(".token", "r") as f:
        token = f.read().strip()
except FileNotFoundError:
    print(".token file not found")
    exit()

headers = {"Authorization": f"Bearer {token}"}
payload = {"title": args.add}

#"{\"title\": \"kup jajka\"}"
res = requests.post(f"{url}/tasks", json = payload, headers = headers)

