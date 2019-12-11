# python3
import random
def brutesolution(arr):
    
    prev=0
    for i in range(len(arr)):
        for j in range (i+1,len(arr)):
            prev=max(prev,arr[i]*arr[j])
    return prev
def solution(numbers):
    
    max_index1 = -1
    for i in range(n):
        if max_index1 == -1 or numbers[i] > numbers[max_index1]:
            max_index1 = i
    
    max_index2 = -1
    for i in range(n):
        if i != max_index1 and (max_index2 == -1 or numbers[i] > numbers[max_index2]):
            max_index2 = i
    
    return numbers[max_index1] * numbers[max_index2]
       
       
def solution2(arr):
    
    firstmax=-1
    secondmax=-1
    for i in range (len(arr)):
        if(arr[i]>firstmax):
            secondmax=firstmax
            firstmax=arr[i]
        elif(arr[i]>secondmax):
            secondmax=arr[i]
            
    return firstmax*secondmax
            
       
    
    
        
if __name__ == '__main__':
    n=int(input())
    arr = list(map(int, input().rstrip().split()))
    result=solution2(arr)
    print(result)
    """while True:
        arr2=[]
        s=random.randint(2,1000)
        
        for x in range(s):
            r=random.randint(1,10000)
            arr2.append(r)
        #print(arr2)
        r1=brutesolution(arr2)
        r2=solution(arr2)
        if(r1!=r2):
            print(r1)
            print(r2)
            #break
        else:
            print("oki")"""
        
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
   