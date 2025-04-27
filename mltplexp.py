try:
    num1, num2, = eval(input("Enter two numbers, seperated by a comma: "))
    result = num1 / num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by zero is error!")
except SyntaxError:
    print("Comma is missing. Enter numbers seperated my comma. eg; 1, 2")
except:
    print("wrong input")
else:
    print("No exceptions")
finally:
    print("This will excecute no matter what")