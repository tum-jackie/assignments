def total_grade(student_grades):
    """return the overall student grade"""
    total_sum = sum(student_grades.values())
    print(total_sum) 

grades = {"math":80, "bio": 90, "phyc": 75}
total_grade(grades)