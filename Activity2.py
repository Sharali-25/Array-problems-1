def left_rotate(n):
    arr = [1,2,3,4,5]
    n = n%len(arr)
    return arr[n:]+arr[:n]
print(left_rotate(3))
print(left_rotate(2))
n = int(input("Enter a number : "))
print(left_rotate(n))