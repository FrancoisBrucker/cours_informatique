def colle(tab1, tab2):
    i1 = i2 = 0
    tab_colle = []
    while i1 < len(tab1) or i2 < len(tab2):
        if i2 == len(tab2):
            tab_colle.append(tab1[i1])
            i1 += 1
        elif i1 == len(tab1):
            tab_colle.append(tab2[i2])
            i2 += 1
        elif tab1[i1] < tab2[i2]:
            tab_colle.append(tab1[i1])
            i1 += 1
        else:
            tab_colle.append(tab2[i2])
            i2 += 1
    return tab_colle


print(colle([1, 4, 7], [0, 2, 3, 98]))
