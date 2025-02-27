# Import Modules ===============>
import json
import os

file_path = os.path.join(os.path.dirname(__file__), "../data/data.json")

# Set Results func. ===============>
def set_result(name, result):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except:
        data = []

    new_result = {
        "name": name.lower(),
        "played": 1,
        "best_score": result
    }

    old_user = False
    for user in data:
        if user["name"] == name.lower():
            old_user = True
            user["played"] += 1
            if user["best_score"] < result:
                user["best_score"] = result
    
    if not old_user:
        data.append(new_result)


    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)