def fibonacci(num):
    """returns a list of fibonacci numbers up to the number passed in"""
    num1 = 0
    num2 = 1
    num_list = [num1, num2]
    while num2 <= num:
        num3 = num1 + num2 
        num1 = num2
        num2 = num3
        num_list.append(num3)
    return num_list[:-1]



result = int(input("enter a number"))
print(f"{fibonacci(result)}")
