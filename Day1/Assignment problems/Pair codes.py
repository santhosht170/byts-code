def getPairsCount(self, arr, n, k):  
    count=0  
    for i in range(0,n):  
        for j in range(i+1,n):  
            if arr[i]+arr[j]==k:  
               count+=1  
    print(count)
