def evaluate_posfixed_expression(expression):
    stack = []
    operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }

    for element in expression:  # iterate through each symbol in the expression
        if element.isdigit():
            stack.append(int(element))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[element](operand1, operand2)
            stack.append(round(result, 2))
    return stack.pop()


# lambda is used for simple functions lambda args: expression

result = evaluate_posfixed_expression("53+82-/")
print(f"Reply: {result}")




