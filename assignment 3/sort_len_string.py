def sort_string(word):
    """return a list of words in ascending order based on length"""
    word.sort(key=len, reverse=False)
    print (word)

sentence = ["hello","world", "is","bot"]
sort_string(sentence)