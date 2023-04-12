def farenheirt():
    """ returns the temprature in farenheit"""
    celcius = float(input( "enter the temprature in celcius: "))
    f = celcius * 9/5 + 32
    return f

print(f"temperature in farenheit is  {farenheirt()}")