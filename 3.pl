student_teacher_sub_code('Alice', 'Mr. Smith', 'CS101').
student_teacher_sub_code('Bob', 'Ms. Johnson', 'MATH201').
student_teacher_sub_code('Charlie', 'Dr. Brown', 'PHYS301').

find_teacher(Student, SubjectCode, Teacher) :-
    student_teacher_sub_code(Student, Teacher, SubjectCode).

find_students(Teacher, SubjectCode, Students) :-
    findall(Student, student_teacher_sub_code(Student, Teacher, SubjectCode), Students).

find_subject_codes(Teacher, SubjectCodes) :-
    findall(SubjectCode, student_teacher_sub_code(_, Teacher, SubjectCode), Codes),
    list_to_set(Codes, SubjectCodes).

find_teachers_by_subject(SubjectCode, Teachers) :-
    findall(Teacher, student_teacher_sub_code(_, Teacher, SubjectCode), List),
    list_to_set(List, Teachers).
