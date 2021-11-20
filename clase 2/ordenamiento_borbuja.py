def ordenamientoBorbuja(arr):
    n = len(arr)  #1
    for i in range(n-1): 
        print(i) #n
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #n^2

#n^2+n+1
#O(n^2)