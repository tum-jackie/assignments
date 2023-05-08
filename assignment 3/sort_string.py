def sort_string(word):
    """return longest word in a string"""
    new_word = word.split()
    longest_word = max(new_word, key=len)
    print(longest_word)
    

word = "my name is jackline"
sort_string(word)
