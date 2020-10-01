#Time - O(N) / Space - O(N)
def caeserCipher(string,key):
    encodedString=[]
    newKey=key%26
    for letter in string:
        encodedString.append(getNewLetter(letter,newKey))
    return ''.join(encodedString)
def getNewLetter(letter,key):
    newLetterValue=ord(letter)+key
    if newLetterValue <=122:
        return chr(newLetterValue)
    else:
        newLetterValue = 96 + newLetterValue % 122
        return chr(newLetterValue)
word="hellozamp"
print(caeserCipher(word,126))
                        
