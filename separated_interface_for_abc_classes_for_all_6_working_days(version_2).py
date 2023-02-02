import random

# List of subjects
subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5", "Subject 6", "Subject 7", "Subject 8"]

# List of classes
classes = ["Class A", "Class B", "Class C"]

# Number of working days
num_days = 6

# Create a dictionary to store the timetable
timetable = {}

# Initialize the timetable with empty lists
for cls in classes:
    timetable[cls] = []
    for i in range(num_days):
        timetable[cls].append([])

# Schedule the subjects for each class
for cls in classes:
    for i in range(num_days):
        # Shuffle the subject list for each day
        random.shuffle(subjects)
        timetable[cls][i] = subjects.copy()

# Print the timetable in a typographic manner
for cls in classes:
    print(f"\nTimetable for {cls}:")
    for i in range(num_days):
        print(f"Day {i+1}: {timetable[cls][i]}")
