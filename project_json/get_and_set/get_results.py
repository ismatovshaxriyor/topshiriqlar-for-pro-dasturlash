# Import Modules ===============>
import json
import os
from prettytable import PrettyTable


file_path = os.path.join(os.path.dirname(__file__), "../data/data.json")

# Get Results func. ================>
def section2():
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        table = PrettyTable(["Name", "Played", "Best_score"])
        for user in data:
            table.add_row([user["name"], user["played"], user["best_score"]])
        
        print(table)
    except:
        print("Natijalar yo'q")

