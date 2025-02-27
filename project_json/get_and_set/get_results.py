# Import Modules ===============>
import json
import os

file_path = os.path.join(os.path.dirname(__file__), "../data/data.json")

# Get Results func. ===============>
def get_result(name, result):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except:
        data = []

    new_result = {
        "name": name,
        "played": 0,
        "best_score": result
    }

    data.append(new_result)

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)