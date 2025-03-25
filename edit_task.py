import requests
import argparse

url = "http://127.0.0.1:5000/tasks"

parser = argparse.ArgumentParser(description="manipulate tasks")
parser.add_argument("-d", "--delete", help="you need to type id of task to delete", required=False)
parser.add_argument("-a", "--add", help="you need to add new tasks' title", required=False)
#parser.add_argument("-e", "--edit", help="you need to type id of task to edit", required=False)
args = parser.parse_args()



            



def delete_task(id):
    try:
        with open(".token", "r") as f:
            token = f.read().strip()
    except FileNotFoundError:
        print(".token file not found")
        exit()

    headers = {"Authorization": f"Bearer {token}"}
    task_id = id

    res = requests.delete(f"{url}/{task_id}", headers=headers)

    if res.status_code == 200:
        print("task deleted")
    else:
        print("error:", res.status_code)
        print("tried to delete taks nr:", args.delete, "but didnt work")

def add_task(add):
    try:
        with open(".token", "r") as f:
            token = f.read().strip()
    except FileNotFoundError:
        print(".token file not found")
        exit()

    headers = {"Authorization": f"Bearer {token}"}
    payload = {"title": add}

    res = requests.post(f"{url}",json = payload, headers=headers)

    if res.status_code in [200, 201]:
        print("task added")
    else:
        print("error:", res.status_code)
        print("tried to add taks :", args.add, "but didnt work")


if args.delete:
    delete_task(args.delete)

if args.add:
    add_task(args.add)




