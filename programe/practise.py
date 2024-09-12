def feed_rats(rat , unit , arr):
    needed = rat * unit
    print(needed)
    resulting_array = []
    temp = 0
    for i in arr:
        if temp < needed:
          print(temp)
          resulting_array.append(i)
          temp += i
        else:
            break
    print(resulting_array)
    value = len(resulting_array)        
    print(value)

feed_rats(7,2,(2,8,3,5,7,4,1,2))