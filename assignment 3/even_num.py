def even_num(NUM):
    """Prints even numbers in a list"""
    for i in NUM:
        if i % 2 == 0:
            print(i)

NUM = [1,2,3,4,5,6]
even_num(NUM)