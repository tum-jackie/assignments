def takes_tuples(age_tuple):
    """This function takes a tuple of names and ages and returns a 
       list of names of people over 18
    """
    age_list =[]
    for i in age_tuple: # for each tuple in list
        if i[1] >= 30: #if age is greater than 30
            age_list.append(i[0]) #add name to list
            print (age_list) 

ages = [("tum",2), ("eve",45), ("dee",50), ("dan",7)]
takes_tuples(ages)