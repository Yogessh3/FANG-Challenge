#O(N) Time / O(1) Space
def longestSubstring(string):
    lastseen={}
    startIdx=0
    longest=[0,1]
    for i in range(1,len(string)):
        char=string[i]
        if char in lastseen:
            startIdx=max(startIdx,lastseen[char]+1)
        if longest[1]-longest[0] < (i+1)-startIdx:
            longest[0]=startIdx
            longest[1]=i+1
        lastseen[char]=i
    return string[longest[0]:longest[1]]
print(longestSubstring("clementi"))
        
        
