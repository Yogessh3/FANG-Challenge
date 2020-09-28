#Time-O(N) / Space-O(N)
def balancedBrackets(brackets):
    opening='[{('
    closing=']})'
    matching={'}':'{',']':'[',')':'('}
    stack=[]
    for bracket in brackets:
        if bracket in opening:
            stack.append(bracket)
        elif bracket in closing:
            if(len(stack)==0):
                return False
            elif(stack[-1]==matching[bracket]):
                stack.pop()
            else:
                return False
    return len(stack)==0
brackets='{}[](){{}}'
print(balancedBrackets(brackets))
