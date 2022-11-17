class Student :
    
    instance_count = 0
    __student_info_list = []

    def __init__(self, id, name, age, _class) -> None:
        self.student_id = id
        self.student_name = name
        self.student_age = age
        self.student_class = _class

        self.student_info = dict()
        self.student_info["id"] = self.student_id
        self.student_info["name"] = self.student_name
        self.student_info["age"] = self.student_age
        self.student_info["class"] = self.student_class
        Student.__student_info_list.append(self.student_info)

        Student.instance_count +=1

    def get_student_info (self) :
        return self.student_info

    @property
    def get_all_students_info () :
        # return "hello testing..."
        return Student.__student_info_list


student_1 = Student(5666, "Sa'ad", 24, "masters")
student_2 = Student(5667, "nasim", 25, "masters")
student_3 = Student(5668, "rasel", 26, "masters")

# print(student_3.get_student_info())
print(Student.get_all_students_info)
