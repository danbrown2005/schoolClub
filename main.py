from inputHandler import accept_int, accept_str


def main():
    student_count = accept_int("Enter your student count: ", "Invalid value entered")
    students = {}
    for i in range(student_count):
        student_name = accept_str("Enter your students name: ", "Invalid name entered")
        student_mark = accept_int(prompt_message=f"Enter {student_name}'s mark: ", error_message="Invalid mark entered",
                                  upper_bound=100)
        students[student_name] = student_mark
        return_grade(student_mark, student_name, True)
    output_sorted_dict(students)


def return_grade(student_grade, student_name, alert=False) -> str:
    if student_grade < 40:
        return "Fail"
    elif student_grade < 51:
        return "Pass"
    elif student_grade < 70:
        return "Merit"
    if alert:
        print(f"Distinction has been achieved by {student_name} who gained {student_grade} marks!")
    return "Distinction"


def output_sorted_dict(unsorted_dictionary):
    index = 1
    for key, value in dict(sorted(unsorted_dictionary.items(), key=lambda item: item[1], reverse=True)).items():
        print(f"{index}: Name: {key}, Mark: {value} Grade: {return_grade(value, key)}")
        index += 1


if __name__ == "__main__":
    main()
