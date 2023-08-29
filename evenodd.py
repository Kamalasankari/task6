# to create list for even and odd numbers separately
list1 = [10, 501, 22, 37, 100, 999, 87, 351]
evenlist = []
oddlist = []
for i in list1:
    if (i % 2) == 0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print("even list :", evenlist)
print("odd list :", oddlist)


