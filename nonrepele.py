# to return first non repeating elements in a list
list_1 = [1, 2, 3, 4, 5, 6, 4, 3, 2, 1]
list_2 = []
dic = {}
for i in list_1:
    dic[i] = 0
#print(dic)
for i in list_1:
    dic[i] += 1
#print(dic)
for i in list_1:
    if dic[i] == 1:
        list_2.append(i)
        #print(list_2)
print(list_2[0])
