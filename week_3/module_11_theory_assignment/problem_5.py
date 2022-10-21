students_count = int(input("Enter students count : "))

students_dict = {}

for count in range(1, students_count+1) : 
    student_name = input(f"Enter the student name : ")
    student_mark = int(input("Enter the student mark : "))
    student_id = count
    student_info_dict = {}
    student_info_dict[f"student_{student_id}_name"] = student_name
    student_info_dict[f"student_{student_id}_mark"] = student_mark

    students_dict[student_id] = student_info_dict


print(students_dict)

file = open("student_info.txt", "w")
file.write(f"{students_dict}")
file.close()


