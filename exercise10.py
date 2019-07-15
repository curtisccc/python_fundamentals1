students = {
    'cohort1': 34,
    'cohort2': 42,
    'cohort3': 22,
}

def display():
    for key, value in students.items():
        print(f"{key}: {value:.0f} students")
display()

students["cohort4"] = 43
print(students)

print(students.keys())

def expanded(): 
    for co, num in students.items():
        size = num * 1.05
        print(int(size))
expanded()

del students["cohort2"]
print(students)

total = 0
for cohort, num in students.items():
    total += num
print(total)