# to find duplicates in given 3 lists
list_1 = ["a", "b", "c", "d", "e"]
list_2 = ["a", "e", "i", "o", "u"]
list_3 = ["a", "p", "p", "l", "e"]
# list_1 = [10, 12, 14, 16, 20]
# list_2 = [12, 18, 20, 22,24]
# list_3 = [6, 8, 10, 12, 15]
duplist= []
for i in list_1:
    if i in list_2 and i in list_3:
        duplist.append(i)
print(duplist)