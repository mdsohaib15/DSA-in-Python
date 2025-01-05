def ispar(s):
    stack = []
    for char in s:
      
        # Opening bracket
        if char in '({[':
            stack.append(char)
            
        # Closing Bracket    
        elif char in ')}]':
          
            # closing bracket without opening
            if not stack:
                return False
              
            # Else pop an item check for matching  
            top = stack.pop()
            if (top == '(' and char != ')') or \
               (top == '{' and char != '}') or \
               (top == '[' and char != ']'):
                return False
              
    # If an opening bracket without closing          
    return len(stack) == 0

s = '{()}[]'

if ispar(s):
    print("true")
else:
    print("false")