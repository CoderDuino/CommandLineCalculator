import time

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    return False

def ValidateInput(equation):
    if len(equation) != 3:
        return False
    if not (is_number(equation[0]) and is_number(equation[2])):
        return False
    if not equation[1] in ["*", "/", "-", "+"]:
        return False

    return True

print("Welcome to command line calculator!")
time.sleep(1)   # sleep for a second

while True:
    equation = input("Enter your calculation: ")    # look for calculation

    if equation.lower() in ["exit", "stop", "quit", "end", "leave", "done", "finish"]:
        break

    if equation.lower() in ["expression", "test", "expr", "exec"]:
        expressionInput = input("Enter Expression: ")
	print(eval(expressionInput()))
	continue

    equation = equation.split(" ")  # split equation into three pieces

    if not ValidateInput(equation):
        continue

    equation[0] = float(equation[0])
    equation[2] = float(equation[2])

    if equation[1] == "*":
       print(str(equation[0] * equation[2]))

    elif equation[1] == "/":
        print(str(equation[0] / equation[2]))

    elif equation[1] == "+":
        print(str(equation[0] + equation[2]))

    elif equation[1] == "-":
        print(str(equation[0] - equation[2]))
