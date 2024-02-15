student = {"name":'Andrew', "age":22, "major":'Business Fellows', "hobbies":['archery','video games','music']}
student['State'] = 'New Hampshire'
student['age'] += 1

for i in student:
    if i == "hobbies":
        print(f'{i}: {student[i][0]}, {student[i][1]}, {student[i][2]}')
    else:
        print(f'{i}: {student[i]}')