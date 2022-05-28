def binary_search(arr, val):
  if arr is None or len(arr) == 0 or val < arr[0] or val > arr[-1]:
    return -1
  left = 0
  right = len(arr) - 1
  while True:
    mid = round((left + right)/2)
    if arr[mid] == val:
      return mid
    if right < left:
      return -1
    if val < arr[mid]:
      right = mid - 1
    else:
      left = mid + 1
  return mid

assert binary_search([], 1) == -1
assert binary_search([0,2,4,6], 2) == 1
assert binary_search([0, 2, 4, 6, 8, 10, 12, 14, 16], 0) == 0
assert binary_search([0, 2, 4, 6, 8, 10, 12, 14, 16], 16) == 8
assert binary_search([0, 2, 4, 6, 8, 10, 12, 14, 16, 18], 8) == 4
arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
for idx, val in enumerate(arr):
  assert binary_search(arr, val) == idx
print("all cases passed")