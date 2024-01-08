def sum(num1, num2):
    return(num1+num2)

def dif(num1,num2):
    return(num1-num2)

def split(str):
    return(str[:str.find(" ")], str[str.find(" ")+1:])

def eval(str):
    num1, eq2 = split(str)
    op, num2 = split(eq2)
    num1 = int(num1)
    num2 = int(num2)
    if (op=="+"):
        result = sum(num1,num2)
    elif(op=="-"):
        result = dif(num1,num2)
    return(result)