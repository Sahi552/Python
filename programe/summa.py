l1 = [2,4,3]
l2 = [5,6,4]

l3=[]
l3.append(l1[::-1])
l4 =[]
l4.append(l2[::-1])

for i in l3:
    st1 = ''
    st1 += str(i)
    print(str(st1))

print(l3,l4)
