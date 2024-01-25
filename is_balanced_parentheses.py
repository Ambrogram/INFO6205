def is_balanced_parentheses(string):
    # Map of corresponding opening and closing parentheses
    parentheses_map = {')': '(', ']': '[', '}': '{'}
    
    # Initialize a stack
    stack = []
    
    # Iterate through each character in the string
    for char in string:
        if char in parentheses_map.values():
            # Push opening parentheses onto the stack
            stack.append(char)
        elif char in parentheses_map:
            # Check for matching opening parentheses
            if stack and stack[-1] == parentheses_map[char]:
                stack.pop()
            else:
                return False
                
    # Return True if all parentheses are matched
    return not stack

# Test the function with provided examples
print(is_balanced_parentheses("I { love [ the {rains}()]}"))  # Output: True
print(is_balanced_parentheses("I { love [ the {rains ] ()"))  # Output: False
