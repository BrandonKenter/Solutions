a = [2, 3, 4, 5, 6, 7]

target = 8
left, right = 0, len(a)
while left < right:
    mid = (left + right) // 2
    if a[mid] >= target:
        right = mid
    else:
        left = mid + 1
print(left)
