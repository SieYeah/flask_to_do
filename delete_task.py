import requests
import argparse


url = "http://127.0.0.1:5000/tasks"

parser = argparse.ArgumentParser(description="add new task for user")
parser.add_argument("-d", "--delete", help="you need to type id of task to delete", required=True)
args = parser.parse_args()

try:
    with open(".token", "r") as f:
        token = f.read().strip()
except FileNotFoundError:
    print(".token file not found")
    exit()

headers = {"Authorization": f"Bearer {token}"}
task_id = args.delete

res = requests.delete(f"{url}/{task_id}", headers=headers)

if res.status_code == 200:
    print("task deleted")
else:
    print("error:", res.status_code)
    print("tried to delete taks nr:", args.delete, "but didnt work")
