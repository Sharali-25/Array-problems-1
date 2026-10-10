# part 1 reversed score check
def reverse(score):
    arr, start, end = list(range(1,score+1)), 0, score-1
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start +=1
        end -=1
    return arr
print("Reverse 3 = ",reverse(3))
print("Reverse 1 = ",reverse(1))
score_check = int(input("Enter a score : "))
print(reverse(score_check))

# part 2 sliced score check
def left_rotate(score):
    arr = [1,2,3,4,5,6,7]
    score = score%len(arr)
    return arr[score:]+arr[:score]
print(left_rotate(3))
print(left_rotate(7))
scorecheck = int(input("Enter a score number "))
print(left_rotate(scorecheck))
