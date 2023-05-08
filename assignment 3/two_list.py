def takes_two_list(lista, listb):
    """return the numbers appearing in both lists"""
    new_list = []
    for i in lista:
        if i in listb:
            new_list.append(i)
    print(new_list)

list1 = [1,2,3,4,5,6,8]
list2 = [2,4,5,7,8,9]
takes_two_list(list1, list2)