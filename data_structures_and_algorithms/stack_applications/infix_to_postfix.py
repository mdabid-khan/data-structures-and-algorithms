def infix_to_postfix(expression):
    precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3
    }

    stack = []
    postfix = []

    for char in expression:
        if char == " ":
            continue

        # Operand
        if char.isalnum():
            postfix.append(char)

        # Left parenthesis
        elif char == "(":
            stack.append(char)

        # Right parenthesis
        elif char == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()  # remove '('

        # Operator
        else:
            while (stack and stack[-1] != "(" and
                   precedence.get(char, 0) <= precedence.get(stack[-1], 0)):
                postfix.append(stack.pop())
            stack.append(char)

    # Pop remaining operators
    while stack:
        postfix.append(stack.pop())

    return "".join(postfix)


# Test
if __name__ == "__main__":
    expression = "A + ( B*C - (D/E^F)*G )*H"
    
    print(f"Infix Expression: {expression}")
    print(f"Postfix Expression: {infix_to_postfix(expression)}")