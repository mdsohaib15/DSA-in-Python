def evaluate_postfix(expression):
    stack = []
    
    for char in expression:
        if char.isdigit():  # If the character is an operand (number)
            stack.append(int(char))
        else:  # If the character is an operator
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 // operand2)  # Integer division
                
    return stack[0]  # The final result is the only value left in the stack

# Test the function
expression = "23*54*+"
result = evaluate_postfix(expression)
print("Result:", result)
