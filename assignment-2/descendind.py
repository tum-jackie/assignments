def sort_nums(list):
    """returns a list of numbers in descending order"""
    new_list = list.sort(reverse = True) # .sort(reverse = true) returns sorted list in descending order
    print (list)

nums = [2,6,0,7,8,5]
sort_nums(nums)