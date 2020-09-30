#O(N+M) Time / O(M) Space (i.e) Storing the pattern list
def knuthMorrisPrattAlgorithm(string,substring):
    pattern=buildPattern(substring)
    return matchPattern(string,substring,pattern)
def buildPattern(substring):
    i=1
    j=0
    pattern=[-1 for i in substring]
    while i<len(substring):
        if(substring[i]==substring[j]):
            i+=1
            j+=1
        elif(j>0):
            j=pattern[j-1]+1
        else:
            i+=1
    return pattern
def matchPattern(string,substring,pattern):
    i=0
    j=0
    while i +len(substring) - j < len(string):
        if(string[i]==substring[j]):
            if(j==len(substring)-1):
                return True
            i+=1
            j+=1
        elif(j>0):
            j=pattern[j-1]+1
        else:
            i+=1
    return False
print(knuthMorrisPrattAlgorithm("Clementis","mentis"))
    
