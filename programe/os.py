from sys import stdin
length = int(input())
array1 = list(map(int,stdin.readline().split()))
array2 = [num for num in array1 if num >=0]
mid = len(array2)//2
print(array2[mid])