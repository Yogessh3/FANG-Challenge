#O(N) - Time / O(1) - Space
def validateSubsequence(sequence,subsequence):
    seqIdx=0
    subSeqIdx=0
    while seqIdx<len(sequence) and subSeqIdx<len(subSequence):
        if(sequence[seqIdx]==subSequence[subSeqIdx]):
            subSeqIdx+=1
        seqIdx+=1
    return subSeqIdx==len(subSequence)
sequence=[2,3,4,5,6,8]
subSequence=[2,3,4]
print(validateSubsequence(sequence,subSequence))
