# reverse the given list

def reverseList(A):
  print( A[::-1])


A = [10, 20, 30, 40, 50]
reverseList(A)

#second method

def reverseList(A, start, end):
  while start < end:
    A[start], A[end] = A[end], A[start]
    start += 1
    end -= 1

A = [10, 20, 30, 40, 50]
reverseList(A, 0, 4)
print(A)