def sort_string(words):
    """ returns a list of strings sorted  by length with short strings first"""
    words.sort(key = len, reverse = True) # .sort(key = len, reverse = True) returns sorted list in descending order
    print (words)

words = ["this", "is", "a", "good", "cold", "extremely", "exhilarating", "apple", "day"]
sort_string(words)