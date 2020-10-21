#Time - O(N) / Space - O(1)
def removeNode(head,n):
    first=head
    second=head
    counter=1
    while(counter<=n):
        second=second.next
        counter+=1
    if second is None:
        head.value=head.next.value
        head.next=head.next.next
        return
    while second is not None:
        first=first.next
        second=second.next
    first.next=first.next.next
    
