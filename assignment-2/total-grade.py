def takes_dict(dict):
    """this functions returns total grade of student from dict with subjects """
    new_sum = sum(dict.values())
    print (new_sum)
            

grades = {"math": 80, "eng": 60, "science": 90, "religion": 70}
takes_dict(grades)