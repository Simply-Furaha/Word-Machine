

def solution(S):
    Max_value = 2**20 - 1
    stack = []

    
    for s in S.split():
        if s.isdigit():
            stack.append(int(s))
        elif s == 'DUP':
            if not stack:
                return -1
            stack.append(stack[-1])
        elif s == 'POP':
            if not stack:
                
                return -1
            stack.pop()
        elif s == '+':
            if len(stack) < 2:
                return -1
            stack.append(stack.pop() + stack.pop())
        elif s == '-':
            if len(stack) < 2:
                return -1
            stack.append(stack.pop() - stack.pop())
        if stack[-1] > Max_value:
            return -1
        if stack[-1] < 0:
            return -1
        print(stack)
    return stack[-1] if stack else -1

solution("13 DUP 4 POP 5 DUP + DUP + -")
            




 
 
