#Time - O(NM) / Space - O(NM)
def levenshteinDistance(str1,str2):
    edits=[[j for j in range(len(str2)+1)] for i in range(len(str1)+1)]
    for i in range(1,len(str1)+1):
        edits[i][0]=edits[i-1][0]+1
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if(str1[i-1]==str2[j-1]):
                edits[i][j]=edits[i-1][j-1]
            else:
                edits[i][j]=1+min(edits[i][j-1],edits[i-1][j-1],edits[i-1][j])
    return edits[-1][-1]
str1="YABD"
str2="ABC"
if len(str1)>len(str2):
    str1,str2=str2,str1
print(levenshteinDistance(str1,str2))
                
