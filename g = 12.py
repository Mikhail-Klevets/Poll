
def binary_search(list,item):
    low = 0
    high = len(list)-1
    while low <= high:
        mind = (low+high)
        guesse =list[mind]
        if guesse == item:
            return mind
        if guesse > item:
            high = mind - 1
        else:
            low = mind+1
    return None

my_list = [1, 3, 5, 7, 9]
print (binary_search(my_list, 3)) 
print (binary_search(my_list,-1)) 
