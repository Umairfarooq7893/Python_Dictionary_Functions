# ### FUNCTIONS

# # block of statements or code that perform a specific task
# # the building blocks of any programme
# # reusable pieces of a code
# # functions are defined using the "def" keyword

# # For Finding sum, of many numbers individually, We have to write code separately for each case
# # Hence We can , Write code once and call it multiple times

# # def fxn_name(parameter1,parameter2,parameter3,):

# def calculate_sum(a,b,c):                 # defining calculate sum fxn
#     sum = a + b + c                       # performing the task
#     return sum                            # returning the resut of the task

# # calling the function
# print(calculate_sum(10,10,10))
# print(calculate_sum(10,10,20))
# print(calculate_sum(10,20,20))

# ### KEY POINT

# # EXAMPLE 5 (This will Only return the value , And not print it)
# def Calc_Avg(a,b,c,d):
#     sum = a+b+c+d
#     avg = sum / 4
#     return avg
# Calc_Avg(10,20,30,40)

# # Example 5 (This will return the value and print it)
# def Calc_Avg(a,b,c,d):
#     sum = a+b+c+d
#     avg = sum / 4
#     print(avg)
#     return avg
# Calc_Avg(10,20,30,40)

### Three different examples of functions with parameters and return values

# Example 1
# calculates the sum, returns it, But not prints it
def Sum1(a,b):
    sum1 = a + b
    return sum1
Sum1(10,10)

# Example 2
# calculates the sum, returns  it, but prints it immediately 
# However, it doesn't return the value for further use.
def Sum2(a,b):
    sum2 = a + b
    print(sum2) 
Sum2(10,20)

# Example 3
# calculates the sum, prints it immediately,returns it
def Sum3(a,b):
    sum3 = a + b
    print(sum3) 
    return sum3
Sum3(20,20)








