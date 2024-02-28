def calculate(x,y,operator):
    if operator == '+':
        result = x+y
    elif operator == '-':
        result = x-y
    elif operator == '*':
        result =  x*y
    elif operator == '/':
        result = x/y
        
    return result


x = float(input('Enter x : '))
operator = input('Enter operator (+,-,*,/): ')
y = float(input('Enter y : '))
print(x,operator,y)
result=calculate(x,y,operator)
print('=',result)