def new_string(new_word):
    """ This function takes a list of strings and returns a new list with only the strings that are longer than 5 characters"""
    word = new_word.split(" ")
    for i in word:
        if len(i) >= 5:
            print (i)

new_word =("this is a good cold extremely exhilarating apple day")
new_string(new_word)