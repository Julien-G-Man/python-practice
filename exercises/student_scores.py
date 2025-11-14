"""
You have dictionary of students and their scores.
Create a new dictionary containing only students who scored more than 80.

Expected output:
{'Alice': 85, 'Diana': 95}
"""

scores = {"Alice": 85, "Bob": 42, "Charley": 78, "Diana": 95}

print(scores["Alice"])

high_scores = {k: v for k, v in scores.items() if v > 80}
print(high_scores)
 
for key, value in scores.items():
    if value > 80:
        print({key: value})