# Resources - https://www.programiz.com/python-programming/examples/fibonacci-recursion

# Memoization - for future call dont have to repeat the work

num_history = {} # Creating a dictionary that stores recent function calls.

def fibonacci(number):
    if number in num_history: # If we have cached the value, then we can simply return it, otherise we must compute the Nth term
        return num_history[number] # Compute the value first, cache the value and then return that value. 

# compute the Nth term 
    if number == 1:
        value = 1

    elif number == 2:
        value = 1

    elif number > 2:
        value = fibonacci(number-1) + fibonacci(number-2) # recursion because its a function that calls itself

# Lastly, store the return value in our fibonacci cache directionary, then return it. 
    num_history[number] = value
    return value

for o in range(1, 90):
    print(o, ":", fibonacci(o))