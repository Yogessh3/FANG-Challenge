# Time-O(N^2) / Space-O(N^2)
class SuffixTrie:
    def __init__(self,string):
        self.root={}
        self.endSymbol='*'
        self.createSuffixTrie(string)
    def createSuffixTrie(self,string):
        for i in range(len(string)):
            self.insertAtSuffixTrie(i,string)
    def insertAtSuffixTrie(self,i,string):
        node=self.root
        for j in range(i,len(string)):
            letter=string[j]
            if letter not in node:
                node[letter]={}
            node=node[letter]
        node[self.endSymbol]=True
    def contains(self,key):
        node=self.root
        for i in range(len(key)):
            letter=key[i]
            if letter not in node:
                return False
            node=node[letter]
        return self.endSymbol in node
strie=SuffixTrie('babc')
print(strie.contains('abc'))
            
