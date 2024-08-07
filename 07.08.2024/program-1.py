def bb_st(arr):
    n=len(arr)
    for i range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=list(map(int,input("Enter Numbers : ").split()))
print("Sorted array : ",bb_st(arr))
