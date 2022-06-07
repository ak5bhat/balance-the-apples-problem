count = int(input())
arr = []
for i in range(count):
    arr.append(int(input()))

def arrangeapples(count,arr):
    l,r = 0, int(count-1)
    sum1= arr[l]
    sum2 = arr[r]
    while l < r:
        if sum1<sum2:
            sum1 += arr[l+1]
            l+=1
        elif sum1>sum2:
            sum2 += arr[r-1]
            r -= 1
        else:
            print(l+1)
            break
        
    
arrangeapples(count,arr)