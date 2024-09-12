#pattern

'''
n = 5
#
##
###
####
#####
'''
n = int(input("enter no of row :"))
s = input("what should print :")

for i in range(1,n+1):
    for j in range(1,i+1):
        print(s,end="")
    print()