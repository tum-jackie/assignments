def takes_tuples(age_list):
    """This function takes a tuple of names and ages and returns a list of names of people over 18"""
    for i in age_list: # for each tuple in list
        if i[1] >= 18: #if age is greater than 18
            print (i[0]) # print the name
ages = [("tum",2), ("eve",45), ("dee",50), ("dan",7)]
takes_tuples(ages)