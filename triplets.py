# to find triplets in a list whose sum is 59
list_1 = [10, 20, 30, 9]
sum = 59
triplets = []
for i in range(0, len(list_1) - 2):

    for j in range(i + 1, len(list_1) - 1):

        for k in range(j + 1, len(list_1)):

            if list_1[i] + list_1[j] + list_1[k] == sum:
                temp = []
                temp.append(list_1[i])
                temp.append(list_1[j])
                temp.append(list_1[k])
                triplets.append(list(temp))
print("Triplets are : " + str(triplets))