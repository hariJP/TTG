import random

subjects = ["subj1", "subj2", "subj3", "subj4", "subj5", "subj6", "subj7", "subj8"]
years = ["1st Year", "2nd Year", "3rd Year"]
classes = ["A", "B", "C"]
schedule = [[[[] for _ in range(3)] for _ in range(3)] for _ in range(6)]

for day in range(6):
    print(f"Day {day+1}")
    print("-"*40)
    random.shuffle(classes)
    for class_ in classes:
        print(f"| Class {class_}", end=" ")
        random.shuffle(years)
        for year in years:
            print(f"| {year:10s}", end=" ")
            random.shuffle(subjects)
            for subject in subjects:
                print(f"| {subject:8s}", end=" ")
            print("|")
        print("-"*40)
