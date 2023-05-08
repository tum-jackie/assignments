names = {"jane": 18, "jack": 7, "john": 11, "joe": 25, "jerry": 30}

def get_age(names):
    for key in names:
        if names[key] >= 18:
            print(key, names[key])
        

get_age(names)