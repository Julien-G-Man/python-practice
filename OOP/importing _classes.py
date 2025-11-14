from digital_payments import Payment
from Trials.appx import student


class person(student, Payment):
    pass

p1 = person()
print(p1.name)  # Output: Jay

from DataStructures.Dictionaries import my_dict

class person:
    def __init__(self):
        self.data = my_dict

p2 = person()
print(p2.data['hobbies'])  # Output: ['programming', 'reading', 'learning]

