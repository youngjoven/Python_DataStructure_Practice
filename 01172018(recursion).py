def list_sum(num_list):
    the_sum = 0
    for i in num_list:
        the_sum = the_sum +i
    return the_sum

print(list_sum([3]))
print(list_sum([1,3,5,7,9]))

def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

print(list_sum([1,3,5,7,9]))
