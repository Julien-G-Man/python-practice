"""
You have a list of dictionaries representing employees.
Write a Python code to print each employee's name and department.
If te department is None, display 'Not Assigned'
"""

employees = [
   {"name": "John", "dept": "Sales", "salary": 5000},
   {"name": "Steve", "dept": "Marketing", "salary": 6000},
   {"name": "Mark", "dept": "Engineering", "salary": 8000},
   {"name": "Bob", "dept": None, "salary": 4500},
]

name = employees[0]["name"]
dept = employees[0]["dept"]
print(f"{name} - {dept}")

n = 0
for emp in employees:
   name = employees[n]["name"]
   dept = employees[n]["dept"] if emp["dept"] else "Not Assigned"
   print(f"{name} - {dept}")
   
   n += 1   
   if n == len(employees):
      print("Both the same") if employees[n-1]["name"] == emp["name"] else print("Not the same")        
      break
      