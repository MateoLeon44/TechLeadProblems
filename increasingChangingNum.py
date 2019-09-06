'''You are given an array of integers in an arbitrary order. Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).'''


def check(lst):
  contador = 0
  for x in range(0,len(lst)-1):
      if(lst[x] >= lst[x+1]):
          contador += 1
      if(contador > 1):
          return False
  return True
        
print(check([13, 4, 7]))
# True
print(check([5,1,3,2,5]))
# False
print(check([1,2,3,4,1,1]))
print(check([1,2,3,3,4,3]))
print(check([1,2,3,4,1]))
