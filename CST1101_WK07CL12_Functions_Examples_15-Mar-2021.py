# Topic - Functions: Examples and Exercises
# CST1101-OLXX Spr-2021 WK07CL12 Review
# by Professor Patrick  PaSlattery@CityTech.CUNY.edu


### VOID FUNCTION
print("Example of a void function for its side effects")
# a simple function which prints whatever argument it receives
def print_void(argument):
    """This void function prints the value passed in as an argument"""
    print ("Your value is:", argument)

print_this = input("What content should we use as an argument to print_void()? > ")
print_void(print_this)
# the following statements are scaffolding to pause and wait for Enter
print()
wait = input("Hit Enter to continue > ")
print()


### LOCAL VARIABLES
print("Example of local and global variable")
# a simple function which changes the value of a local variable
def change_value(argument):
    """This function changes the local value passed in to 17"""
    print ("Inside (local) argument is:", argument)
    argument = 17
    print ("Inside (local) argument is changed to:", argument)

number = 42
print ("Outside (global) number is:", number)
change_value(number)
print ("Outside (global) number is still:", number)
# the following statements are scaffolding to pause and wait for Enter
print()
wait = input("Hit Enter to continue > ")
print()


### GLOBAL VARIABLES INSIDE A FUNCTION
print("Example of using the global statement to access a global variable")
# a simple function which uses global to change a variable outside of scope
def change_number():
    """This function changes the value passed in to 19 (global)"""
    global number
    number = 19

number = 55
print ("Outside (global) number is:", number)
change_number()
print ("Outside (global) number is now:", number)
# the following statements are scaffolding to pause and wait for Enter
print()
wait = input("Hit Enter to continue > ")
print()


### RETURN VALUES
print("Example of returning a value(s)")
# a simple function which returns the square of an argument
def square(root):
    """This function calculates the square of the argument value"""
    result = root * root
    return result


# a rationalizing the function which returns the square of an argument
def square(root):
    """This function calculates the square of the argument value"""
    # result = num * num
    return root * root

# calling the square() function from within a for loop
for i in range(1,11):
    print(square(i))
# the following statements are scaffolding to pause and wait for Enter
print()
wait = input("Hit Enter to continue > ")
print()


### DEFAULT ARGUMENTS #1
print("Example of setting a default value for an argument")
# Using a default value for the argument in our earlier square() function
def square(root = 1):
    """This function calculates the square of a the argument value"""
    return root * root

# calling the square() function and allowing the default value for the argument
print(square())
# the following statements are scaffolding to pause and wait for Enter
print()
wait = input("Hit Enter to continue > ")
print()


### DEFAULT ARGUMENTS #2
print("Examples of using/not-using a default value for an argument")
# Using a default value to count number of times to prompt the user
def prompt_user(prompt, num_tries = 2):
    """This function prompts the user for 'yes' or 'no' a number of times"""
    answer = input(prompt)

    while (answer != "yes" and answer != "no" and num_tries > 1):
       num_tries = num_tries - 1
       print ("Try again")
       answer = input(prompt)

# Calling prompt_user() with or without the default value
prompt_user("Enter yes or no: ")
prompt_user("Enter yes or no: ", 4)
# the following statements are scaffolding to pause and wait for Enter
print()
wait = input("Hit Enter to continue > ")
print()


### KEYWORD ARGUMENTS
print("Example of using keywords to assign values to arguments")
# Calling prompt_user() with keyword arguments    
prompt_user(prompt="Hello ")
prompt_user(num_tries=1, prompt="Hi ")
# the following statements are scaffolding to pause and wait for Enter
print()
wait = input("Hit Enter to continue > ")
print()



