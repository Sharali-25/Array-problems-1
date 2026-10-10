def reverse(n):
    arr, i, j = list(range(1,n+1)), 0, n-1
    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i +=1
        j -=1
    return arr
print("Reverse 4 = ",reverse(4))
print("Reverse 6 = ",reverse(6))
n = int(input("Enter a number : "))
print(reverse(n))