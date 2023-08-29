# to create list for even and odd numbers separately
list1 = [10, 501, 22, 37, 100, 999, 87, 351]
primelist = []

for i in list1:

    for j in range(2, i):

        flag = 0
        if (i % j) == 0:
            flag = 1
            break
    else:
        primelist.append(i)
print("prime numbers:", primelist)


