
def binary_search(list,item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low+high)
        guesse = list[mid]
        if guesse == item:
            return mid
        if guesse > item:
            high = mid - 1
        else:
            low = mid+1
    return None
my_list = [1, 3, 3, 5, 7, 9]
print (binary_search(my_list, 3)) 
print (binary_search(my_list,-1)) 
