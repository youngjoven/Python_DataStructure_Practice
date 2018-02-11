def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) -1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i+1]:
                exchanges = True
                temp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = temp
                pass_num = pass_num -1

a_list = [20,30,40,90,50,60,70,80,100,110]
short_bubble_sort(a_list)
print(a_list)


def selection_sort(a_list):
    for fill_slot in range(len(a_list)-1, 0, -1):
        pos_of_max = 0
        for location in range(1,fill_slot+1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
        temp = a_list[fill_slot]
        a_list[fill_slot] = a_list[pos_of_max]
        a_list[pos_of_max] = temp

a_list = [54,26,93, 17, 77 ,31, 44,55,20]
selection_sort(a_list)
print(a_list)
