def is_valid_parenthesis(s):
    pair = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    opener = "({["
    stack = []

    for char in s:
        if char in opener:
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if pair[char] != top:
                return False

    return not stack
    

if __name__ == "__main__":
    print(is_valid_parenthesis("()"))
    print(is_valid_parenthesis("()[]{}"))
    print(is_valid_parenthesis("(]"))
