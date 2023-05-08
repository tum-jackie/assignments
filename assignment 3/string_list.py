WORDS = ['hello', 'world', 'everything', 'majesticaly']

def string_list(WORDS):
    """adds words in list longer than 5 to a new list"""
    new_list = []
    for i in WORDS:
        if len(i) > 5:
            new_list.append(i)
    print(new_list)

string_list(WORDS)