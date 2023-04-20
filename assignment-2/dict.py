def takes_dict(dict):
    """this functions returns a list with  names of people over 18 """
    for i in dict:
        if dict[i] >= 18:
            print (i)

dict = {"tum": 2, "eve": 45, "dee": 90, "dan": 7}
takes_dict(dict)