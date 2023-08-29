n = [10,20,30,15,25,60]
m = len(n)
n.sort()
min = n[0]
n.sort(reverse=True)
max = n[0]
diff = max - min
print("the number of mangoes in each student bag is ", diff)
