# Time - O(N) / Space - O(1)
def shiftLinkedList(head,key):
    listTail=head
    listLength=1
    while listTail is not None:
        listTail=listTail.next
        listLength+=1    
    newKey=abs(key)%listLength   
    offset=listLength-newKey if key>0 else newKey
    if(offset==0):
        return head
    newTail=head
    for i in range(1,offset):
        newTail=newTail.next
    newHead=newTail.next
    newTail.next=None
    listTail.next=head
    return newHead
        
    
    
