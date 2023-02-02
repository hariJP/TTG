import random
from collections import Counter

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
    # Create a list to keep track of scheduled subjects
    scheduled_subjects = []
    for i in range(num_days):
        # Shuffle the subject list for each day
        random.shuffle(subjects)
        # Get the subjects that are not scheduled yet
        unscheduled_subjects = list(set(subjects) - set(scheduled_subjects))
        # If we have less than 8 subjects unscheduled, add the remaining subjects
        if len(unscheduled_subjects) < 8:
            unscheduled_subjects += list(set(subjects) - set(unscheduled_subjects))
        # Schedule the first 8 subjects
        timetable[cls][i] = unscheduled_subjects[:8]
        random.shuffle(timetable[cls][i]) # shuffle the order of the subjects for each day
        # Add the scheduled subjects to the list
        scheduled_subjects += timetable[cls][i]
    # check the count of each subject if it is equal in a week
    print(cls)
    print(Counter(scheduled_subjects))
# Print the timetable in a typographic manner
for cls in classes:
    print(f"\nTimetable for {cls}:")
    for i in range(num_days):
        print(f"Day {i+1}: {timetable[cls][i]}")
