#O(N) - Time / O(1) - Space
def palindromeCheck(string):
    leftIdx=0
    rightIdx=len(string)-1
    while leftIdx < rightIdx:
        if(string[leftIdx]!=string[rightIdx]):
            return False
        leftIdx+=1
        rightIdx-=1
    return True
string="madam"
print(palindromeCheck(string))
