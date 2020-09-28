#Time-O(N) / Space-O(d)
def productSum(array,multiplier=1):
    sum=0
    print(array)
    for element in array:
        if type(element) is list:
            sum+=productSum(element,multiplier+1)
        else:
            sum+=element
    return(sum*multiplier)
array=[5,6,[9,3],9]
print(productSum(array))
