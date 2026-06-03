import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    all_students_and_subjects = students.merge(subjects, how='cross')

    exam_count_per_student = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')

    student_exam_count = all_students_and_subjects.merge(exam_count_per_student, on=['student_id', 'subject_name'], how='left')
    student_exam_count['attended_exams'].fillna(0, inplace=True)

    return student_exam_count.sort_values(by=['student_id', 'subject_name'])