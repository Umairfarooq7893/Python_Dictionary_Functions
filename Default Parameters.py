### Assigning a default value to a parameter in a function
def Calc_Product(a,b=2):
    p = a * b
    print(p)
    return p

# calling the function with both parameters
Calc_Product(3,2)
Calc_Product(4,2)

# calling the function with one parameter, second will take default value of 2
Calc_Product(3)
Calc_Product(4)

### Assigning a default value to multiple parameters in a function
def Calc_prodt(a=2,b=3,c=4):
    p = a * b * c
    print(p)
    return(p)