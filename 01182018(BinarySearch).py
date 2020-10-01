def binary_search(a_list, item):
    first = 0
    last = len(a_list) -1
    found = False

    while first <= last and not found:
        midpoint = (first+last) //2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint -1
            else:
                first = midpoint +1
    return first

test_list = [ 0,1,2,8,13,17,19,32,42,]
print(binary_search(test_list,2))
print(binary_search(test_list,3))
print(binary_search(test_list,13))

def binary_search(a_list, item):
    if len(a_list) ==0:
        return False
    else:
        midpoint = len(a_list) //2
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search(a_list[:midpoint], item)
        else:
            return binary_search(a_list[midpoint+1:], item)
test_list = [0,1,2,8,13,17,19,32,42]

print(binary_search(test_list,3))
print(binary_search(test_list,13))






#binary search with recursion
 def binsearch(low,high,key):
        if (l==h):
            if A[low==key]:
                return low
            else:
                return 0
        else:
            mid=low+high//2
            if (key==A[mid]):
                return mid
            if (key<mid):
                return binsearch(low,mid-1,key)
            else:
                return binsearch(mid+1,high,key)
# this is recursive algorithm   and works with  O(log n) complexity 
            
            
            


