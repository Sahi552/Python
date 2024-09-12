'''get a list ,print number divisible by 5 or 7 in asc orde'''
'''l = [ int(i) for i in input().split()]
a = []'''
'''for i in l:
   if i%5==0 or i%7==0 :
      a.append(i)
a.sort()
print(a)'''

'''list and n , print n largest number'''
'''n = int(input())
l.sort(reverse=True)
a=l[:n]
print(a)'''
 
'''count and print all odd num in a list'''
'''for i in l:
    if i % 2 != 0 :
        a.append(i)
print(a ,"number of odd number",len(a))'''

'''shift all zeros in a list towards right by maintaing order'''
'''f = [1,0,2,10,5,0,10]
d =[]
e =[]
for i in f:
    if i != 0:
        d.append(i)
    else:
        e.append(i)
d.extend(e)        
print(d)'''

'''take n,k , list l of len n all of 0 ,if k is even change 0 to 1 in even index else odd index'''  
'''n,k = int(input()),int(input())
l = []
for i in range(n):
    l.append(0)
print(l) 
for q in range(len(l)):
    if k%2==0 and q%2==0:
        l[q]=1
    elif k%2!=0 and q%2!=0:
        l[q]=1            
print(l)'''

'''replace all vowels in a string to *'''
'''s =input()
v ="aeiouAEIOU"
for k in v:
       s=s.replace(k,'*')    
print(s)'''

'''palindrome or not'''
'''s = "malayalam" 
s2 = s[::-1]
if s==s2:
    print("the given string is palindrome")
else:
    print("The given string is not a palindrome")'''
    
'''Accept 2 strings and check anagram or not'''
'''s1 = input("Enter string1:")
s2 = input("Enter string 2:")
if (sorted(s1) == sorted(s2)):
    print("The given string is anagram")
else:
    print("The given string is not a anagram")'''

'''accept string s .replace 3 consecutive vowels as *'''
'''s ="aaabcideee"
v = "aeiouAEIOU"
for k in v:
    s = s.replace(k,'k').replace('kkk',"*")
print(s)  '''        


'''perfect num or not 6 = 1+2+3''' 
'''n = int( input("enter a number:"))
m = 0
for i in range(1,n):
    if n % i == 0:
        m += i

if m == n:
    print("the given number is perfect number")    
else:
    print("the given number is not a perfect number")'''
    
'''print the second prime num in list'''

'''print second prime number'''

'''input_string = input("Enter a list of numbers separated by spaces: ")
numbers_as_strings = input_string.split()
if len(numbers_as_strings) >= 2:
    if numbers_as_strings[1].isdigit() or (numbers_as_strings[1][0] == '-' and numbers_as_strings[1][1:].isdigit()):
        second_number = int(numbers_as_strings[1])
        print(f"The second number in the list is: {second_number}")
    else:
        print("The second element is not a valid integer.")
else:
    print("The list must contain at least two elements.")
'''
'''print the list unique elements in sorted order'''
'''l = [1,2,1,4,5,4,6]
s=[]
a=set(l)
for i in a:
    s.append(i)
print(s)'''

'''print the number along with its index'''
'''l=[1,2,3,4,5,6]
for i in l:
    print(i,l.index(i),end ='')
a=enumerate(l)    
print(list(a))'''

'''print all the composte numbers between range'''
'''st = int(input())
en = int(input())
for i in range(st,en):
    if i>1:
        comp = False
        for j in range(2,i):
            if (i % j)==0:
                comp =True
                break
        if comp:
            print(i,end="")'''

'''def bubble_sort(arr):
    n = len(arr)
    swaps = 0

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return swaps

if __name__ == "__main__":
    # Input list of integers
    numbers = [64, 34, 25, 12, 22, 11, 90]

    # Perform bubble sort and get the number of swaps
    num_swaps = bubble_sort(numbers)

    print("Sorted array:", numbers)
    print("Number of swaps:", num_swaps)
'''
 
a = map(lambda x: x**3, [i for i in range(1, 11)])
print(list(a))



