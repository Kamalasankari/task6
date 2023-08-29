def sublists(lst):
    n = len(lst)
    list_2 = []

    for i in range(n):
        for j in range(i + 1, n + 1):
            list_2.append(lst[i:j])

    return list_2

list_1 = [4, 2, -3, 1, 6]
list_2 = sublists(list_1)
print("sublists are ",list_2)
num = len(list_2)
#print(num)
#print(list_2[1])
n = 0
for k in range(0, num):
    list_3 = list_2[k]
    #print(list_3)
    for l in range(0, len(list_3)):
        n = n + list_3[l]
        #print(n)

    if n == 0:
        print("sublist whose sum is 0 :",list_3)
    n = 0