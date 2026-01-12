def marks(**kwargs): # kwargs is a dictionary with all the key value pairs which were passed to marks
    # for item in kwargs.keys():
    for name, score in kwargs.items(): # Simpler version of the for loop
        print(f"The marks of {name}, is {score}")

marks(joshua=90, joel=87, joash=77)