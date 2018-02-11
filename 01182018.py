def sequential_search(a_list, item):
    pos = 0
    found = False
    while pos <len(a_list) and not found:
        if a_list[pos] == item:
            found =True
        else:
            pos = pos+1

    return item




test_list = [1,2,32,8,17,19,42,13,0]

print(sequential_search(test_list,3))
print(sequential_search(test_list,13))

def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos <len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
         if a_list[pos] > item:
                stop = True
         else:
            pos = pos+1
    return found
test_list = [0,1,2,8,13,17,19,32,42]
print(ordered_sequential_search(test_list, 3))
print(ordered_sequential_search(test_list,13))
