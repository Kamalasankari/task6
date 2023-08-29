# to find happy numbers from the list
list1 = [10, 501, 22, 37, 100, 999, 87, 351]
def is_Happy_num(n):
  past = set()
  while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
  return True
res_list=[]
for i in list1:

    if is_Happy_num(i):
        res_list.append(i)

print(res_list)


