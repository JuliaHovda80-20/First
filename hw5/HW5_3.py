n = 5
for i in range (1,n + 1):
    tmp_list = list()
    for j in range(1,i+1):
        tmp_list.append(str(j))
    print(" ".join(tmp_list))
