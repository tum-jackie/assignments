def  list_string(word):
    """return a new list with strings that have len greater than 5"""
    new_list=[]
    for i in word:
        if len(i) >= 5:
            new_list.append(i)
    print (new_list)

word =["this", "is", "a", "good", "cold", "extremely", "exhilarating", "apple", "day"]
list_string(word)