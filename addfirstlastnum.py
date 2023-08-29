# to add first and last integer of a number
s = input("enter number :")
num = [int(x) for x in str(s)]
print(num)
last = (len(num))
sum = num[0] + num[last-1]
print(sum)
