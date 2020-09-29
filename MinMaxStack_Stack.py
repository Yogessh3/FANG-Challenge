class MinMaxStack:
    def __init__(self):
        self.stack=[]
        self.minMaxStack=[]
        
    #Time - O(1) / Space - O(1)
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()
    
    #Time - O(1) / Space - O(N)
    def push(self,data):
        self.stack.append(data)
        minValue=data
        maxValue=data
        if len(self.minMaxStack)==0:
            self.minMaxStack.append({"min":minValue,"max":maxValue})
        elif(len(self.minMaxStack)>0):
            newMinMax={}
            newMinMax["min"]=min(self.minMaxStack[-1]["min"],minValue)
            newMinMax["max"]=max(self.minMaxStack[-1]["max"],maxValue)
            self.minMaxStack.append(newMinMax)
            
    #Time - O(1) / Space - O(1)
    def getMin(self):
        return self.minMaxStack[-1]["min"]
    
    #Time - O(1) / Space - O(1)
    def getMax(self):
        return self.minMaxStack[-1]["max"]
    
m=MinMaxStack()
N=int(input())
arr=[int(x) for x in input().split()]
for i in arr:
    m.push(i)
    print('Min: ',m.getMin())
    print('Max: ',m.getMax())
m.pop()
print('Min: ',m.getMin())
print('Max: ',m.getMax())
