def anagram_solution2(s1,s2):
    a_list1=list(s1)
    a_list2=list(s2)
    a_list1.sort()
    a_list2.sort()

    pos = 0
    matches = True

    while pos <len(s1) and matches:
        if a_list1[pos] == a_list2[pos]:
            pos=pos +1
        else:
            matches=False

    return matches

print(anagram_solution2('abcde','edcba'))

