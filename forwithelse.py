#break

#program to display students marks from record

student_name='Prabhu'
marks = {'James':90, 'Jules':55, 'Arthur': 77
, 'Soyuj':100}

for student in marks:
    if student == student_name:
        print(marks[student])
        break

else:
    print('No entry with that name found')

#list[index]
#dict[key]